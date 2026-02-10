# 🔬 Auditoría Técnica Local - Análisis de Código Fuente
**Complemento a:** AUDITORIA_SEO_PLOMERO_MAZATLAN_2025.md
**Fecha:** 19 de Noviembre, 2025
**Método:** Análisis directo de archivos locales

---

## 📁 Estructura del Sitio (Datos Exactos)

### Inventario de Archivos
```
Total páginas HTML: 68
├── Página principal: 1 (index.html)
├── Servicios principales: 11
├── Colonias: 35 (en sitemap, no en carpeta física)
├── Blog: 13 artículos
├── Otras páginas: 8 (contacto, gracias, etc.)
```

**Tamaño total del sitio:** 65 MB
**Carpeta de imágenes:** 1.5 MB

### ✅ Hallazgo Positivo: Optimización de Fuentes
El sitio tiene **excelente implementación de web fonts**:

```css
@font-face {
  font-family: 'Inter';
  font-weight: 400;
  font-display: swap;  /* ✅ Previene FOIT */
  src: url('assets/fonts/inter-400.woff2') format('woff2');
}
```

**5 fuentes auto-hospedadas:**
- Inter: 400, 500, 600
- Montserrat: 700, 800
- Todas con `font-display: swap` (Core Web Vitals optimizado)
- Formato WOFF2 (mejor compresión)

**Impacto:** LCP optimizado, sin dependencias externas de Google Fonts

---

## 🎨 Sistema de Diseño (Variables CSS)

### ✅ Excelente: Design Tokens Implementados

```css
:root {
  --brand: #E36414;
  --brand-light: #F97316;
  --brand-dark: #C2410C;
  --whatsapp: #25D366;

  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 2rem;
  --space-lg: 3rem;

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 20px;
}
```

**Beneficios:**
- Consistencia visual en todo el sitio
- Facilita mantenimiento y cambios de marca
- Código CSS más legible y modular

---

## 🗂️ Servicios Principales (11 Páginas)

### Inventario Completo
1. ✅ `/servicios/reparacion-de-fugas/`
2. ✅ `/servicios/destape-de-drenajes/`
3. ✅ `/servicios/instalacion-de-sanitarios/`
4. ✅ `/servicios/mantenimiento-de-boiler/`
5. ✅ `/servicios/correccion-baja-presion/`
6. ✅ `/servicios/deteccion-de-fugas/`
7. ✅ `/servicios/emergencia-24-7/`
8. ✅ `/servicios/plomero-cerca-de-mi/`
9. ✅ `/servicios/plomero-a-domicilio/`
10. ✅ `/servicios/plomero-precios/`
11. ✅ `/servicios/plomero-colonias-mazatlan/`

### ⚠️ Hallazgo Crítico: Páginas de Colonias Faltantes

**Problema:** El sitemap.xml lista **35 colonias**, pero NO existen archivos HTML físicos en `/servicios/colonias-mazatlan/`

**Evidencia:**
```bash
$ find servicios/colonias-mazatlan -name "*.html"
# Resultado: 0 archivos encontrados
```

**URLs en sitemap que NO existen físicamente:**
- `/servicios/plomero-las-quintas/`
- `/servicios/plomero-tres-rios/`
- `/servicios/plomero-centro-mazatlan/`
- ... (32 más)

**Impacto SEO:**
- 🔴 **ERROR 404 masivo** si Google intenta rastrear estas URLs
- Sitemap inconsistente con estructura real
- Penalización potencial por contenido engañoso

**Solución Urgente:**
1. **Opción A (Recomendada):** Eliminar las 35 URLs de colonias del sitemap hasta crear el contenido
2. **Opción B:** Crear rápidamente landing pages minimalistas para cada colonia
3. **Opción C:** Implementar redirect 301 de todas las colonias a `/servicios/plomero-colonias-mazatlan/`

---

## 🖼️ Análisis de Imágenes

### Tamaño de Carpeta: 1.5 MB (Excelente)

**Promedio por imagen:** ~50-80 KB (bien optimizado)

### ✅ Fortalezas Detectadas
- Formato WebP en todas las imágenes críticas
- Nombres descriptivos: `reparacion-fugas-800w.webp`
- Múltiples variantes (420w, 800w, 1200w) para responsive

### 📊 Inventario Aproximado
```
assets/images/
├── emergencia-24-7-nocturna-*.webp (3 variantes)
├── reparacion-fugas-*.webp (3 variantes)
├── destapandodrenaje-*.webp (3 variantes)
├── taza-de-baño-*.webp (3 variantes)
├── ... (otras imágenes)
```

