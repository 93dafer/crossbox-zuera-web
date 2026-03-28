import os

template = """<!DOCTYPE html>
<html class="dark" lang="es">
<head>
  <meta charset="utf-8" />
  <meta content="width=device-width, initial-scale=1.0" name="viewport" />
  <title>{title} | CROSSBOXZUERA</title>
  <script src="https://cdn.tailwindcss.com?plugins=forms,typography"></script>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <script>
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "surface-container-low": "#1c1b1b",
            "primary-container": "#d2261e",
            "on-surface-variant": "#e5bdb8",
            "surface": "#131313",
            "on-surface": "#e5e2e1",
          }},
          fontFamily: {{
            "headline": ["Space Grotesk"],
            "body": ["Inter"],
            "label": ["Space Grotesk"]
          }},
        }},
      }},
    }}
  </script>
</head>
<body class="bg-[#131313] text-[#e5e2e1] font-body selection:bg-primary-container selection:text-[#ffebe8]">
  <nav class="w-full bg-[#131313]/60 backdrop-blur-xl border-b border-[#5c403c]/15 px-8 py-6 sticky top-0 z-50">
    <a href="code.html" class="flex items-center h-16 group cursor-pointer inline-block">
      <img alt="CROSSBOX ZUERA" class="h-full object-contain" src="./logo.png" />
    </a>
  </nav>
  <main class="max-w-4xl mx-auto py-24 px-8 prose prose-invert prose-headings:font-headline prose-headings:font-black prose-headings:uppercase prose-p:text-[#e5bdb8] prose-a:text-[#d2261e]">
    {content}
  </main>
</body>
</html>"""

privacidad = """<h1>Política de Privacidad</h1>
<p>El presente Política de Privacidad establece los términos en que CrossboxZuera usa y protege la información que es proporcionada por sus usuarios al momento de utilizar su sitio web. Esta compañía está comprometida con la seguridad de los datos de sus usuarios. Cuando le pedimos llenar los campos de información personal con la cual usted pueda ser identificado, lo hacemos asegurando que sólo se empleará de acuerdo con los términos de este documento. Sin embargo esta Política de Privacidad puede cambiar con el tiempo o ser actualizada por lo que le recomendamos y enfatizamos revisar continuamente esta página para asegurarse que está de acuerdo con dichos cambios.</p>
<h2>Información que es recogida</h2>
<p>Nuestro sitio web podrá recoger información personal por ejemplo: Nombre, información de contacto como su dirección de correo electrónica e información demográfica. Así mismo cuando sea necesario podrá ser requerida información específica para procesar algún pedido o realizar una entrega o facturación.</p>
<h2>Uso de la información recogida</h2>
<p>Nuestro sitio web emplea la información con el fin de proporcionar el mejor servicio posible, particularmente para mantener un registro de usuarios, de pedidos en caso que aplique, y mejorar nuestros productos y servicios. Es posible que sean enviados correos electrónicos periódicamente a través de nuestro sitio con ofertas especiales, nuevos productos y otra información publicitaria que consideremos relevante para usted o que pueda brindarle algún beneficio, estos correos electrónicos serán enviados a la dirección que usted proporcione y podrán ser cancelados en cualquier momento.</p>
<p>CrossBoxZuera está altamente comprometido para cumplir con el compromiso de mantener su información segura. Usamos los sistemas más avanzados y los actualizamos constantemente para asegurarnos que no exista ningún acceso no autorizado.</p>
<h2>Cookies</h2>
<p>Una cookie se refiere a un fichero que es enviado con la finalidad de solicitar permiso para almacenarse en su ordenador, al aceptar dicho fichero se crea y la cookie sirve entonces para tener información respecto al tráfico web, y también facilita las futuras visitas a una web recurrente. Otra función que tienen las cookies es que con ellas las web pueden reconocerte individualmente y por tanto brindarte el mejor servicio personalizado de su web.</p>
<p>Nuestro sitio web emplea las cookies para poder identificar las páginas que son visitadas y su frecuencia. Esta información es empleada únicamente para análisis estadístico y después la información se elimina de forma permanente. Usted puede eliminar las cookies en cualquier momento desde su ordenador. Sin embargo las cookies ayudan a proporcionar un mejor servicio de los sitios web, estás no dan acceso a información de su ordenador ni de usted, a menos de que usted así lo quiera y la proporcione directamente. Usted puede aceptar o negar el uso de cookies, sin embargo la mayoría de navegadores aceptan cookies automáticamente pues sirve para tener un mejor servicio web. También usted puede cambiar la configuración de su ordenador para declinar las cookies. Si se declinan es posible que no pueda utilizar algunos de nuestros servicios.</p>
<h2>Enlaces a Terceros</h2>
<p>Este sitio web pudiera contener enlaces a otros sitios que pudieran ser de su interés. Una vez que usted de clic en estos enlaces y abandone nuestra página, ya no tenemos control sobre al sitio al que es redirigido y por lo tanto no somos responsables de los términos o privacidad ni de la protección de sus datos en esos otros sitios terceros. Dichos sitios están sujetos a sus propias políticas de privacidad por lo cual es recomendable que los consulte para confirmar que usted está de acuerdo con estas.</p>
<h2>Control de su información personal</h2>
<p>En cualquier momento usted puede restringir la recopilación o el uso de la información personal que es proporcionada a nuestro sitio web. Cada vez que se le solicite rellenar un formulario, como el de alta de usuario, puede marcar o desmarcar la opción de recibir información por correo electrónico. En caso de que haya marcado la opción de recibir nuestro boletín o publicidad usted puede cancelarla en cualquier momento.</p>
<p>Esta compañía no venderá, cederá ni distribuirá la información personal que es recopilada sin su consentimiento, salvo que sea requerido por un juez con un orden judicial.</p>"""

