// Main JavaScript - Plomero Mazatlán Pro
// Loaded with defer for optimal performance
// Last updated: 2025-11-21

// Nav scroll – fondo solido al hacer scroll
(function() {
    var nav = document.querySelector('.nav');
    if (!nav) return;

    var ticking = false;

    function updateNav() {
        if (window.scrollY > 50) {
            nav.classList.add('nav-scrolled');
        } else {
            nav.classList.remove('nav-scrolled');
        }
        ticking = false;
    }

    window.addEventListener('scroll', function() {
        if (!ticking) {
            requestAnimationFrame(updateNav);
            ticking = true;
        }
    }, { passive: true });

    updateNav();
})();

// Mobile menu toggle with scroll position preservation
(function() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.nav-menu');
    if (!mobileMenuBtn || !navMenu) return;

    let scrollY = 0;

    function openMenu() {
        scrollY = window.scrollY;
        document.body.style.top = '-' + scrollY + 'px';
        document.body.classList.add('menu-open');
        navMenu.classList.add('active');
        mobileMenuBtn.classList.add('active');
        mobileMenuBtn.setAttribute('aria-expanded', 'true');
        mobileMenuBtn.setAttribute('aria-label', 'Cerrar menú de navegación');
    }

    function closeMenu() {
        const savedScrollY = scrollY;
        document.body.classList.remove('menu-open');
        document.body.style.top = '';
        navMenu.classList.remove('active');
        mobileMenuBtn.classList.remove('active');
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
        mobileMenuBtn.setAttribute('aria-label', 'Abrir menú de navegación');
        window.scrollTo(0, savedScrollY);
    }

    mobileMenuBtn.addEventListener('click', () => {
        if (document.body.classList.contains('menu-open')) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    // Close mobile menu when clicking a link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', closeMenu);
    });
})();

// Urgency indicator - mensaje dinamico segun hora del dia
(function() {
    var el = document.getElementById('urgency-text');
    if (!el) return;

    var h = new Date().getHours();

    if (h >= 7 && h < 22) {
        el.textContent = 'Disponible ahora \u2013 respuesta en ~5 min';
    } else {
        el.textContent = 'Servicio nocturno activo';
    }
})();

// Real-time form validation
(function() {
    const form = document.getElementById('contact-form');
    if (!form) return; // Exit if form doesn't exist

    const nombreField = document.getElementById('nombre');
    const telefonoField = document.getElementById('telefono');
    const emailField = document.getElementById('email');
    const mensajeField = document.getElementById('mensaje');
    const submitBtn = form.querySelector('button[type="submit"]');

    // Validation functions
    const validators = {
        nombre: (value) => value.trim().length >= 2,
        telefono: (value) => /^[0-9]{10}$/.test(value.replace(/\s/g, '')),
        email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
        mensaje: (value) => value.trim().length >= 10
    };

    // Validate single field
    function validateField(field, validatorKey) {
        const value = field.value;
        const fieldWrapper = field.closest('.form-field');
        const isValid = validators[validatorKey](value);

        if (value.length === 0) {
            // Empty: neutral state
            fieldWrapper.classList.remove('valid', 'invalid');
        } else if (isValid) {
            // Valid: green checkmark
            fieldWrapper.classList.remove('invalid');
            fieldWrapper.classList.add('valid');
        } else {
            // Invalid: red X
            fieldWrapper.classList.remove('valid');
            fieldWrapper.classList.add('invalid');
        }

        updateSubmitButton();
        return isValid;
    }

    // Check if form is completely valid
    function isFormValid() {
        return validators.nombre(nombreField.value) &&
               validators.telefono(telefonoField.value) &&
               validators.email(emailField.value) &&
               validators.mensaje(mensajeField.value);
    }

    // Enable/disable submit button based on form validity
    function updateSubmitButton() {
        if (isFormValid()) {
            submitBtn.disabled = false;
            submitBtn.style.opacity = '1';
            submitBtn.style.cursor = 'pointer';
        } else {
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.6';
            submitBtn.style.cursor = 'not-allowed';
        }
    }

    // Add real-time validation listeners
    nombreField.addEventListener('input', () => validateField(nombreField, 'nombre'));
    nombreField.addEventListener('blur', () => validateField(nombreField, 'nombre'));

    telefonoField.addEventListener('input', () => {
        // Only allow numbers
        telefonoField.value = telefonoField.value.replace(/\D/g, '');
        validateField(telefonoField, 'telefono');
    });
    telefonoField.addEventListener('blur', () => validateField(telefonoField, 'telefono'));

    emailField.addEventListener('input', () => validateField(emailField, 'email'));
    emailField.addEventListener('blur', () => validateField(emailField, 'email'));

    mensajeField.addEventListener('input', () => validateField(mensajeField, 'mensaje'));
    mensajeField.addEventListener('blur', () => validateField(mensajeField, 'mensaje'));

    // Initial state: button disabled
    updateSubmitButton();
})();

