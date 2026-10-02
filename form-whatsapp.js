/* Formularios de contacto → WhatsApp.
   El sitio vive en GitHub Pages: no hay backend que reciba formularios (los atributos de
   Netlify no hacen nada aquí; antes los POST daban error 405 y los datos se perdían).
   Cualquier formulario arma un mensaje con lo que escribió la persona, abre WhatsApp y
   después lleva a /gracias/. La medición (generate_lead) la registra el bloque de cada
   página, que escucha el submit antes que este script. */
(function() {
  var WHATSAPP = '526673922273';
  var ETIQUETAS = { nombre: 'Nombre', telefono: 'Teléfono', email: 'Email', colonia: 'Colonia',
                    servicio: 'Servicio', mensaje: 'Mensaje' };
  var OMITIR = { 'form-name': 1, 'bot-field': 1, origen: 1 };
  document.addEventListener('submit', function(e) {
    var f = e.target;
    if (!f || f.tagName !== 'FORM' || f.hasAttribute('data-sin-whatsapp')) return;
    e.preventDefault();
    var trampa = f.querySelector('[name="bot-field"]');
    if (trampa && trampa.value) return; // robot
    var lineas = ['Hola, solicito cotización de plomería en Mazatlán:'];
    new FormData(f).forEach(function(v, k) {
      v = String(v).trim();
      if (OMITIR[k] || !v) return;
      lineas.push((ETIQUETAS[k] || k) + ': ' + v);
    });
    lineas.push('Página: ' + location.pathname);
    var url = 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(lineas.join('\n'));
    var ventana = null;
    try { ventana = window.open(url, '_blank'); } catch (err) {}
    if (ventana) setTimeout(function() { location.href = '/gracias/'; }, 700);
    else location.href = url; // bloqueador de ventanas: ir directo a WhatsApp
  });
})();
