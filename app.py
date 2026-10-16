<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>أبو نمر - خدمات صيانة وإكساء المنازل في بورصة | Bursa Ev Tadilat & Dekorasyon</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
        body { font-family: 'Cairo', sans-serif; }
        .floating-whatsapp {
            position: fixed;
            bottom: 25px;
            right: 25px;
            z-index: 999;
        }
        html[dir="ltr"] .floating-whatsapp {
            right: auto;
            left: 25px;
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 flex flex-col min-h-screen">

    <!-- Header / Navbar -->
    <header class="bg-slate-900 text-white sticky top-0 z-50 shadow-md">
        <div class="max-w-7xl mx-auto px-4 py-3 flex justify-between items-center">
            <div class="flex items-center space-x-3 space-x-reverse">
                <div class="bg-amber-500 text-slate-900 p-2 rounded-lg font-bold text-xl">
                    <i class="fa-solid fa-paint-roller"></i>
                </div>
                <div>
                    <h1 class="font-bold text-lg leading-tight" id="nav-title">أبو نمر للإكساء والصيانة</h1>
                    <p class="text-xs text-amber-400" id="nav-subtitle">بورصة | Bursa</p>
                </div>
            </div>

            <div class="flex items-center gap-3">
                <!-- Language Toggle Button -->
                <button onclick="toggleLanguage()" class="bg-slate-800 hover:bg-slate-700 text-amber-400 border border-amber-500/30 px-3 py-1.5 rounded-lg text-sm font-semibold transition flex items-center gap-2">
                    <i class="fa-solid fa-globe"></i>
                    <span id="lang-btn-text">Türkçe</span>
                </button>

                <!-- Admin Login Button -->
                <button onclick="openAdminModal()" class="bg-amber-500 hover:bg-amber-600 text-slate-900 px-3 py-1.5 rounded-lg text-sm font-bold transition flex items-center gap-1">
                    <i class="fa-solid fa-user-gear"></i>
                    <span id="admin-btn-text">الإدارة</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-slate-900 via-slate-800 to-amber-950 text-white py-16 px-4 text-center relative overflow-hidden">
        <div class="max-w-4xl mx-auto">
            <span class="bg-amber-500/20 text-amber-400 text-xs md:text-sm font-bold px-4 py-1.5 rounded-full border border-amber-500/30 inline-block mb-4" id="hero-badge">
                📍 بورصة - جميع المناطق / Bursa Tüm Bölgeler
            </span>
            <h2 class="text-3xl md:text-5xl font-extrabold mb-4 leading-tight" id="hero-heading">
                خدمات الدهان، السيراميك، الصحية، والكهرباء
            </h2>
            <p class="text-slate-300 text-base md:text-lg mb-8 max-w-2xl mx-auto" id="hero-desc">
                خبرة وعناية فائقة في تشطيب وصيانة المنازل والمحلات بأعلى جودة وأفضل الأسعار.
            </p>
            <div class="flex flex-wrap justify-center gap-4">
                <a href="https://wa.me/905317327802?text=مرحباً%20أبو%20نمر،%20أريد%20الاستفسار%20عن%20خدمة" target="_blank" class="bg-green-600 hover:bg-green-700 text-white font-bold px-6 py-3 rounded-xl shadow-lg hover:shadow-green-500/30 transition flex items-center gap-2 text-lg">
                    <i class="fa-brands fa-whatsapp text-2xl"></i>
                    <span id="btn-wa">تواصل واتساب</span>
                </a>
                <a href="tel:+905317327802" class="bg-amber-500 hover:bg-amber-600 text-slate-900 font-bold px-6 py-3 rounded-xl shadow-lg transition flex items-center gap-2 text-lg">
                    <i class="fa-solid fa-phone"></i>
                    <span id="btn-call">اتصال مباشر</span>
                </a>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="py-12 px-4 max-w-7xl mx-auto">
        <h3 class="text-2xl md:text-3xl font-bold text-center mb-8 text-slate-900" id="services-title">خدماتنا الرئيسية</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- Service 1 -->
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-md transition">
                <div class="w-12 h-12 bg-amber-100 text-amber-600 rounded-xl flex items-center justify-center text-2xl mb-4">
                    <i class="fa-solid fa-paint-roller"></i>
                </div>
                <h4 class="font-bold text-xl mb-2 text-slate-900" id="s1-title">الدهان والديكور</h4>
                <p class="text-slate-600 text-sm" id="s1-desc">دهان منازل داخلي احترافي، تجهيز معجونة، معالجة رطوبة وتناسق ألوان عالي الدقة.</p>
            </div>
            <!-- Service 2 -->
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-md transition">
                <div class="w-12 h-12 bg-amber-100 text-amber-600 rounded-xl flex items-center justify-center text-2xl mb-4">
                    <i class="fa-solid fa-cubes"></i>
                </div>
                <h4 class="font-bold text-xl mb-2 text-slate-900" id="s2-title">تركيب السيراميك</h4>
                <p class="text-slate-600 text-sm" id="s2-desc">تركيب سيراميك وبورسلان أرضيات وجدران حمامات ومطابخ مع ضبط الميول وتقفيل ممتازة.</p>
            </div>
            <!-- Service 3 -->
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-md transition">
                <div class="w-12 h-12 bg-amber-100 text-amber-600 rounded-xl flex items-center justify-center text-2xl mb-4">
                    <i class="fa-solid fa-faucet-drip"></i>
                </div>
                <h4 class="font-bold text-xl mb-2 text-slate-900" id="s3-title">الصحية والسباكة</h4>
                <p class="text-slate-600 text-sm" id="s3-desc">تمديد وصيانة خطوط المياه والصرف، تركيب أدوات صحية ومعالجة التسريبات.</p>
            </div>
            <!-- Service 4 -->
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-md transition">
                <div class="w-12 h-12 bg-amber-100 text-amber-600 rounded-xl flex items-center justify-center text-2xl mb-4">
                    <i class="fa-solid fa-bolt"></i>
                </div>
                <h4 class="font-bold text-xl mb-2 text-slate-900" id="s4-title">الكهرباء والتمديدات</h4>
                <p class="text-slate-600 text-sm" id="s4-desc">إصلاح الأعطال الكهربائية، تمديد نقاط جديدة، وتركيب الإنارة الحديثة والليدات.</p>
            </div>
        </div>
    </section>

    <!-- Public Feed / Custom Posts Section (معرض الأعمال والتحديثات) -->
    <section class="py-12 bg-slate-100 px-4">
        <div class="max-w-7xl mx-auto">
            <div class="flex justify-between items-center mb-8">
                <div>
                    <h3 class="text-2xl md:text-3xl font-bold text-slate-900" id="posts-title">أحدث أعمالنا والعروض</h3>
                    <p class="text-slate-500 text-sm" id="posts-subtitle">صور وفيديوهات من مواقع العمل الحقيقية مع التفاصيل والأسعار</p>
                </div>
            </div>

            <!-- Posts Container -->
            <div id="posts-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Posts will be generated dynamically by JavaScript -->
            </div>
        </div>
    </section>

    <!-- Floating WhatsApp Button -->
    <a href="https://wa.me/905317327802" target="_blank" class="floating-whatsapp bg-green-500 text-white w-14 h-14 rounded-full flex items-center justify-center text-3xl shadow-2xl hover:bg-green-600 transition hover:scale-110">
        <i class="fa-brands fa-whatsapp"></i>
    </a>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 py-8 text-center text-sm mt-auto">
        <p class="mb-2" id="footer-text">أبو نمر – خدمات صيانة وإكساء المنازل | بورصة</p>
        <p class="text-amber-400 font-bold" dir="ltr">+90 531 732 7802</p>
    </footer>

    <!-- Admin Modal / Dashboard (لوحة الإدارة الخاصة بك) -->
    <div id="admin-modal" class="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white w-full max-w-lg rounded-2xl shadow-2xl overflow-hidden">
            <div class="bg-slate-900 text-white p-4 flex justify-between items-center">
                <h4 class="font-bold text-lg"><i class="fa-solid fa-lock text-amber-400 ml-2"></i> لوحة التحكم بالنشر</h4>
                <button onclick="closeAdminModal()" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark text-xl"></i></button>
            </div>
            
            <!-- Auth Form -->
            <div id="auth-box" class="p-6">
                <p class="text-slate-600 text-sm mb-4">يرجى إدخال كلمة السر الخاصة بالمشرف للنشر:</p>
                <input type="password" id="admin-pass" placeholder="كلمة السر" class="w-full border border-slate-300 p-3 rounded-xl mb-4 focus:outline-amber-500">
                <button onclick="verifyPassword()" class="w-full bg-amber-500 hover:bg-amber-600 text-slate-900 font-bold py-3 rounded-xl">دخول</button>
            </div>

            <!-- Publish Form (Hides initially) -->
            <div id="publish-box" class="p-6 hidden max-h-[80vh] overflow-y-auto">
                <h5 class="font-bold text-slate-800 mb-3 border-b pb-2">إضافة منشور جديد</h5>
                
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">نوع الملف (صورة أو فيديو):</label>
                        <select id="post-type" class="w-full border p-2.5 rounded-lg text-sm">
                            <option value="image">صورة (Image)</option>
                            <option value="video">فيديو (Video)</option>
                        </select>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">رابط الصورة/الفيديو (URL):</label>
                        <input type="text" id="post-media-url" placeholder="ضع رابط الصورة أو الفيديو هنا" class="w-full border p-2.5 rounded-lg text-sm">
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">الملاحظة / الوصف (بالعربي):</label>
                        <textarea id="post-desc-ar" rows="2" placeholder="مثال: دهان شقة كاملة مع المعجونة في منطقة نيلوفر" class="w-full border p-2.5 rounded-lg text-sm"></textarea>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">الملاحظة / الوصف (بالتركي):</label>
                        <textarea id="post-desc-tr" rows="2" placeholder="Örnek: Nilüfer bölgesinde komple daire boya işi" class="w-full border p-2.5 rounded-lg text-sm"></textarea>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">السعر (اختياري):</label>
                        <input type="text" id="post-price" placeholder="مثال: 5000 TL أو حسب المعاينة" class="w-full border p-2.5 rounded-lg text-sm">
                    </div>

                    <button onclick="addNewPost()" class="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-3 rounded-xl transition">
                        <i class="fa-solid fa-plus ml-1"></i> نشر الآن
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- JavaScript Translations & Logic -->
    <script>
        let currentLang = 'ar';
        const defaultPassword = "123"; // كلمة السر الافتراضية للوحة التحكم (يمكنك تغييرها)

        // Translation Data
        const translations = {
            ar: {
                navTitle: "أبو نمر للإكساء والصيانة",
                navSubtitle: "بورصة | Bursa",
                langBtn: "Türkçe",
                adminBtn: "الإدارة",
                heroBadge: "📍 بورصة - جميع المناطق",
                heroHeading: "خدمات الدهان، السيراميك، الصحية، والكهرباء",
                heroDesc: "خبرة وعناية فائقة في تشطيب وصيانة المنازل والمحلات بأعلى جودة وأفضل الأسعار.",
                btnWa: "تواصل واتساب",
                btnCall: "اتصال مباشر",
                servicesTitle: "خدماتنا الرئيسية",
                s1Title: "الدهان والديكور",
                s1Desc: "دهان منازل داخلي احترافي، تجهيز معجونة، معالجة رطوبة وتناسق ألوان عالي الدقة.",
                s2Title: "تركيب السيراميك",
                s2Desc: "تركيب سيراميك وبورسلان أرضيات وجدران حمامات ومطابخ مع ضبط الميول وتقفيل ممتازة.",
                s3Title: "الصحية والسباكة",
                s3Desc: "تمديد وصيانة خطوط المياه والصرف، تركيب أدوات صحية ومعالجة التسريبات.",
                s4Title: "الكهرباء والتمديدات",
                s4Desc: "إصلاح الأعطال الكهربائية، تمديد نقاط جديدة، وتركيب الإنارة الحديثة والليدات.",
                postsTitle: "أحدث أعمالنا والعروض",
                postsSubtitle: "صور وفيديوهات من مواقع العمل الحقيقية مع التفاصيل والأسعار",
                footerText: "أبو نمر – خدمات صيانة وإكساء المنازل | بورصة",
                priceTag: "السعر:",
                noteTag: "ملاحظة:"
            },
            tr: {
                navTitle: "Ebu Nemr Dekorasyon & Tadilat",
                navSubtitle: "Bursa",
                langBtn: "العربية",
                adminBtn: "Yönetim",
                heroBadge: "📍 Bursa - Tüm Bölgeler",
                heroHeading: "Boya, Seramik, Tesisat ve Elektrik Hizmetleri",
                heroDesc: "Bursa'da ev ve iş yerleriniz için kaliteli, hızlı ve uygun fiyatlı tadilat ve dekorasyon çözümleri.",
                btnWa: "WhatsApp İletişim",
                btnCall: "Hemen Ara",
                servicesTitle: "Hizmetlerimiz",
                s1Title: "Boya & Dekorasyon",
                s1Desc: "Profesyonel iç mekan boya, macun çekimi, nem onarımı ve kaliteli işçilik.",
                s2Title: "Seramik & Fayans",
                s2Desc: "Banyo, mutfak ve zemin seramik döşeme, derz dolgu ve hassاس terazi ayarı.",
                s3Title: "Sıhhi Tesisat",
                s3Desc: "Su ve gider tesisat montajı, arıza tamiri ve vitrifiye montajı.",
                s4Title: "Elektrik Tesisatı",
                s4Desc: "Elektrik arıza tamiri, yeni hat çekimi, LED ve aydınlatma montajı.",
                postsTitle: "Son Çalışmalarımız ve İlanlar",
                postsSubtitle: "Gerçek iş sahalarından detaylar, resimler ve fiyatlar",
                footerText: "Ebu Nemr – Bursa Ev Tadilat & Dekorasyon Hizmetleri",
                priceTag: "Fiyat:",
                noteTag: "Not:"
            }
        };

        // Initial Posts Sample Data
        let samplePosts = [
            {
                id: 1,
                type: 'image',
                url: 'https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=600&auto=format&fit=crop&q=60',
                descAr: 'تشطيب وتحديد دهان صالون مع ديكور إضاءة ليد في منطقة أوسمان غازي.',
                descTr: 'Osmangazi bölgesinde LED aydınlatmalı salon boya ve dekorasyon uygulaması.',
                price: 'حسب المعاينة / Keşfe Göre'
            },
            {
                id: 2,
                type: 'image',
                url: 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=600&auto=format&fit=crop&q=60',
                descAr: 'تجديد سيراميك حمام كامل مع التمديدات الصحية واختبار التسريب.',
                descTr: 'Komple banyo seramik yenileme ve su tesisatı montajı.',
                price: 'اتصل للتفاصيل'
            }
        ];

        // Load Posts from LocalStorage if exists
        function getPosts() {
            const saved = localStorage.getItem('abunemer_posts');
            return saved ? JSON.parse(saved) : samplePosts;
        }

        function savePosts(posts) {
            localStorage.setItem('abunemer_posts', JSON.stringify(posts));
        }

        // Render Posts
        function renderPosts() {
            const grid = document.getElementById('posts-grid');
            const posts = getPosts();
            const t = translations[currentLang];
            grid.innerHTML = '';

            if(posts.length === 0) {
                grid.innerHTML = `<p class="text-slate-500 text-center col-span-full">لا يوجد منشورات حالياً</p>`;
                return;
            }

            posts.forEach(post => {
                const desc = currentLang === 'ar' ? post.descAr : post.descTr;
                const mediaHtml = post.type === 'video' 
                    ? `<video controls class="w-full h-56 object-cover rounded-t-2xl"><source src="${post.url}" type="video/mp4">متصفحك لا يدعم الفيديو</video>`
                    : `<img src="${post.url}" alt="Work" class="w-full h-56 object-cover rounded-t-2xl">`;

                grid.innerHTML += `
                    <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden flex flex-col">
                        ${mediaHtml}
                        <div class="p-5 flex flex-col flex-grow">
                            <p class="text-slate-700 text-sm mb-4 font-semibold">${desc}</p>
                            <div class="mt-auto pt-3 border-t border-slate-100 flex justify-between items-center text-xs">
                                <span class="bg-amber-100 text-amber-800 font-bold px-2.5 py-1 rounded-md">
                                    ${t.priceTag} ${post.price || '---'}
                                </span>
                                <a href="https://wa.me/905317327802?text=${encodeURIComponent('استفسار عن عمل: ' + desc)}" target="_blank" class="text-green-600 font-bold hover:underline flex items-center gap-1">
                                    <i class="fa-brands fa-whatsapp"></i> استفسر
                                </a>
                            </div>
                        </div>
                    </div>
                `;
            });
        }

        // Language Switcher
        function toggleLanguage() {
            currentLang = currentLang === 'ar' ? 'tr' : 'ar';
            document.html = document.documentElement.setAttribute('lang', currentLang);
            document.documentElement.setAttribute('dir', currentLang === 'ar' ? 'rtl' : 'ltr');

            const t = translations[currentLang];
            document.getElementById('nav-title').innerText = t.navTitle;
            document.getElementById('nav-subtitle').innerText = t.navSubtitle;
            document.getElementById('lang-btn-text').innerText = t.langBtn;
            document.getElementById('admin-btn-text').innerText = t.adminBtn;
            document.getElementById('hero-badge').innerText = t.heroBadge;
            document.getElementById('hero-heading').innerText = t.heroHeading;
            document.getElementById('hero-desc').innerText = t.heroDesc;
            document.getElementById('btn-wa').innerText = t.btnWa;
            document.getElementById('btn-call').innerText = t.btnCall;
            document.getElementById('services-title').innerText = t.servicesTitle;
            document.getElementById('s1-title').innerText = t.s1Title;
            document.getElementById('s1-desc').innerText = t.s1Desc;
            document.getElementById('s2-title').innerText = t.s2Title;
            document.getElementById('s2-desc').innerText = t.s2Desc;
            document.getElementById('s3-title').innerText = t.s3Title;
            document.getElementById('s3-desc').innerText = t.s3Desc;
            document.getElementById('s4-title').innerText = t.s4Title;
            document.getElementById('s4-desc').innerText = t.s4Desc;
            document.getElementById('posts-title').innerText = t.postsTitle;
            document.getElementById('posts-subtitle').innerText = t.postsSubtitle;
            document.getElementById('footer-text').innerText = t.footerText;

            renderPosts();
        }

        // Admin Modal Logic
        function openAdminModal() {
            document.getElementById('admin-modal').classList.remove('hidden');
        }
        function closeAdminModal() {
            document.getElementById('admin-modal').classList.add('hidden');
        }

        function verifyPassword() {
            const pass = document.getElementById('admin-pass').value;
            if(pass === defaultPassword) {
                document.getElementById('auth-box').classList.add('hidden');
                document.getElementById('publish-box').classList.remove('hidden');
            } else {
                alert('كلمة السر غير صحيحة!');
            }
        }

        function addNewPost() {
            const type = document.getElementById('post-type').value;
            const url = document.getElementById('post-media-url').value;
            const descAr = document.getElementById('post-desc-ar').value;
            const descTr = document.getElementById('post-desc-tr').value;
            const price = document.getElementById('post-price').value;

            if(!url || !descAr) {
                alert('يرجى وضع رابط الصورة/الفيديو ووصف بالعربي على الأقل!');
                return;
            }

            const posts = getPosts();
            const newPost = {
                id: Date.now(),
                type: type,
                url: url,
                descAr: descAr,
                descTr: descTr || descAr,
                price: price
            };

            posts.unshift(newPost);
            savePosts(posts);
            renderPosts();
            closeAdminModal();

            // Reset inputs
            document.getElementById('post-media-url').value = '';
            document.getElementById('post-desc-ar').value = '';
            document.getElementById('post-desc-tr').value = '';
            document.getElementById('post-price').value = '';
            alert('تم نشر العمل بنجاح!');
        }

        // Initialize Page
        renderPosts();
    </script>
</body>
</html>