// Multi-layer lead capture: Netlify Forms + localStorage + GA4 + WhatsApp
(function() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        const formData = new FormData(this);
        const nombre = formData.get('nombre');
        const telefono = formData.get('telefono');
        const email = formData.get('email');
        const mensaje = formData.get('mensaje');

        const leadData = {
            timestamp: new Date().toISOString(),
            nombre: nombre,
            telefono: telefono,
            email: email,
            mensaje: mensaje,
            source: 'homepage_form',
            url: window.location.href
        };

        // 1. Track lead in GA4 via GTM dataLayer (immediate)
        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'generate_lead',
                'form_name': 'contact_form_homepage',
                'method': 'netlify_forms',
                'value': 1,
                'currency': 'MXN'
            });
        }

        // 2. Store in localStorage as backup (immediate)
        try {
            const leads = JSON.parse(localStorage.getItem('plomero_leads') || '[]');
            leads.push(leadData);
            localStorage.setItem('plomero_leads', JSON.stringify(leads));
        } catch (e) {
            // console.error('Error storing lead in localStorage:', e);
        }

        // 3. Submit to Netlify Forms (primary backend)
        try {
            const response = await fetch('/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams(formData).toString()
            });

            if (response.ok) {
                // Success: show thank you and open WhatsApp
                const whatsappMessage = `Hola! Solicito cotización de servicios de plomería:\n\n` +
                                      `Nombre: ${nombre}\n` +
                                      `Teléfono: ${telefono}\n` +
                                      `Email: ${email}\n` +
                                      `Mensaje: ${mensaje}`;
                const whatsappURL = `https://wa.me/526691325300?text=${encodeURIComponent(whatsappMessage)}`;

                // Open WhatsApp in new tab
                window.open(whatsappURL, '_blank');

                // Redirect to thank you page
                window.location.href = '/gracias';
            } else {
                throw new Error('Netlify form submission failed');
            }
        } catch (error) {
            // console.error('Error submitting to Netlify:', error);

            // Fallback: open WhatsApp directly
            alert('Formulario enviado. Te redirigiremos a WhatsApp.');
            const whatsappMessage = `Hola! Solicito cotización de servicios de plomería:\n\n` +
                                  `Nombre: ${nombre}\n` +
                                  `Teléfono: ${telefono}\n` +
                                  `Email: ${email}\n` +
                                  `Mensaje: ${mensaje}`;
            const whatsappURL = `https://wa.me/526691325300?text=${encodeURIComponent(whatsappMessage)}`;
            window.location.href = whatsappURL;
        }
    });
})();