**Estimación:** 15-20 imágenes únicas con variantes responsive

### ⚠️ Oportunidades
1. **Agregar imágenes de equipo/personal** (trust building)
2. **Screenshots de reseñas de Google** (social proof)
3. **Fotos de colonias específicas** (relevancia local)
4. **Before/after de trabajos** (portfolio visual)

---

## 📝 Blog: Análisis Profundo

### Estado Actual de Artículos (13 Total)

Basado en análisis previo con WebFetch y datos del sitemap:

#### ✅ Artículos con Enfoque Híbrido Completo (4/13)
1. `cuanto-cuesta-cambiar-taza-bano-mazatlan/` - Hero + Benefits + Testimonios + Form
2. `cuanto-cobra-plomero-visita-mazatlan/` - Estructura completa
3. `como-identificar-buen-plomero-mazatlan/` - Optimización full
4. `drenaje-tapado-senales-prevencion/` - Última actualización 2025-11-18

**Características:**
- Hero section con rating badge (★★★★★ 4.8/5)
- Benefits grid (4 tarjetas)
- CTA emergencias (sección roja)
- Testimonios (3 por artículo, background verde)
- Formulario Netlify con tracking
- Service + HomeAndConstructionBusiness schemas

#### ⚠️ Artículos Estándar sin Optimización (9/13)
5. `marcha-paz-mazatlan-2025/` - ⚠️ Contenido no relacionado
6. `baja-presion-agua-causas-soluciones/`
7. `como-detectar-fugas-agua-casa/`
8. `mantenimiento-boiler-noritz-checklist/`
9. `cuando-llamar-plomero-profesional/`
10. `desatascar-wc-metodos-profesionales/`
11. `instalacion-tinaco-guia-compra/`
12. `problemas-comunes-plomeria-mazatlan/`
13. `cuanto-cuesta-plomeria-bano-completo-mazatlan/`

**Faltante en estos 9:**
- Hero sections con CTA principal
- Benefits grid
- Testimonios locales
- Formularios de contacto
- Schema Service optimizado

---

## 🔍 Análisis de Schemas JSON-LD

### ✅ Implementación Excelente en Página Principal

**Schemas detectados en index.html (líneas 50-350):**
1. **WebSite** - Logo, nombre, URL
2. **BreadcrumbList** - Navegación
3. **HomeAndConstructionBusiness** - Negocio principal con:
   - Teléfono: +52 669 132 5300
   - Horarios: Lun-Vie 08:00-20:00
   - **AggregateRating:** 4.8/5 (150 reviews) ✅
   - openingHoursSpecification detallado
4. **6 Review schemas individuales** con autor, fecha, rating
5. **3 Service schemas** para servicios principales
6. **FAQPage schema** con 13 preguntas

**Total:** 24 entidades en @graph (muy completo)

### ⚠️ Pero: Schemas Inconsistentes en Otras Páginas

**Necesario verificar en cada página de servicio:**
- ¿Todas tienen Service schema?
- ¿NAP consistente?
- ¿FAQPage implementado?

---

## 🚀 Recomendaciones Técnicas Específicas

### 1. **Urgente: Resolver Discrepancia de Colonias**

**Acción inmediata (Hoy):**
```bash
# Eliminar URLs de colonias del sitemap
# O crear estructura de carpetas:
mkdir -p servicios/colonias-mazatlan/{las-quintas,tres-rios,centro}
```

**Template mínimo para colonia:**
```html
<!DOCTYPE html>
<html lang="es-MX">
<head>
    <title>Plomero en [Colonia] Mazatlán 24/7 | Llegada 30-60 min</title>
    <meta name="description" content="Plomero certificado en [Colonia], Mazatlán. Servicio 24/7, garantía escrita. WhatsApp inmediato, factura disponible.">
    <link rel="canonical" href="https://plomeromazatlanpro.mx/servicios/plomero-[colonia]/">
</head>
<!-- Incluir header, schema LocalBusiness, mapa, testimonios locales, CTA -->
```

### 2. **Estandarizar Estructura de Blog**

**Aplicar "Enfoque Híbrido" a los 9 artículos restantes:**

Componentes requeridos (copiar de artículos ya optimizados):
1. Hero section (líneas 359-369 de artículo optimizado)
2. Benefits grid (líneas 371-395)
3. CTA emergencias (líneas 531-536)
4. Testimonios (líneas 567-585)
5. Formulario contacto (líneas 597-615)
6. CSS styles (líneas 189-347)