cookies = """<h1>Política de Cookies</h1>
<p>www.crossboxzuera.com</p>
<p>El acceso a este Sitio Web puede implicar la utilización de cookies. Las cookies son pequeñas cantidades de información que se almacenan en el navegador utilizado por cada Usuario —en los distintos dispositivos que pueda utilizar para navegar— para que el servidor recuerde cierta información que posteriormente y únicamente el servidor que la implementó leerá. Las cookies facilitan la navegación, la hacen más amigable, y no dañan el dispositivo de navegación.</p>
<p>Las cookies son procedimientos automáticos de recogida de información relativa a las preferencias determinadas por el Usuario durante su visita al Sitio Web con el fin de reconocerlo como Usuario, y personalizar su experiencia y el uso del Sitio Web, y pueden también, por ejemplo, ayudar a identificar y resolver errores.</p>
<p>La información recabada a través de las cookies puede incluir la fecha y hora de visitas al Sitio Web, las páginas visionadas, el tiempo que ha estado en el Sitio Web y los sitios visitados justo antes y después del mismo. Sin embargo, ninguna cookie permite que esta misma pueda contactarse con el número de teléfono del Usuario o con cualquier otro medio de contacto personal. Ninguna cookie puede extraer información del disco duro del Usuario o robar información personal. La única manera de que la información privada del Usuario forme parte del archivo Cookie es que el usuario dé personalmente esa información al servidor.</p>
<p>Las cookies que permiten identificar a una persona se consideran datos personales. Por tanto, a las mismas les será de aplicación la Política de Privacidad anteriormente descrita. En este sentido, para la utilización de las mismas será necesario el consentimiento del Usuario. Este consentimiento será comunicado, en base a una elección auténtica, ofrecido mediante una decisión afirmativa y positiva, antes del tratamiento inicial, removible y documentado.</p>
<h2>Cookies propias</h2>
<p>Son aquellas cookies que son enviadas al ordenador o dispositivo del Usuario y gestionadas exclusivamente por CrossBoxZuera para el mejor funcionamiento del Sitio Web. La información que se recaba se emplea para mejorar la calidad del Sitio Web y su Contenido y su experiencia como Usuario. Estas cookies permiten reconocer al Usuario como visitante recurrente del Sitio Web y adaptar el contenido para ofrecerle contenidos que se ajusten a sus preferencias.</p>
<h2>Deshabilitar, rechazar y eliminar cookies</h2>
<p>El Usuario puede deshabilitar, rechazar y eliminar las cookies —total o parcialmente— instaladas en su dispositivo mediante la configuración de su navegador (entre los que se encuentran, por ejemplo, Chrome, Firefox, Safari, Explorer). En este sentido, los procedimientos para rechazar y eliminar las cookies pueden diferir de un navegador de Internet a otro. En consecuencia, el Usuario debe acudir a las instrucciones facilitadas por el propio navegador de Internet que esté utilizando. En el supuesto de que rechace el uso de cookies —total o parcialmente— podrá seguir usando el Sitio Web, si bien podrá tener limitada la experiencia de uso.</p>"""