// CTA fijo con tracking (progressive enhancement: funciona sin JS)
(function(){
  // Progressive Enhancement: hrefs ya funcionan, JS solo agrega tracking
  var PATH = location.pathname;
  var wa = document.getElementById("cta-whatsapp");
  var tl = document.getElementById("cta-llamar");

  // Tracking de clics en GA4 via dataLayer
  window.dataLayer = window.dataLayer || [];
  function pushEvt(type, label) {
    try {
      window.dataLayer.push({
        event: "cta_click",
        cta_type: type,
        cta_label: label,
        page: PATH
      });
    } catch(e) {}
  }

  if (wa) {
    wa.addEventListener("click", function() {
      pushEvt("whatsapp", "cta_floating");
    });
  }
  if (tl) {
    tl.addEventListener("click", function() {
      pushEvt("llamar", "cta_floating");
    });
  }
})();

// Mini footer nav tracking
(function(){
  window.dataLayer=window.dataLayer||[];
  document.querySelectorAll(".site-mini-nav a").forEach(function(a){
    if(a.dataset.navBound==="1") return; a.dataset.navBound="1";
    a.addEventListener("click", function(){
      try{ dataLayer.push({event:"nav_click", nav_label:a.textContent.trim(), nav_href:a.getAttribute("href"), page:location.pathname}); }catch(e){}
    });
  });
})();

// Tracking de tarjetas SEO - diferido con requestIdleCallback
(typeof requestIdleCallback === 'function' ? requestIdleCallback : setTimeout)(function() {
  // Tracking de clics en tarjetas "Más opciones de plomería"
  document.querySelectorAll('.seo-card[data-event="click_seo_card"]').forEach(function(card) {
    card.addEventListener('click', function(e) {
      var cardName = this.getAttribute('data-card-name');
      var cardPosition = this.getAttribute('data-card-position');
      var cardHref = this.getAttribute('href');

      try {
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
          'event': 'click_seo_card',
          'card_name': cardName,
          'card_position': cardPosition,
          'card_url': cardHref,
          'page_location': window.location.pathname
        });
      } catch(e) {
        // console.error('Error tracking seo card:', e);
      }
    });
  });

  // Tracking de scroll depth para medir engagement - optimizado con rAF throttle
  var scrollDepths = [25, 50, 75, 90];
  var scrollTracked = {};
  var scrollTicking = false;
  var cachedScrollableHeight = document.documentElement.scrollHeight - window.innerHeight;

  // Actualizar cache solo en resize
  window.addEventListener('resize', function() {
    cachedScrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
  }, { passive: true });

  window.addEventListener('scroll', function() {
    if (scrollTicking) return;
    scrollTicking = true;
    requestAnimationFrame(function() {
      var scrollPercent = Math.round((window.scrollY / cachedScrollableHeight) * 100);
      for (var i = 0; i < scrollDepths.length; i++) {
        var depth = scrollDepths[i];
        if (scrollPercent >= depth && !scrollTracked[depth]) {
          scrollTracked[depth] = true;
          try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
              'event': 'scroll_depth',
              'scroll_percentage': depth,
              'page_location': window.location.pathname
            });
          } catch(e) {}
        }
      }
      scrollTicking = false;
    });
  }, { passive: true });
});