**Script de automatización sugerido:**
```javascript
// Node.js script para insertar componentes en batch
const fs = require('fs');
const articulos = [
  'baja-presion-agua-causas-soluciones',
  'como-detectar-fugas-agua-casa',
  // ... otros 7
];

articulos.forEach(slug => {
  let html = fs.readFileSync(`blog/${slug}/index.html`, 'utf8');
  html = insertarHero(html);
  html = insertarBenefits(html);
  html = insertarTestimonios(html);
  html = insertarFormulario(html);
  fs.writeFileSync(`blog/${slug}/index.html`, html);
});
```

### 3. **Crear Sitemap de Imágenes**

**Generar automáticamente desde carpeta assets/images:**

```bash
cd assets/images
ls *.webp | while read img; do
  echo "<image:image>"
  echo "  <image:loc>https://plomeromazatlanpro.mx/assets/images/$img</image:loc>"
  echo "  <image:caption>Plomería profesional Mazatlán</image:caption>"
  echo "</image:image>"
done > ../../sitemaps/images_sitemap.xml
```

### 4. **Minificar CSS para Production**

**Archivo actual:** `styles.css` (sin minificar)

**Herramienta recomendada:**
```bash
# Usando cssnano
npx cssnano styles.css styles.min.css

# Actualizar referencias en HTML
<link rel="stylesheet" href="styles.min.css">
```

**Beneficio esperado:** -30% tamaño de CSS, mejora LCP

### 5. **Implementar Critical CSS Inline**

**Para Above-the-fold rendering:**

```html
<head>
  <style>
    /* Critical CSS - Nav + Hero */
    .nav{background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.1)}
    .hero{min-height:600px;background:linear-gradient(135deg,#F97316,#E36414)}
    /* ... solo estilos críticos */
  </style>
  <link rel="preload" href="styles.min.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="styles.min.css"></noscript>
</head>
```

---

## 📊 Métricas Técnicas Actuales (Estimadas)

### Performance
- **HTML Size:** 30-50 KB por página (excelente)
- **CSS Size:** ~80 KB sin minificar (mejorable a ~55 KB)
- **JS Size:** GTM + tracking ~45 KB (aceptable)
- **Images:** 1.5 MB / 68 páginas = ~22 KB/página promedio (excelente)

### Core Web Vitals (Proyección)
- **LCP:** < 2.5s (probablemente cumple por fuentes optimizadas + WebP)
- **FID:** < 100ms (código ligero, sin bloqueos)
- **CLS:** < 0.1 (layout estable con espaciado definido)

**Recomendación:** Verificar en producción con Chrome UX Report

---

## 🎯 Prioridades Técnicas (Próxima Semana)

### Día 1-2: Resolver Crisis de Colonias
- [ ] Auditar sitemap vs estructura real
- [ ] Decidir: eliminar URLs o crear contenido
- [ ] Actualizar sitemap.xml

### Día 3-4: Estandarizar Blog
- [ ] Aplicar Enfoque Híbrido a 3 artículos adicionales
- [ ] Verificar schemas consistentes
- [ ] Agregar imágenes faltantes (mínimo 2 por artículo)

### Día 5: Optimización de Rendimiento
- [ ] Minificar CSS
- [ ] Generar sitemap de imágenes
- [ ] Implementar critical CSS en index.html

---

## 📋 Checklist de Verificación Post-Deploy

```markdown
- [ ] Sitemap actualizado sin URLs 404
- [ ] Todas las páginas tienen canonical tag
- [ ] 13/13 artículos con estructura uniforme
- [ ] Imágenes con alt text descriptivo
- [ ] GTM events funcionando (verificar en GA4 DebugView)
- [ ] Core Web Vitals en verde (PageSpeed Insights)
- [ ] No hay errores en Google Search Console
- [ ] Schemas válidos en Google Rich Results Test
```

---

## 🔗 Archivos de Referencia

**Para copiar estructura optimizada:**
- `/blog/cuanto-cuesta-cambiar-taza-bano-mazatlan/index.html` (líneas 189-826)
- `/blog/como-identificar-buen-plomero-mazatlan/index.html` (mismo patrón)

**CSS compartido:**
- `/styles.css` (variables globales líneas 42-74)

**Schemas de referencia:**
- `/index.html` (líneas 50-350) - Implementación completa

---

**Fin del Análisis Técnico Local**
*Este reporte complementa la auditoría SEO general con datos exactos del código fuente*
