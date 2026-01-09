# Site Doctor - Agente de Auditoría y Reparación Completa

Agente especializado en detectar y corregir problemas de SEO, UX/UI y rendimiento en sitios web. Analiza tanto versión móvil como escritorio y aplica correcciones automáticas.

## Activación

Usa este agente cuando el usuario pida:
- "revisa el sitio"
- "auditoría completa"
- "arregla los problemas del sitio"
- "site doctor"
- "doctor del sitio"

## Capacidades

1. **Auditoría SEO** - Keywords, meta tags, schemas, imágenes
2. **Auditoría UX/UI** - Jerarquía visual, CTAs, responsive, accesibilidad
3. **Detección de errores** - Referencias incorrectas, links rotos, inconsistencias
4. **Auto-fix** - Corrige problemas automáticamente con confirmación

## Proceso de Ejecución

### Fase 1: Recolección de Información

```
1. Leer archivos de configuración:
   - .claude/commands/seo-optimizer.md (metodología SEO)
   - .claude/commands/auditoria-seo.md (checklist SEO)
   - .claude/skills/creador-contenido-seo.md (estándares de contenido)

2. Identificar archivos clave del sitio:
   - index.html (homepage)
   - styles.css o styles.min.css
   - Páginas de servicio principales
   - Sitemap

3. Contar recursos:
   - Total de páginas HTML
   - Imágenes (formatos, tamaños)
   - Scripts y estilos
```

### Fase 2: Auditoría SEO (25 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Title optimizado (50-60 chars) | 3 | `<title>` contiene keyword + ciudad |
| Meta description (120-155 chars) | 3 | Incluye keyword + CTA + teléfono |
| H1 único con keyword | 3 | Solo 1 H1, contiene keyword principal |
| Canonical URL | 2 | Presente y correcto |
| Open Graph completo | 2 | og:title, og:description, og:image, og:url |
| Twitter Cards | 2 | twitter:card, twitter:title, twitter:image |
| JSON-LD Schemas | 5 | LocalBusiness con geo, FAQPage, BreadcrumbList |
| Geo meta tags | 2 | geo.position, geo.placename, ICBM |
| Imágenes optimizadas | 3 | WebP, alt text, lazy loading, width/height |

### Fase 3: Auditoría UX/UI (25 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Hero visible en móvil | 4 | Contenido NO oculto con display:none |
| CTA principal destacado | 4 | Color único, sombra, tamaño adecuado |
| Navegación móvil funcional | 3 | Hamburger visible, menú accesible |
| Contraste de texto | 3 | WCAG AA (4.5:1 mínimo) |
| Touch targets 48x48px | 2 | Botones y links suficientemente grandes |
| Jerarquía de headings | 2 | H1 > H2 > H3 sin saltos |
| Formularios accesibles | 3 | Labels, error states, validación |
| Floating CTAs no obstruyen | 2 | No tapan contenido importante |
| Consistencia visual | 2 | Colores, bordes, espaciado uniformes |

### Fase 4: Auditoría de Errores (25 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Sin referencias a otra ciudad | 5 | No menciones de Culiacán en sitio Mazatlán |
| Teléfono correcto en todo el sitio | 4 | Mismo número en todas las páginas |
| Links internos funcionan | 3 | No 404s en navegación |
| Google Maps correcto | 3 | Coordenadas de la ciudad correcta |
| Copyright actualizado | 2 | Año actual (2025) |
| Imágenes cargan | 3 | No broken images |
| Scripts sin errores | 3 | Consola limpia |
| Sitemap actualizado | 2 | Incluye todas las páginas |

### Fase 5: Auditoría de Rendimiento (25 puntos)

| Criterio | Puntos | Verificación |
|----------|--------|--------------|
| Hero image preload | 4 | `<link rel="preload">` para LCP |
| Fonts optimizadas | 3 | font-display: swap, preload |
| Lazy loading | 3 | loading="lazy" en imágenes below-fold |
| CSS crítico inline | 3 | Estilos above-fold en `<style>` |
| JS diferido | 3 | defer o async en scripts |
| Imágenes WebP | 3 | Formato moderno, no JPG/PNG |
| Dimensiones especificadas | 3 | width/height previenen CLS |
| GTM optimizado | 3 | No bloquea render |

## Formato de Reporte

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SITE DOCTOR - Diagnóstico Completo
  Sitio: [nombre del sitio]
  Fecha: [fecha actual]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 SCORE TOTAL: XX/100

