// Unregister any active service workers from previous projects on this port
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.getRegistrations().then(function(registrations) {
        for(let registration of registrations) {
            registration.unregister();
            console.log('Unregistered active service worker:', registration);
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const burgerMenu = document.querySelector('.burger-menu');
    const navMenu = document.querySelector('.nav-menu');

    if (burgerMenu && navMenu) {
        burgerMenu.addEventListener('click', () => {
            navMenu.classList.toggle('open');
            // Animate burger lines
            const lines = burgerMenu.querySelectorAll('.burger-line');
            lines[0].style.transform = navMenu.classList.contains('open') ? 'rotate(45deg) translate(6px, 6px)' : 'none';
            lines[1].style.opacity = navMenu.classList.contains('open') ? '0' : '1';
            lines[2].style.transform = navMenu.classList.contains('open') ? 'rotate(-45deg) translate(5deg, -5px)' : 'none';
            // Simple offset fix
            if (navMenu.classList.contains('open')) {
                lines[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
            }
        });
    }

    // 2. Client-side search filters
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            const searchableCards = document.querySelectorAll('.searchable-card');
            
            searchableCards.forEach(card => {
                const title = card.querySelector('.searchable-title').textContent.toLowerCase();
                const description = card.querySelector('.searchable-desc') ? card.querySelector('.searchable-desc').textContent.toLowerCase() : '';
                if (title.includes(query) || description.includes(query)) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }

    // 3. Category Filter Dropdown
    const filterSelect = document.getElementById('filter-select');
    if (filterSelect) {
        filterSelect.addEventListener('change', (e) => {
            const selectedCategory = e.target.value;
            const filterableCards = document.querySelectorAll('.searchable-card');
            
            filterableCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');
                if (selectedCategory === 'ALL' || cardCategory === selectedCategory) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }

    // 4. Modal Triggers
    const modalTriggers = document.querySelectorAll('[data-modal-target]');
    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = trigger.getAttribute('data-modal-target');
            const modal = document.getElementById(targetId);
            if (modal) {
                modal.classList.add('open');
            }
        });
    });

    const modalCloses = document.querySelectorAll('.modal-close, [data-modal-close]');
    modalCloses.forEach(closeBtn => {
        closeBtn.addEventListener('click', () => {
            const openModal = document.querySelector('.modal-overlay.open');
            if (openModal) {
                openModal.classList.remove('open');
            }
        });
    });

    // Close modal on clicking overlay background
    const modals = document.querySelectorAll('.modal-overlay');
    modals.forEach(modal => {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('open');
            }
        });
    });

    // 5. Client-Side Multilingual Dictionary
    const translations = {
        'en': {
            'home': 'Home',
            'notices': 'Notices',
            'schemes': 'Schemes',
            'complaints': 'Complaints',
            'agriculture': 'Agriculture',
            'health': 'Health',
            'education': 'Education',
            'marketplace': 'Marketplace',
            'documents': 'Documents',
            'dashboard': 'Dashboard',
            'login': 'Login',
            'logout': 'Logout',
            'register': 'Register',
            'sarpanch_name': 'Sarpanch Ramesh Patil',
            'welcome_msg': 'Empowering Rural Communities through Digital Connectivity',
            'subtitle_msg': 'A modern platform connecting citizens with notices, government schemes, agricultural advice, grievance handling, and local trade.',
            'view_all_notices': 'View All Notices',
            'population': 'Population',
            'schools': 'Schools',
            'hospitals': 'Hospitals',
            'water_connections': 'Water Connections',
            'quick_links': 'Quick Links',
            'submit_complaint': 'Register Complaint',
            'explore_marketplace': 'Local Marketplace',
            'view_schemes': 'Government Schemes',
            'weather_title': 'Farming & Weather Alert',
            'weather_temp': '28°C - Scattered Rain',
            'weather_desc': 'Clear field drainage channels. Good time to apply organic fertilizers.'
        },
        'hi': {
            'home': 'गृह',
            'notices': 'सूचनाएं',
            'schemes': 'योजनाएं',
            'complaints': 'शिकायतें',
            'agriculture': 'कृषि मार्गदर्शन',
            'health': 'स्वास्थ्य',
            'education': 'शिक्षा',
            'marketplace': 'बाज़ार',
            'documents': 'दस्तावेज़',
            'dashboard': 'डैशबोर्ड',
            'login': 'लॉगिन',
            'logout': 'लॉगआउट',
            'register': 'पंजीकरण',
            'sarpanch_name': 'सरपंच रमेश पाटिल',
            'welcome_msg': 'डिजिटल कनेक्टिविटी के माध्यम से ग्रामीण समुदायों का सशक्तिकरण',
            'subtitle_msg': 'एक आधुनिक मंच जो नागरिकों को सूचनाओं, सरकारी योजनाओं, कृषि सलाह, शिकायत निवारण और स्थानीय व्यापार से जोड़ता है।',
            'view_all_notices': 'सभी सूचनाएं देखें',
            'population': 'जनसंख्या',
            'schools': 'स्कूलों की संख्या',
            'hospitals': 'अस्पताल',
            'water_connections': 'नल कनेक्शन',
            'quick_links': 'त्वरित संपर्क',
            'submit_complaint': 'शिकायत दर्ज करें',
            'explore_marketplace': 'स्थानीय बाज़ार',
            'view_schemes': 'सरकारी योजनाएं',
            'weather_title': 'कृषि और मौसम अलर्ट',
            'weather_temp': '28°C - छिटपुट बारिश',
            'weather_desc': 'खेतों में जल निकासी का ध्यान रखें। जैविक खाद डालने का सही समय।'
        },
        'mr': {
            'home': 'मुख्यपृष्ठ',
            'notices': 'सूचना फलक',
            'schemes': 'शासकीय योजना',
            'complaints': 'तक्रार नोंदणी',
            'agriculture': 'कृषि सल्ला',
            'health': 'आरोग्य सेवा',
            'education': 'शिक्षण',
            'marketplace': 'स्थानिक बाजार',
            'documents': 'महत्त्वाची कागदपत्रे',
            'dashboard': 'डॅशबोर्ड',
            'login': 'लॉगिन',
            'logout': 'लॉगआउट',
            'register': 'नोंदणी करा',
            'sarpanch_name': 'सरपंच रमेश पाटील',
            'welcome_msg': 'डिजिटल कनेक्टिव्हिटीद्वारे ग्रामीण भागांचे सक्षमीकरण',
            'subtitle_msg': 'नागरिकांना शासकीय योजना, सूचना, तक्रार निवारण, शेती मार्गदर्शन आणि स्थानिक बाजारपेठेशी जोडणारे डिजिटल पोर्टल.',
            'view_all_notices': 'सर्व सूचना पहा',
            'population': 'एकूण लोकसंख्या',
            'schools': 'शाळांची संख्या',
            'hospitals': 'रुग्णालये',
            'water_connections': 'नळ जोडण्या',
            'quick_links': 'त्वरित लिंक्स',
            'submit_complaint': 'तक्रार दाखल करा',
            'explore_marketplace': 'स्थानिक बाजारपेठ',
            'view_schemes': 'शासकीय योजना पहा',
            'weather_title': 'हवामान आणि शेती सल्ला',
            'weather_temp': '२८°C - हलका पाऊस',
            'weather_desc': 'शेतातील पाण्याचा निचरा करा. सेंद्रिय खते टाकण्यासाठी योग्य वेळ.'
        }
    };

    const languageSelector = document.getElementById('language-selector');
    
    function applyTranslations(lang) {
        const translateElements = document.querySelectorAll('[data-translate]');
        translateElements.forEach(element => {
            const key = element.getAttribute('data-translate');
            if (translations[lang] && translations[lang][key]) {
                if (element.tagName === 'INPUT' && (element.type === 'text' || element.type === 'search')) {
                    element.placeholder = translations[lang][key];
                } else {
                    element.textContent = translations[lang][key];
                }
            }
        });
        localStorage.setItem('selectedLanguage', lang);
    }

    if (languageSelector) {
        languageSelector.addEventListener('change', (e) => {
            applyTranslations(e.target.value);
        });

        // Initialize language from local storage
        const savedLang = localStorage.getItem('selectedLanguage') || 'en';
        languageSelector.value = savedLang;
        applyTranslations(savedLang);
    }
});
