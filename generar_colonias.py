#!/usr/bin/env python3
"""
Generador de páginas de colonias para Plomero Mazatlán Pro
Generador de páginas de colonias para Plomero Mazatlán Pro
"""
import json
import os
import re
from pathlib import Path

# Colonias principales de Mazatlán con descripciones
COLONIAS_PRINCIPALES = {
    "Centro": {
        "titulo": "Plomero Especializado en Centro de Mazatlán",
        "subtitulo": "Expertos en sistemas antiguos, drenajes de hierro fundido, tuberías de galvanizado. Más de 20 años trabajando en construcciones históricas del Centro. Técnicas que preservan la arquitectura original.",
        "experiencia": "Sistemas Antiguos del Centro",
        "beneficios": [
            ("🏛️", "Construcciones Históricas", "40-70 años de antigüedad"),
            ("🔧", "Drenajes de Hierro Fundido", "Reparación especializada"),
            ("🛠️", "Tuberías de Galvanizado", "Reemplazo y mantenimiento"),
            ("🏠", "Técnicas Especiales", "Preservamos pisos originales"),
            ("✅", "Garantía 6 Meses", "En todas nuestras reparaciones"),
        ],
        "servicios": [
            ("Reparación de Drenajes Antiguos", "Hierro fundido, concreto, sistemas de 40+ años. Técnicas especializadas."),
            ("Reemplazo de Tuberías", "Galvanizado a cobre/PEX. Mínima invasión, máxima durabilidad."),
            ("Destape Profundo", "Obstrucciones severas en drenajes antiguos. Equipos especiales."),
            ("Detección de Fugas Ocultas", "En muros antiguos sin romper acabados originales."),
            ("Restauración de Baños Antiguos", "Preservamos azulejos originales, instalamos grifería moderna."),
            ("Emergencias en Centro", "Atención 24/7 para fugas e inundaciones en construcciones antiguas."),
        ],
        "conocimiento": [
            "Sistemas Antiguos: Drenajes de hierro fundido, tuberías de galvanizado de 40-70 años.",
            "Construcciones Históricas: Respeto por arquitectura original, pisos de mosaico, azulejos antiguos.",
            "Técnicas Especiales: Reparación sin destruir, detección precisa, mínima invasión.",
            "Materiales Compatibles: Usamos materiales que respetan la antigüedad del inmueble.",
            "Experiencia Comprobada: 20+ años trabajando en el Centro de Mazatlán.",
        ],
        "testimonios": [
            ("Repararon el drenaje de mi casa de 60 años sin romper los pisos de mosaico original. Trabajo impecable.", "Don José, Centro"),
            ("Conocen perfectamente los sistemas antiguos. Cambiaron las tuberías de galvanizado sin destrozar la casa.", "María Elena, Centro"),
        ]
    },
    "Zona Dorada": {
        "titulo": "Plomero en Zona Dorada, Mazatlán",
        "subtitulo": "Servicio especializado para hoteles, condominios y residencias de playa. Expertos en sistemas de alta presión, bombas y problemas por salitre. Atención 24/7 para el sector turístico.",
        "experiencia": "Zona Turística y Hotelera",
        "beneficios": [
            ("🏨", "Hoteles y Condominios", "Experiencia en grandes instalaciones"),
            ("🌊", "Problemas por Salitre", "Corrosión y mantenimiento"),
            ("💨", "Alta Presión", "Bombas y sistemas presurizados"),
            ("🏖️", "Zona de Playa", "Atención rápida al turismo"),
            ("✅", "Garantía 6 Meses", "En todas nuestras reparaciones"),
        ],
        "servicios": [
            ("Plomería para Hoteles", "Mantenimiento preventivo y correctivo para el sector hotelero."),
            ("Reparación de Bombas", "Instalación y reparación de sistemas de bombeo y presurización."),
            ("Protección contra Salitre", "Tuberías y conexiones resistentes a la corrosión marina."),
            ("Destape de Drenajes", "Servicio rápido para no afectar huéspedes y residentes."),
            ("Fugas en Condominios", "Detección y reparación con mínima molestia a vecinos."),
            ("Emergencias 24/7", "Atención inmediata para no afectar la operación turística."),
        ],
        "conocimiento": [
            "Sector Turístico: Entendemos la urgencia de resolver problemas sin afectar huéspedes.",
            "Condominios de Playa: Experiencia en edificios con múltiples unidades y sistemas centrales.",
            "Corrosión Marina: Conocemos los efectos del salitre y usamos materiales resistentes.",
            "Sistemas de Bombeo: Expertos en bombas de alta presión para edificios altos.",
            "Disponibilidad Total: Servicio 24/7 porque el turismo no descansa.",
        ],
        "testimonios": [
            ("Resolvieron una fuga en mi condominio sin molestar a los vecinos. Muy profesionales.", "Carlos, Zona Dorada"),
            ("Atienden rápido y entienden que en un hotel no podemos tener problemas de agua.", "Gerente de Hotel, Zona Dorada"),
        ]
    },
    "Marina Mazatlán": {
        "titulo": "Plomero en Marina Mazatlán",
        "subtitulo": "Servicio premium para residencias de lujo y condominios frente al mar. Expertos en sistemas modernos de alta gama, filtración de agua y problemas de humedad costera.",
        "experiencia": "Residencias de Lujo",
        "beneficios": [
            ("🛥️", "Zona Exclusiva", "Servicio premium garantizado"),
            ("🏢", "Condominios de Lujo", "Experiencia en acabados finos"),
            ("💧", "Filtración de Agua", "Sistemas de purificación"),
            ("🌅", "Frente al Mar", "Protección contra humedad"),
            ("✅", "Garantía 6 Meses", "En todas nuestras reparaciones"),
        ],
        "servicios": [
            ("Plomería de Alta Gama", "Instalación de grifería y accesorios de lujo importados."),
            ("Sistemas de Filtración", "Instalación y mantenimiento de purificadores de agua."),
            ("Protección contra Humedad", "Impermeabilización y drenajes para zonas costeras."),
            ("Reparación Discreta", "Trabajamos cuidando acabados finos y privacidad."),
            ("Mantenimiento Preventivo", "Programas de mantenimiento para residencias de lujo."),
            ("Emergencias VIP", "Atención prioritaria 24/7 con respuesta inmediata."),
        ],
        "conocimiento": [
            "Acabados de Lujo: Trabajamos con cuidado extremo en mármol, granito y acabados finos.",
            "Marcas Premium: Experiencia con Kohler, Grohe, Hansgrohe y marcas de alta gama.",
            "Discreción: Respetamos la privacidad de nuestros clientes en todo momento.",
            "Ambiente Costero: Conocemos los retos de la humedad y el salitre en la zona.",
            "Servicio Premium: Atención personalizada acorde a la exclusividad de la zona.",
        ],
        "testimonios": [
            ("Instalaron mi sistema de filtración sin ningún problema. Muy profesionales y discretos.", "Residente, Marina Mazatlán"),
            ("Excelente servicio, respetan los acabados y dejan todo impecable.", "Propietario, Marina Mazatlán"),
        ]
    },
}