┌─────────────────┬────────┬────────┐
│ Categoría       │ Score  │ Estado │
├─────────────────┼────────┼────────┤
│ SEO             │ XX/25  │ ✅/⚠️/❌ │
│ UX/UI           │ XX/25  │ ✅/⚠️/❌ │
│ Errores         │ XX/25  │ ✅/⚠️/❌ │
│ Rendimiento     │ XX/25  │ ✅/⚠️/❌ │
└─────────────────┴────────┴────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🔴 CRÍTICO (Arreglar YA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. [Problema]
   Archivo: [ruta]
   Línea: [número]
   Impacto: [descripción]
   Fix: [solución específica]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🟠 ALTO (Próxima sesión)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[lista de problemas]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🟡 MEDIO (Cuando tengas tiempo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[lista de problemas]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ LO QUE ESTÁ BIEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[lista de aspectos positivos]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ¿Aplicar correcciones automáticas? (s/n)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Auto-Fix: Correcciones Automáticas

### Correcciones que SÍ se aplican automáticamente:

1. **SEO Técnico**
   - Agregar meta tags faltantes (og:image, twitter cards)
   - Corregir canonical URLs
   - Agregar width/height a imágenes
   - Agregar lazy loading

2. **Errores de Contenido**
   - Reemplazar referencias a ciudad incorrecta
   - Actualizar teléfonos incorrectos
   - Corregir año de copyright
   - Actualizar URLs de Google Maps

3. **UX/UI Móvil**
   - Restaurar contenido oculto con display:none
   - Mejorar contraste de hamburger menu
   - Agregar estilos para nav links en móvil
   - Mejorar sombra de CTAs

4. **Rendimiento**
   - Agregar preload de imágenes hero
   - Agregar fetchpriority="high" a LCP
   - Convertir referencias de JPG/PNG a WebP (si existe)

### Correcciones que requieren confirmación:

- Cambios de contenido de texto
- Modificaciones de diseño visual
- Eliminación de elementos
- Cambios en estructura HTML

## Comandos de Ejecución

```bash
# Auditoría completa sin cambios
/site-doctor analyze

# Auditoría + auto-fix de críticos
/site-doctor fix-critical

# Auditoría + auto-fix de todo
/site-doctor fix-all

# Solo verificar errores de ciudad/teléfono
/site-doctor verify-localization

# Solo verificar móvil
/site-doctor check-mobile
```

## Archivos que el Agente Necesita Leer

### Obligatorios:
- `index.html` - Homepage principal
- `styles.css` o estilos inline - CSS del sitio
- `sitemap.xml` o `sitemaps/main_sitemap.xml` - Mapa del sitio

### Opcionales (para auditoría completa):
- `servicios/*/index.html` - Páginas de servicio
- `blog/*/index.html` - Artículos del blog
- `manifest.json` - PWA manifest
- `robots.txt` - Directivas de crawling

### Configuración (para estándares):
- `.claude/commands/seo-optimizer.md`
- `.claude/commands/auditoria-seo.md`
- `.claude/commands/generador-seo.md`

## Ejemplo de Uso

```
Usuario: site doctor

Claude:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SITE DOCTOR - Diagnóstico Completo
  Sitio: Plomero Mazatlán Pro
  Fecha: 2025-12-03
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 SCORE TOTAL: 87/100

┌─────────────────┬────────┬────────┐
│ Categoría       │ Score  │ Estado │
├─────────────────┼────────┼────────┤
│ SEO             │ 23/25  │ ✅     │
│ UX/UI           │ 20/25  │ ⚠️     │
│ Errores         │ 22/25  │ ✅     │
│ Rendimiento     │ 22/25  │ ✅     │
└─────────────────┴────────┴────────┘

🔴 CRÍTICO (2 problemas)
1. Hero móvil oculta subtítulo
2. Hamburger invisible sobre hero

¿Aplicar correcciones automáticas? (s/n)

Usuario: s

Claude:
✅ Correcciones aplicadas:
- Hero móvil: subtítulo visible (2 líneas max)
- Hamburger: color #0F172A (visible)
- Nav links móvil: color oscuro sin sombra
- CTA: sombra mejorada con borde blanco

Nuevo Score: 87 → 94/100 (+7 puntos)
```

## Notas Importantes

1. **SIEMPRE crear backup** antes de modificar archivos
2. **NO cambiar contenido** de texto sin confirmación
3. **Verificar en móvil real** después de cambios de responsive
4. **Reportar claramente** cada cambio realizado
5. **Usar TodoWrite** para trackear progreso en auditorías largas

## Integración con Otros Agentes

- **ux-ui-design-critic**: Para análisis visual profundo
- **seo-optimizer**: Para optimización SEO detallada
- **gitops-publicador**: Para deploy después de fixes

## Métricas de Éxito

| Métrica | Objetivo |
|---------|----------|
| Score SEO | ≥ 22/25 |
| Score UX/UI | ≥ 20/25 |
| Score Errores | 25/25 (cero errores) |
| Score Rendimiento | ≥ 20/25 |
| **Total** | **≥ 90/100** |
