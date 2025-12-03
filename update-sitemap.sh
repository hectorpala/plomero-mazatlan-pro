#!/bin/bash
# Script para actualizar automáticamente las fechas del sitemap basándose en las últimas modificaciones
# Uso: ./update-sitemap.sh

SITEMAP="sitemaps/main_sitemap.xml"
TEMP_FILE="sitemaps/sitemap_temp.xml"

# Obtener la fecha actual en formato ISO 8601
CURRENT_DATE=$(date -u +"%Y-%m-%dT%H:%M:%S+00:00")

echo "🔄 Actualizando sitemap con fechas reales de modificación..."

# Función para obtener la fecha de modificación de un archivo
get_file_date() {
    local url="$1"
    local file_path=""

    # Convertir URL a ruta de archivo
    if [ "$url" = "https://plomeromazatlanpro.mx/" ]; then
        file_path="index.html"
    elif echo "$url" | grep -q "/blog/"; then
        # Extraer el path después de /blog/
        local blog_path="${url#https://plomeromazatlanpro.mx/blog/}"
        blog_path="${blog_path%/}"
        if [ -z "$blog_path" ]; then
            file_path="blog/index.html"
        else
            file_path="blog/$blog_path/index.html"
        fi
    else
        # Para servicios y otras páginas
        local page_path="${url#https://plomeromazatlanpro.mx/}"
        page_path="${page_path%/}"
        file_path="$page_path/index.html"
    fi

    # Verificar si el archivo existe y obtener su fecha de modificación
    if [ -f "$file_path" ]; then
        # macOS usa -f para formato de fecha personalizado
        stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S+00:00" "$file_path" 2>/dev/null || echo "$CURRENT_DATE"
    else
        echo "$CURRENT_DATE"
    fi
}

# Función para determinar changefreq basado en el tipo de página
get_changefreq() {
    local url="$1"

    if [ "$url" = "https://plomeromazatlanpro.mx/" ]; then
        echo "weekly"  # Homepage se actualiza frecuentemente
    elif echo "$url" | grep -q "/blog/" && [ "$url" != "https://plomeromazatlanpro.mx/blog/" ]; then
        echo "monthly"  # Artículos de blog son contenido estático
    elif [ "$url" = "https://plomeromazatlanpro.mx/blog/" ]; then
        echo "weekly"  # El índice del blog se actualiza con nuevos artículos
    elif echo "$url" | grep -q "/contacto/"; then
        echo "yearly"  # Página de contacto rara vez cambia
    else
        echo "monthly"  # Páginas de servicio son relativamente estables
    fi
}

# Crear el sitemap directamente con todas las URLs
cat > "$TEMP_FILE" << 'XMLEOF'
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
XMLEOF

# Procesar cada URL individualmente
process_url() {
    local url="$1"
    local priority="$2"
    local lastmod=$(get_file_date "$url")
    local changefreq=$(get_changefreq "$url")

    cat >> "$TEMP_FILE" << URLEOF
  <url>
    <loc>$url</loc>
    <lastmod>$lastmod</lastmod>
    <changefreq>$changefreq</changefreq>
    <priority>$priority</priority>
  </url>
URLEOF
}

# Procesar todas las URLs
process_url "https://plomeromazatlanpro.mx/" "1.0"
process_url "https://plomeromazatlanpro.mx/servicios/emergencia-24-7/" "0.9"
process_url "https://plomeromazatlanpro.mx/servicios/plomero-cerca-de-mi/" "0.8"
process_url "https://plomeromazatlanpro.mx/servicios/plomero-a-domicilio/" "0.8"
process_url "https://plomeromazatlanpro.mx/servicios/plomero-precios/" "0.8"
process_url "https://plomeromazatlanpro.mx/servicios/plomero-colonias-mazatlan/" "0.8"
process_url "https://plomeromazatlanpro.mx/servicios/reparacion-de-fugas/" "0.9"
process_url "https://plomeromazatlanpro.mx/servicios/destape-de-drenajes/" "0.9"
process_url "https://plomeromazatlanpro.mx/servicios/instalacion-de-sanitarios/" "0.9"
process_url "https://plomeromazatlanpro.mx/servicios/mantenimiento-de-boiler/" "0.9"
process_url "https://plomeromazatlanpro.mx/servicios/correccion-baja-presion/" "0.9"
process_url "https://plomeromazatlanpro.mx/servicios/deteccion-de-fugas/" "0.9"
process_url "https://plomeromazatlanpro.mx/contacto/" "0.7"
process_url "https://plomeromazatlanpro.mx/blog/" "0.8"
process_url "https://plomeromazatlanpro.mx/blog/marcha-paz-mazatlan-2025/" "0.6"
process_url "https://plomeromazatlanpro.mx/blog/mantenimiento-boiler-noritz-checklist/" "0.7"
process_url "https://plomeromazatlanpro.mx/blog/baja-presion-agua-causas-soluciones/" "0.7"
process_url "https://plomeromazatlanpro.mx/blog/como-detectar-fugas-agua-casa/" "0.7"
process_url "https://plomeromazatlanpro.mx/blog/desatascar-wc-metodos-profesionales/" "0.7"
process_url "https://plomeromazatlanpro.mx/blog/problemas-comunes-plomeria-mazatlan/" "0.7"
process_url "https://plomeromazatlanpro.mx/blog/instalacion-tinaco-guia-compra/" "0.7"
process_url "https://plomeromazatlanpro.mx/blog/cuando-llamar-plomero-profesional/" "0.7"
process_url "https://plomeromazatlanpro.mx/blog/drenaje-tapado-senales-prevencion/" "0.7"

# Cerrar el XML
echo "</urlset>" >> "$TEMP_FILE"

# Reemplazar el sitemap original
mv "$TEMP_FILE" "$SITEMAP"

echo "✅ Sitemap actualizado exitosamente en $SITEMAP"
echo "📅 Fecha de actualización: $CURRENT_DATE"

# Mostrar resumen
echo ""
echo "📊 Resumen de changefreq:"
echo "  - weekly:  Homepage, Blog index"
echo "  - monthly: Servicios, Artículos de blog"
echo "  - yearly:  Contacto"