// Exit-Intent Popup - versión simplificada (móvil: back button, desktop: mouseleave)
(typeof requestIdleCallback === 'function' ? requestIdleCallback : setTimeout)(function() {
    var popup = document.getElementById('exit-intent-popup');
    if (!popup) return;

    var closeBtn = document.querySelector('.exit-popup-close');
    var whatsappBtn = document.getElementById('exit-popup-whatsapp');
    var phoneBtn = document.getElementById('exit-popup-phone');
    var popupShown = false;
    var SESSION_KEY = 'exitPopupShown';

    // Ya se mostró en esta sesión? Salir
    if (sessionStorage.getItem(SESSION_KEY)) return;

    function isMobile() {
        return window.innerWidth <= 768 || 'ontouchstart' in window;
    }

    function showPopup() {
        if (popupShown) return;
        popupShown = true;
        sessionStorage.setItem(SESSION_KEY, 'true');
        popup.style.display = 'flex';
        document.body.style.overflow = 'hidden';

        // Track popup shown event
        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'exit_intent_shown',
                'page_location': window.location.pathname,
                'trigger': isMobile() ? 'mobile_back' : 'desktop_mouseleave'
            });
        } catch(e) {}
    }

    function hidePopup() {
        popup.style.display = 'none';
        document.body.style.overflow = '';

        // Track popup close event
        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'exit_intent_closed',
                'page_location': window.location.pathname
            });
        } catch(e) {}
    }

    // DESKTOP: Mouse leave detection
    if (!isMobile()) {
        document.addEventListener('mouseleave', function(e) {
            if (e.clientY < 10) showPopup();
        });
    }

    // MOBILE: Detectar botón back
    if (isMobile()) {
        history.pushState(null, '', location.href);
        window.addEventListener('popstate', function() {
            if (!popupShown) {
                showPopup();
                history.pushState(null, '', location.href);
            }
        });
    }

    // Close popup on X button click
    if (closeBtn) {
        closeBtn.addEventListener('click', function(e) {
            e.preventDefault();
            hidePopup();
        });
    }

    // Close popup on overlay click
    popup.addEventListener('click', function(e) {
        if (e.target === popup) {
            hidePopup();
        }
    });

    // Close popup on ESC key
    document.addEventListener('keydown', function(e) {
        if (popup.style.display === 'flex' && e.key === 'Escape') {
            hidePopup();
        }
    });

    // Track WhatsApp CTA click
    if (whatsappBtn) {
        whatsappBtn.addEventListener('click', function() {
            try {
                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'exit_intent_whatsapp_click',
                    'page_location': window.location.pathname
                });
            } catch(e) {}
        });
    }

    // Track Phone CTA click
    if (phoneBtn) {
        phoneBtn.addEventListener('click', function() {
            try {
                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'exit_intent_phone_click',
                    'page_location': window.location.pathname
                });
            } catch(e) {}
        });
    }
}, 2500);

// Hide floating buttons in critical sections - optimizado sin reflows
(typeof requestIdleCallback === 'function' ? requestIdleCallback : setTimeout)(function() {
    var floatingBtns = document.querySelectorAll('.floating-btn');
    if (!floatingBtns.length) return;

    var criticalSections = document.querySelectorAll('#contacto, .footer, .contact-form, .map-embed');
    if (!criticalSections.length) return;

    // Flags para evitar lecturas de classList en cada callback
    var isHidden = false;
    var menuOpen = false;

    // Observar cambios de clase en body una sola vez
    var bodyObserver = new MutationObserver(function(mutations) {
        menuOpen = document.body.classList.contains('menu-open');
    });
    bodyObserver.observe(document.body, { attributes: true, attributeFilter: ['class'] });

    function updateVisibility(shouldHide) {
        if (shouldHide === isHidden) return; // No cambio, evitar reflow
        isHidden = shouldHide;
        var opacity = shouldHide ? '0' : '1';
        var pointer = shouldHide ? 'none' : 'auto';
        for (var i = 0; i < floatingBtns.length; i++) {
            floatingBtns[i].style.cssText = 'opacity:' + opacity + ';pointer-events:' + pointer;
        }
    }

    var observer = new IntersectionObserver(function(entries) {
        var anyVisible = false;
        for (var i = 0; i < entries.length; i++) {
            if (entries[i].isIntersecting && entries[i].intersectionRatio > 0.3) {
                anyVisible = true;
                break;
            }
        }
        if (!menuOpen) updateVisibility(anyVisible);
    }, {
        threshold: [0, 0.3, 0.5],
        rootMargin: '0px 0px -100px 0px'
    });

    criticalSections.forEach(function(section) {
        observer.observe(section);
    });
});

// Service Worker Registration
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                // console.log('SW registered:', registration.scope);
            })
            .catch(err => {
                // console.log('SW registration failed:', err);
            });
    });
}