def cargar_colonias_del_json():
    """Carga las colonias desde el archivo JSON oficial de Mazatlán"""
    json_path = Path("/Users/hectorpc/Documents/Hector Palazuelos/Google My Business/Plomero Mazatlan Pro/mazatlan_colonias.json")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extraer nombres únicos de colonias
    colonias = set()
    for c in data['colonias']:
        nombre = c['nombre']
        # Normalizar: convertir mayúsculas a título
        if nombre.isupper():
            nombre = nombre.title()
        colonias.add(nombre)

    return sorted(list(colonias))

def slugify(text):
    """Convertir texto a slug para URL"""
    text = text.lower()
    text = re.sub(r'[áàäâ]', 'a', text)
    text = re.sub(r'[éèëê]', 'e', text)
    text = re.sub(r'[íìïî]', 'i', text)
    text = re.sub(r'[óòöô]', 'o', text)
    text = re.sub(r'[úùüû]', 'u', text)
    text = re.sub(r'[ñ]', 'n', text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

def generar_datos_genericos(nombre):
    """Genera datos para colonias sin información específica"""
    return {
        "titulo": f"Plomero en {nombre}, Mazatlán",
        "subtitulo": f"Servicio profesional de plomería en {nombre}. Reparación de fugas, destape de drenajes, instalación de boilers y tinacos. Llegamos en 30-60 minutos. Garantía en todos los trabajos.",
        "experiencia": f"Colonia {nombre}",
        "beneficios": [
            ("🚀", "Llegada Rápida", "30-60 minutos en tu domicilio"),
            ("🔧", "Servicio Completo", "Fugas, destapes, instalaciones"),
            ("💰", "Precios Justos", "Cotización gratis sin compromiso"),
            ("🕐", "24/7 Disponible", "Emergencias día y noche"),
            ("✅", "Garantía 6 Meses", "En todas nuestras reparaciones"),
        ],
        "servicios": [
            ("Reparación de Fugas", "Detectamos y reparamos fugas de agua en tuberías, llaves y conexiones."),
            ("Destape de Drenajes", "Destapamos WC, lavabos, regaderas y drenajes principales."),
            ("Instalación de Boiler", "Instalamos y reparamos calentadores de agua de todas las marcas."),
            ("Instalación de Tinaco", "Colocación profesional de tinacos y cisternas."),
            ("Reparación de WC", "Arreglamos fugas, cambio de piezas y problemas de descarga."),
            ("Emergencias 24/7", "Atención inmediata para urgencias de plomería."),
        ],
        "conocimiento": [
            f"Conocemos {nombre}: Sabemos las particularidades de las instalaciones en tu zona.",
            "Respuesta Rápida: Llegamos en 30-60 minutos a cualquier punto de la colonia.",
            "Precios Transparentes: Cotizamos antes de iniciar, sin sorpresas ni cargos ocultos.",
            "Garantía Real: 6 meses de garantía en mano de obra y materiales.",
            "Experiencia: Más de 15 años atendiendo a familias de Mazatlán.",
        ],
        "testimonios": [
            (f"Llegaron rápido y resolvieron la fuga en menos de una hora. Muy recomendados.", f"Cliente satisfecho, {nombre}"),
            (f"Precios justos y trabajo de calidad. Los volvería a llamar sin duda.", f"Vecino de {nombre}"),
        ]
    }

def generar_pagina(nombre, datos):
    """Genera el HTML para una página de colonia - estructura para Mazatlán"""
    slug = slugify(nombre)

    # Generar beneficios HTML
    beneficios_html = ""
    for icon, titulo, desc in datos["beneficios"]:
        beneficios_html += f'<div class="benefit"><div class="benefit-icon">{icon}</div><h3>{titulo}</h3><p>{desc}</p></div>'

    # Generar servicios HTML
    servicios_html = ""
    for titulo, desc in datos["servicios"]:
        servicios_html += f'<div class="card"><h3>{titulo}</h3><p>{desc}</p></div>'

    # Generar conocimiento HTML
    conocimiento_html = ""
    for item in datos["conocimiento"]:
        partes = item.split(": ", 1)
        if len(partes) == 2:
            conocimiento_html += f'<p><strong>✓ {partes[0]}:</strong> {partes[1]}</p>'
        else:
            conocimiento_html += f'<p><strong>✓</strong> {item}</p>'

    # Generar testimonios HTML
    testimonios_html = ""
    for texto, autor in datos["testimonios"]:
        testimonios_html += f'<div class="testimonial"><p>"{texto}"</p><cite>— {autor}</cite></div>'

    template = f'''<!DOCTYPE html>
<html lang="es-MX">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{datos["titulo"]} | Servicio 24/7</title>
<meta name="description" content="Plomero en {nombre}, Mazatlán. {datos["subtitulo"][:150]}. WhatsApp: 669 132 5300">
<link rel="icon" href="../../../assets/icons/favicon.ico" sizes="any">
<link rel="stylesheet" href="../../../styles.min.css">
<link rel="canonical" href="https://plomeromazatlanpro.mx/servicios/plomero-colonias-mazatlan/{slug}/" />
<meta name="x-build" content="2025-12-03T23:00:00Z" />
<!-- JSON-LD Schema: Solo BreadcrumbList -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{
      "@type": "ListItem",
      "position": 1,
      "name": "Inicio",
      "item": "https://plomeromazatlanpro.mx/"
    }},
    {{
      "@type": "ListItem",
      "position": 2,
      "name": "Servicios",
      "item": "https://plomeromazatlanpro.mx/#servicios"
    }},
    {{
      "@type": "ListItem",
      "position": 3,
      "name": "Plomero por Colonias",
      "item": "https://plomeromazatlanpro.mx/servicios/plomero-colonias-mazatlan/"
    }},
    {{
      "@type": "ListItem",
      "position": 4,
      "name": "{nombre}",
      "item": "https://plomeromazatlanpro.mx/servicios/plomero-colonias-mazatlan/{slug}/"
    }}
  ]
}}
</script>

    <style>
    .breadcrumb {{
        background: #f8f9fa;
        padding: 12px 0;
        font-size: 14px;
        border-bottom: 1px solid #e9ecef;
    }}
    .breadcrumb-container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }}
    .breadcrumb-list {{
        display: flex;
        align-items: center;
        list-style: none;
        margin: 0;
        padding: 0;
        flex-wrap: wrap;
    }}
    .breadcrumb-item {{
        display: flex;
        align-items: center;
    }}
    .breadcrumb-item a {{
        color: #0066cc;
        text-decoration: none;
        transition: color 0.2s;
    }}
    .breadcrumb-item a:hover {{
        color: #004499;
        text-decoration: underline;
    }}
    .breadcrumb-item.active {{
        color: #6c757d;
    }}
    .breadcrumb-separator {{
        margin: 0 8px;
        color: #6c757d;
        user-select: none;
    }}
    @media (max-width: 768px) {{
        .breadcrumb {{
            font-size: 13px;
            padding: 10px 0;
        }}
        .breadcrumb-separator {{
            margin: 0 6px;
        }}
    }}
    </style>

</head>
<body>
<script>window.dataLayer=window.dataLayer||[];if(window.requestIdleCallback){{requestIdleCallback(()=>{{var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtm.js?id=GTM-W75CRTX5';document.head.appendChild(s);}})}};</script>
<nav class="nav"><div class="container"><div class="nav-wrapper"><a href="../../../" class="logo">
                    <img src="../../../logo-plomero-mazatlan-pro.webp" alt="Plomero Mazatlán Pro - Logo">
                </a><button class="mobile-menu-btn" aria-label="Menu"><span></span><span></span><span></span></button><ul class="nav-menu"><li><a href="../../../#inicio" class="nav-link">Inicio</a></li><li><a href="../../../#servicios" class="nav-link">Servicios</a></li><li><a href="../../../blog/" class="nav-link">Blog</a></li><li><a href="../../../#contacto" class="nav-link">Contacto</a></li></ul></div></div></nav>

    <!-- Breadcrumb Navigation -->
    <nav class="breadcrumb" aria-label="breadcrumb">
        <div class="breadcrumb-container">
            <ol class="breadcrumb-list">
            <li class="breadcrumb-item"><a href="https://plomeromazatlanpro.mx/">Inicio</a></li>
            <li class="breadcrumb-separator" aria-hidden="true">›</li>
            <li class="breadcrumb-item"><a href="https://plomeromazatlanpro.mx/#servicios">Servicios</a></li>
            <li class="breadcrumb-separator" aria-hidden="true">›</li>
            <li class="breadcrumb-item"><a href="https://plomeromazatlanpro.mx/servicios/plomero-colonias-mazatlan/">Plomero por Colonias</a></li>
            <li class="breadcrumb-separator" aria-hidden="true">›</li>
            <li class="breadcrumb-item active" aria-current="page">{nombre}</li>
            </ol>
        </div>
    </nav>
<header id="inicio" class="hero"><div class="container"><div class="hero-content"><h1 class="fade-in">{datos["titulo"]}</h1><p class="hero-subtitle fade-in">{datos["subtitulo"]}</p>
    <div style="background: #e8f4f8; padding: 20px; border-radius: 8px; margin: 24px 0; border-left: 4px solid #0066cc;">
        <p style="margin: 0; font-size: 15px; line-height: 1.6;">
            <strong>Nuestros servicios principales:</strong>
            <a href="../../emergencia-24-7/" style="color: #0066cc;">Emergencias 24/7</a>,
            <a href="../../destape-de-drenajes/" style="color: #0066cc;">destape de drenajes</a>,
            <a href="../../reparacion-de-fugas/" style="color: #0066cc;">reparación de fugas</a> y
            <a href="../../deteccion-de-fugas/" style="color: #0066cc;">detección de fugas</a>.
        </p>
    </div>
<p class="hero-contact">WhatsApp: 52 669 132 5300</p><a href="#contacto" class="btn-primary hover-lift">Solicitar Servicio en {nombre}</a></div></div></header>
<section class="section section-alt"><div class="container"><h2>Experiencia en {datos["experiencia"]}</h2><div class="benefits-grid">{beneficios_html}</div></div></section>
<section id="servicios" class="section"><div class="container"><h2>Servicios Especializados en {nombre}</h2><div class="grid">{servicios_html}</div></div></section>
<section class="section section-alt"><div class="container"><h2>Conocimiento de {nombre}</h2><div class="pricing-content"><div class="pricing-box"><h3>¿Por qué nos eligen en {nombre}?</h3>{conocimiento_html}</div></div></div></section>
<section class="section"><div class="container"><h2>Testimonios de {nombre}</h2><div class="testimonials">{testimonios_html}</div></div></section>
<section id="contacto" class="section section-alt"><div class="container"><h2>¿Necesitas Plomero en {nombre}?</h2><div class="final-cta"><p class="cta-text">WhatsApp: <strong>669 132 5300</strong></p><div class="cta-buttons"><a href="https://wa.me/526691325300?text=Hola,%20necesito%20un%20plomero%20en%20{slug.replace('-', '%20')}" target="_blank" class="btn-primary">WhatsApp</a><a href="tel:6691325300" class="btn-secondary">Llamar</a></div></div></div></section>
<footer class="footer"><div class="container"><p>&copy; 2025 Plomero Mazatlán Pro. Expertos en {nombre}. | <a href="/terminos/">Términos</a></p></div></footer>
<script>const m=document.querySelector('.mobile-menu-btn'),n=document.querySelector('.nav-menu');m.addEventListener('click',()=>{{n.classList.toggle('active');m.classList.toggle('active')}});document.querySelectorAll('.nav-link').forEach(l=>l.addEventListener('click',()=>{{n.classList.remove('active');m.classList.remove('active')}}));</script>
<style>.cta-bar{{position:fixed;right:16px;bottom:16px;display:flex;gap:10px;z-index:9999}}.cta-btn{{font:600 15px/1.1 system-ui;padding:12px 14px;border-radius:12px;color:#fff;text-decoration:none;box-shadow:0 6px 20px rgba(0,0,0,.15)}}.cta-wa{{background:#25D366}}.cta-tel{{background:#1E40AF}}</style>
<div class="cta-bar"><a id="cta-whatsapp" class="cta-btn cta-wa" href="https://wa.me/526691325300?text=Hola,%20necesito%20un%20plomero%20en%20{slug.replace('-', '%20')}" rel="noopener">💬 WhatsApp</a><a id="cta-llamar" class="cta-btn cta-tel" href="tel:+526691325300" rel="noopener">📞 Llamar</a></div>
</body>
</html>'''
    return template

def main():
    base_path = Path("/Users/hectorpc/Documents/Hector Palazuelos/Google My Business/Plomero Mazatlan Pro/servicios/plomero-colonias-mazatlan")

    created = 0

    # Primero eliminar las carpetas existentes
    import shutil
    for item in base_path.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
            print(f"🗑️ Eliminada: {item.name}/")

    # Crear colonias con datos específicos
    for nombre, datos in COLONIAS_PRINCIPALES.items():
        slug = slugify(nombre)
        colonia_path = base_path / slug
        colonia_path.mkdir(parents=True, exist_ok=True)

        html = generar_pagina(nombre, datos)
        with open(colonia_path / 'index.html', 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✓ Creada (específica): {nombre} -> {slug}/")
        created += 1

    # Cargar colonias del JSON oficial
    todas_colonias = cargar_colonias_del_json()
    print(f"\n📋 Total colonias en JSON: {len(todas_colonias)}")

    # Nombres de colonias principales (ya creadas arriba)
    principales = set(slugify(n) for n in COLONIAS_PRINCIPALES.keys())

    # Crear páginas para TODAS las colonias del JSON (excepto las principales)
    for nombre in todas_colonias:
        slug = slugify(nombre)

        # Saltar si ya se creó como colonia principal
        if slug in principales:
            continue

        colonia_path = base_path / slug
        colonia_path.mkdir(parents=True, exist_ok=True)

        datos = generar_datos_genericos(nombre)
        html = generar_pagina(nombre, datos)
        with open(colonia_path / 'index.html', 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✓ {nombre} -> {slug}/")
        created += 1

    print(f"\n✅ Total: {created} páginas de colonias creadas")

if __name__ == "__main__":
    main()