aviso = """<h1>Aviso Legal</h1>
<h2>LEY DE LOS SERVICIOS DE LA SOCIEDAD DE LA INFORMACIÓN (LSSI)</h2>
<p>CrossBox Zuera, responsable del sitio web, en adelante RESPONSABLE, pone a disposición de los usuarios el presente documento, con el que pretende dar cumplimiento a las obligaciones dispuestas en la Ley 34/2002, de 11 de julio, de Servicios de la Sociedad de la Información y del Comercio Electrónico (LSSICE), así como informar a todos los usuarios del sitio web respecto a cuáles son las condiciones de uso.</p>
<p>Toda persona que acceda a este sitio web asume el papel de usuario, comprometiéndose a la observancia y cumplimiento riguroso de las disposiciones aquí dispuestas, así como a cualquier otra disposición legal que fuera de aplicación.</p>
<p>CrossBox Zuera se reserva el derecho de modificar cualquier tipo de información que pudiera aparecer en el sitio web, sin que exista obligación de preavisar o poner en conocimiento de los usuarios dichas obligaciones, entendiéndose como suficiente con la publicación en el sitio web de ATLAS & FALCATA SL</p>
<h2>1. DATOS IDENTIFICATIVOS</h2>
<p>Denominación social: ATLAS & FALCATA SL<br>Nombre comercial: CROSSBOXZUERA<br>CIF: B44912590<br>Domicilio: AVENIDA PIRINEOS 16, ZUERA, ZARAGOZA<br>e-mail: hola@crossboxzuera.com</p>
<h2>2. OBJETO</h2>
<p>A través del Sitio Web, les ofrecemos a los Usuarios la posibilidad de acceder a la información sobre nuestros servicios.</p>
<h2>3. PRIVACIDAD Y TRATAMIENTO DE DATOS</h2>
<p>Cuando para el acceso a determinados contenidos o servicio sea necesario facilitar datos de carácter personal, los Usuarios garantizarán su veracidad, exactitud, autenticidad y vigencia. La empresa dará a dichos datos el tratamiento automatizado que corresponda en función de su naturaleza o finalidad, en los términos indicados en la sección de Política de Privacidad.</p>
<h2>4. PROPIEDAD INDUSTRIAL E INTELECTUAL</h2>
<p>El Usuario reconoce y acepta que todos los contenidos que se muestran en el Espacio Web y en especial, diseños, textos, imágenes, logos, etc., están sujetos a derechos de Propiedad Intelectual...</p>
<h2>5. OBLIGACIONES Y RESPONSABILIDADES DEL USUARIO DEL ESPACIO WEB</h2>
<p>El Usuario se compromete a: Hacer un uso adecuado y lícito del Espacio Web así como de los contenidos y servicios... Proveerse de todos los medios y requerimientos técnicos... Facilitar información veraz...</p>
<h2>6. RESPONSABILIDADES</h2>
<p>No se garantiza el acceso continuado, ni la correcta visualización, descarga o utilidad de los elementos e informaciones contenidas en la web que puedan verse impedidos, dificultados o interrumpidos por factores o circunstancias que están fuera de su control...</p>
<h2>7. HIPERVÍNCULOS</h2>
<p>El Usuario se obliga a no reproducir de ningún modo, ni siquiera mediante un hiperenlace o hipervínculo, el Espacio Web, salvo autorización.</p>
<h2>8. PROTECCIÓN DE DATOS</h2>
<p>Para utilizar algunos de los Servicios, el Usuario debe proporcionar previamente ciertos datos de carácter personal. La empresa tratará automatizadamente estos datos y aplicará las correspondientes medidas de seguridad, todo ello en cumplimiento del RGPD.</p>
<h2>9. COOKIES</h2>
<p>La empresa se reserva el derecho de utilizar la tecnología “cookie” en el Espacio Web, a fin de reconocerlo como Usuario frecuente y personalizar el uso que realice del Espacio Web.</p>
<h2>10. DECLARACIONES Y GARANTÍAS</h2>
<p>En general, los contenidos y servicios ofrecidos en el Espacio Web tienen carácter meramente informativo.</p>
<h2>11. FUERZA MAYOR</h2>
<p>La empresa no será responsable en todo en caso de imposibilidad de prestar servicio, si ésta se debe a supuestos de fuerza mayor o de caso fortuito.</p>
<h2>12. RESOLUCIÓN DE CONTROVERSIAS. LEY APLICABLE Y JURISDICCIÓN</h2>
<p>Las presentes Condiciones Generales de Uso, así como el uso del Espacio Web, se regirán por la legislación española. Para la resolución de cualquier controversia las partes se someterán a los Juzgados y Tribunales del domicilio social del Responsable del sitio web.</p>"""

with open('/Users/deilabel/Documents/crossBoxZuera/stitch_crossboxzuera_landing_page (1)/politica-privacidad.html', 'w', encoding='utf-8') as f:
    f.write(template.format(title="Política de Privacidad", content=privacidad))

with open('/Users/deilabel/Documents/crossBoxZuera/stitch_crossboxzuera_landing_page (1)/politica-cookies.html', 'w', encoding='utf-8') as f:
    f.write(template.format(title="Política de Cookies", content=cookies))

with open('/Users/deilabel/Documents/crossBoxZuera/stitch_crossboxzuera_landing_page (1)/aviso-legal.html', 'w', encoding='utf-8') as f:
    f.write(template.format(title="Aviso Legal", content=aviso))
