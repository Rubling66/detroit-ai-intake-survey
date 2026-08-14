import base64
import os

base_dir = r"c:\Users\Admin\Desktop\detroit_ai_intake_survey"

def get_base64_img(rel_path):
    full_path = os.path.join(base_dir, rel_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode('utf-8')
            ext = os.path.splitext(full_path)[1].lower().replace('.', '')
            mime = 'image/jpeg' if ext in ['jfif', 'jpg', 'jpeg'] else 'image/png'
            return f"data:{mime};base64,{encoded}"
    return ""

logo_b64 = get_base64_img("assets/logo.jfif")
tribes_b64 = get_base64_img("assets/tribes_chart.jpg")
community_b64 = get_base64_img("assets/community_graphic.jpg")

# Ultimate Spanish Trifold
trifold_spanish_html = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Folleto Tríptico en Español | ISUPK Edición Especial</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; background: #090d16; color: #f8fafc; display: flex; flex-direction: column; align-items: center; padding: 2rem; gap: 2rem; }}
    .trifold-sheet {{ width: 11in; height: 8.5in; background: #ffffff; color: #0f172a; padding: 0.22in; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.22in; box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-radius: 8px; position: relative; page-break-after: always; }}
    .trifold-sheet::before, .trifold-sheet::after {{ content: ''; position: absolute; top: 0; bottom: 0; width: 1px; border-left: 1px dashed #cbd5e1; pointer-events: none; }}
    .trifold-sheet::before {{ left: 3.66in; }} .trifold-sheet::after {{ left: 7.33in; }}
    .panel {{ display: flex; flex-direction: column; justify-content: space-between; border: 1.5px solid #cbd5e1; border-radius: 6px; padding: 0.75rem; background: #fff; font-size: 0.78rem; line-height: 1.4; }}
    .panel-cover {{ background: linear-gradient(165deg, #064e3b 0%, #022c22 100%); color: #fff; border-color: #10b981; text-align: center; justify-content: space-between; }}
    .cover-logo {{ width: 70px; height: 70px; border-radius: 10px; border: 2px solid #10b981; margin: 0.2rem auto 0.4rem; box-shadow: 0 0 15px rgba(16, 185, 129, 0.4); }}
    .cover-title {{ font-family: 'Cinzel', serif; font-size: 1.3rem; color: #10b981; line-height: 1.15; margin-bottom: 0.3rem; text-transform: uppercase; }}
    .cover-subtitle {{ font-size: 0.75rem; color: #cbd5e1; margin-bottom: 0.5rem; }}
    .badge-emerald {{ background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #10b981; font-size: 0.62rem; font-weight: 800; padding: 0.2rem 0.5rem; border-radius: 9999px; display: inline-block; text-transform: uppercase; }}
    .panel h3 {{ font-family: 'Cinzel', serif; color: #059669; font-size: 0.95rem; margin-bottom: 0.35rem; border-bottom: 1.5px solid #059669; padding-bottom: 0.2rem; text-transform: uppercase; }}
    .panel-image {{ width: 100%; height: 95px; object-fit: cover; border-radius: 5px; border: 1px solid #059669; margin: 0.35rem 0; }}
    .quote-box {{ background: #ecfdf5; border-left: 3px solid #059669; padding: 0.4rem 0.5rem; margin: 0.35rem 0; font-style: italic; font-size: 0.72rem; color: #065f46; }}
    .callout-box {{ background: #022c22; color: #fff; padding: 0.5rem; border-radius: 5px; border-left: 3.5px solid #10b981; font-size: 0.72rem; margin: 0.35rem 0; }}
    .benefit-tag {{ display: inline-block; background: #ecfdf5; border: 1px solid #10b981; color: #065f46; font-size: 0.68rem; font-weight: bold; padding: 2px 5px; border-radius: 3px; }}
    .loss-tag {{ display: inline-block; background: #fff1f2; border: 1px solid #f43f5e; color: #881337; font-size: 0.68rem; font-weight: bold; padding: 2px 5px; border-radius: 3px; }}
    .print-bar {{ position: fixed; top: 1rem; right: 1rem; z-index: 100; display: flex; gap: 0.5rem; }}
    .btn-print {{ background: #10b981; color: #000; font-weight: 800; padding: 0.6rem 1.2rem; border: none; border-radius: 6px; cursor: pointer; }}
    @media print {{ body {{ background: #fff; padding: 0; }} .trifold-sheet {{ box-shadow: none; border-radius: 0; padding: 0.2in; }} .print-bar {{ display: none; }} }}
  </style>
</head>
<body>
  <div class="print-bar">
    <button class="btn-print" onclick="window.print()">🖨️ Imprimir Tríptico en Español</button>
    <a href="index.html" class="btn-print" style="background: #374151; color: #fff; text-decoration: none;">← Todos los Folletos</a>
  </div>

  <div style="text-align: center; color: #cbd5e1; font-size: 0.85rem;">
    📄 <strong>LADO 1: PANELES EXTERIORES</strong> (Imprimir Horizontal Doble Cara 11" x 8.5")
  </div>

  <div class="trifold-sheet">
    <div class="panel">
      <div>
        <h3>Sobre Nuestra Iniciativa</h3>
        <p style="margin-bottom: 0.3rem;">La Escuela Israelita de Conocimiento Práctico Universal (ISUPK) es una organización 501(c)(3) sin fines de lucro dedicada a la educación bíblica y al fortalecimiento familiar.</p>
        <img src="{community_b64}" alt="Gráfico Comunitario" class="panel-image">
        <h4 style="font-family: 'Cinzel', serif; color: #059669; font-size: 0.82rem; margin-top: 0.3rem; font-weight: bold;">RAZONES PARA PARTICIPAR:</h4>
        <ol style="margin-left: 1rem; font-size: 0.72rem; margin-bottom: 0.3rem; color: #1e293b;">
          <li><strong>Descubra su Identidad Bíblica:</strong> Conozca sus raíces bíblicas históricas.</li>
          <li><strong>Proteja a la Juventud:</strong> Ofrezca disciplina moral y valores a nuestros jóvenes.</li>
          <li><strong>Apoyo a la Comunidad:</strong> Participación en entregas de alimentos y abrigos.</li>
        </ol>
        <div class="quote-box">"Proclamaréis libertad en la tierra a todos sus moradores..." — Levítico 25:10</div>
      </div>
      <div style="background: #022c22; color: #fff; padding: 0.4rem; border-radius: 4px; border-left: 3px solid #10b981; font-size: 0.7rem;">
        <strong>DECLARACIÓN PODEROSA:</strong> "Una comunidad que conoce su historia no puede ser dividida. La verdad restaura la unidad."
      </div>
    </div>

    <div class="panel">
      <div>
        <h3 style="text-align: center;">QUIÉN SE BENEFICIA Y QUIÉN PIERDE</h3>
        <div style="margin-bottom: 0.4rem;">
          <span class="benefit-tag">✓ QUIÉN SE BENEFICIA:</span>
          <ul style="font-size: 0.72rem; margin-left: 1rem; margin-top: 0.2rem; color: #1e293b;">
            <li><strong>Nuestros Jóvenes:</strong> Obtienen disciplina moral y respeto familiar.</li>
            <li><strong>Nuestras Familias:</strong> Restauradas mediante principios bíblicos del hogar.</li>
            <li><strong>Comunidades de Flint y Saginaw:</strong> Fortalecidas mediante ayuda mutua.</li>
          </ul>
        </div>
        <div style="margin-bottom: 0.4rem;">
          <span class="loss-tag">✗ QUIÉN PIERDE:</span>
          <ul style="font-size: 0.72rem; margin-left: 1rem; margin-top: 0.2rem; color: #881337;">
            <li><strong>La Delincuencia y Adicciones:</strong> Derrotadas cuando se adopta la hermandad y salud.</li>
            <li><strong>La Ignorancia Histórica:</strong> Superada al recuperar la herencia bíblica.</li>
          </ul>
        </div>
        <div style="text-align: center; border-top: 1px solid #e2e8f0; padding-top: 0.4rem;">
          <img src="{logo_b64}" alt="Logo ISUPK" style="width: 48px; height: 48px; border-radius: 6px; margin: 0.2rem auto; border: 1px solid #059669;">
          <p style="font-weight: bold; font-size: 0.8rem; margin-bottom: 0.15rem;">Sede Regional de Michigan</p>
          <p style="font-size: 0.72rem; color: #475569;">16134 Moross Rd, Detroit, MI 48205 | 📞 267-353-6021<br>🌐 <strong>isupk.com</strong> | Registro: <strong>http://localhost:8080/contact.html</strong></p>
        </div>
      </div>
      <div style="border-top: 1px solid #e2e8f0; padding-top: 0.3rem; font-size: 0.65rem; color: #64748b; text-align: center;">© 2026 Organización ISUPK 501(c)(3). Todos los derechos reservados.</div>
    </div>

    <div class="panel panel-cover">
      <div>
        <span class="badge-emerald">Serie Educativa 501(c)(3)</span>
        <img src="{logo_b64}" alt="Logo ISUPK" class="cover-logo">
        <h2 class="cover-title">RESTAURANDO LA FE Y LA FAMILIA</h2>
        <p class="cover-subtitle">Guía de Estudio Bíblico e Identidad Histórica para las Familias Hispanas e Indígenas</p>
        <img src="{tribes_b64}" alt="Gráfico de las 12 Tribus" style="width: 100%; height: 100px; object-fit: cover; border-radius: 6px; border: 1px solid #10b981; margin-bottom: 0.4rem;">
      </div>
      <div style="background: rgba(255,255,255,0.08); padding: 0.4rem; border-radius: 6px; font-size: 0.7rem;">
        <strong>DECLARACIÓN PODEROSA:</strong><br>"Usted no es una etiqueta impuesta. Es descendiente de una gran herencia bíblica."
      </div>
    </div>
  </div>

  <div style="text-align: center; color: #cbd5e1; font-size: 0.85rem;">
    📄 <strong>LADO 2: PANELES INTERIORES</strong> (Paneles 2, 3, 4)
  </div>

  <div class="trifold-sheet">
    <div class="panel">
      <div>
        <h3>Las Tribus del Norte</h3>
        <p style="margin-bottom: 0.3rem;">Las Escrituras revelan la conexión bíblica e histórica de los pueblos hispanos e indígenas de América con las diez tribus del Norte de Israel.</p>
        <img src="{tribes_b64}" alt="Mapa de las Tribus" class="panel-image">
        <div class="callout-box">
          <strong>PRUEBAS BÍBLICAS HISTÓRICAS:</strong>
          <ul style="margin-left: 0.8rem; margin-top: 0.2rem; font-size: 0.7rem;">
            <li><strong>2 Esdras 13:40-45:</strong> Migración de las 10 tribus a las Américas (Arsareth).</li>
            <li><strong>Deut 33:17:</strong> La bendición sobre Efraín y Manasés en las Américas.</li>
            <li><strong>Génesis 49:19:</strong> La perseverancia histórica de la tribu de Gad.</li>
          </ul>
        </div>
      </div>
      <div class="quote-box">"Aquellas son las diez tribus llevadas cautivas..." — 2 Esdras 13:40-41</div>
    </div>

    <div class="panel">
      <div>
        <h3>POR QUÉ IMPORTA PARA SU HOGAR</h3>
        <p style="margin-bottom: 0.3rem;">Nuestra misión comunitaria busca fortalecer las familias, alejar a los jóvenes de la violencia y restaurar la dignidad moral.</p>
        <div style="background: #ecfdf5; border: 1px solid #10b981; padding: 0.45rem; border-radius: 5px; font-size: 0.72rem; margin: 0.3rem 0;">
          <strong style="color: #065f46;">EL PROPÓSITO:</strong><br>La verdadera restauración familiar se logra al retornar a la rectitud moral, los mandamientos de Dios y el respeto mutuo.
        </div>
        <div class="callout-box">
          📜 <strong>GUÍA EDUCATIVA GRATUITA EN ESPAÑOL:</strong><br>Solicite folletos impresos por correo en <strong>isupk.com</strong> o <strong>http://localhost:8080/resources.html</strong>.
        </div>
      </div>
      <div style="background: #f8fafc; padding: 0.4rem; border-radius: 4px; border: 1px solid #e2e8f0; font-size: 0.7rem; text-align: center;">
        <strong>Información Telefónica:</strong> 📞 <strong>267-353-6021</strong>
      </div>
    </div>

    <div class="panel">
      <div>
        <h3>CÓMO PARTICIPAR HOY</h3>
        <div style="font-size: 0.73rem; margin-bottom: 0.4rem;">
          <p style="font-weight: bold; color: #059669;">1. MESA INFORMATIVA EN FLINT</p>
          <p style="color: #475569;">Sábados 1:00–4:00 PM | Centro de Flint (S. Saginaw St)</p>
          <p style="font-weight: bold; color: #059669; margin-top: 0.3rem;">2. CLASE BÍBLICA VIRTUAL</p>
          <p style="color: #475569;">Martes y Jueves 7:00 PM EST (Zoom / Webcast)</p>
          <p style="font-weight: bold; color: #059669; margin-top: 0.3rem;">3. ENTREGA DE ALIMENTOS</p>
          <p style="color: #475569;">Tercer Domingo del Mes | Riverbank Park, Flint</p>
        </div>
        <img src="{community_b64}" alt="Gráfico de Apoyo Comunitario" style="width: 100%; height: 70px; object-fit: cover; border-radius: 4px; border: 1px solid #059669;">
      </div>
      <div style="background: #022c22; color: #fff; padding: 0.45rem; border-radius: 4px; text-align: center; font-size: 0.7rem; margin-top: 0.2rem;">
        📱 <strong>Registro en Línea:</strong><br><strong>http://localhost:8080/contact.html</strong>
      </div>
    </div>
  </div>
</body>
</html>
'''

with open(os.path.join(base_dir, "flyers", "trifold_spanish.html"), "w", encoding="utf-8") as f:
    f.write(trifold_spanish_html)

print("Generated Ultimate 100% Filled Spanish Trifold HTML.")
