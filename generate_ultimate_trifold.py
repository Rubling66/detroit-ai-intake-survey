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

# Ultimate 100% Filled Heritage Trifold HTML Content
trifold_heritage_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heritage & Scripture 3-Fold Pamphlet | ISUPK Ultimate Edition</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: #090d16;
      color: #f8fafc;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem;
      gap: 2rem;
    }}

    /* 11" x 8.5" Landscape Sheet */
    .trifold-sheet {{
      width: 11in;
      height: 8.5in;
      background: #ffffff;
      color: #0f172a;
      padding: 0.22in;
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 0.22in;
      box-shadow: 0 15px 35px rgba(0,0,0,0.6);
      border-radius: 8px;
      position: relative;
      page-break-after: always;
    }}

    /* Fold Guide Lines */
    .trifold-sheet::before, .trifold-sheet::after {{
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      width: 1px;
      border-left: 1px dashed #cbd5e1;
      pointer-events: none;
    }}
    .trifold-sheet::before {{ left: 3.66in; }}
    .trifold-sheet::after {{ left: 7.33in; }}

    .panel {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 1.5px solid #cbd5e1;
      border-radius: 6px;
      padding: 0.75rem;
      background: #fff;
      font-size: 0.78rem;
      line-height: 1.4;
    }}

    .panel-cover {{
      background: linear-gradient(165deg, #1e293b 0%, #0f172a 100%);
      color: #fff;
      border-color: #f59e0b;
      text-align: center;
      justify-content: space-between;
    }}

    .cover-logo {{
      width: 70px;
      height: 70px;
      border-radius: 10px;
      border: 2px solid #f59e0b;
      margin: 0.2rem auto 0.4rem;
      box-shadow: 0 0 15px rgba(245, 158, 11, 0.4);
    }}

    .cover-title {{
      font-family: 'Cinzel', serif;
      font-size: 1.3rem;
      color: #fbbf24;
      line-height: 1.15;
      margin-bottom: 0.3rem;
      text-transform: uppercase;
    }}

    .cover-subtitle {{
      font-size: 0.75rem;
      color: #cbd5e1;
      margin-bottom: 0.5rem;
    }}

    .badge-gold {{
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid #f59e0b;
      color: #f59e0b;
      font-size: 0.62rem;
      font-weight: 800;
      padding: 0.2rem 0.5rem;
      border-radius: 9999px;
      display: inline-block;
      text-transform: uppercase;
    }}

    .panel h3 {{
      font-family: 'Cinzel', serif;
      color: #d97706;
      font-size: 0.95rem;
      margin-bottom: 0.35rem;
      border-bottom: 1.5px solid #d97706;
      padding-bottom: 0.2rem;
      text-transform: uppercase;
    }}

    .panel-image {{
      width: 100%;
      height: 95px;
      object-fit: cover;
      border-radius: 5px;
      border: 1px solid #d97706;
      margin: 0.35rem 0;
    }}

    .quote-box {{
      background: #fef3c7;
      border-left: 3px solid #d97706;
      padding: 0.4rem 0.5rem;
      margin: 0.35rem 0;
      font-style: italic;
      font-size: 0.72rem;
      color: #78350f;
    }}

    .callout-box {{
      background: #0f172a;
      color: #fff;
      padding: 0.5rem;
      border-radius: 5px;
      border-left: 3.5px solid #f59e0b;
      font-size: 0.72rem;
      margin: 0.35rem 0;
    }}

    .benefit-tag {{
      display: inline-block;
      background: #ecfdf5;
      border: 1px solid #10b981;
      color: #065f46;
      font-size: 0.68rem;
      font-weight: bold;
      padding: 2px 5px;
      border-radius: 3px;
    }}

    .loss-tag {{
      display: inline-block;
      background: #fff1f2;
      border: 1px solid #f43f5e;
      color: #881337;
      font-size: 0.68rem;
      font-weight: bold;
      padding: 2px 5px;
      border-radius: 3px;
    }}

    .print-bar {{
      position: fixed;
      top: 1rem;
      right: 1rem;
      z-index: 100;
      display: flex;
      gap: 0.5rem;
    }}

    .btn-print {{
      background: #f59e0b;
      color: #000;
      font-weight: 800;
      padding: 0.6rem 1.2rem;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(245, 158, 11, 0.4);
    }}

    @media print {{
      body {{ background: #fff; padding: 0; }}
      .trifold-sheet {{ box-shadow: none; border-radius: 0; padding: 0.2in; }}
      .print-bar {{ display: none; }}
    }}
  </style>
</head>
<body>

  <div class="print-bar">
    <button class="btn-print" onclick="window.print()">🖨️ Print 3-Fold Brochure (Landscape)</button>
    <a href="index.html" class="btn-print" style="background: #374151; color: #fff; text-decoration: none;">← All Flyers</a>
  </div>

  <div style="text-align: center; color: #cbd5e1; font-size: 0.85rem;">
    📄 <strong>SIDE 1: OUTER FLAPS</strong> (Print Double-Sided Landscape 11" x 8.5")
  </div>

  <!-- SHEET 1: OUTER SIDE (Panels 5, 6, 1) -->
  <div class="trifold-sheet">
    
    <!-- Panel 5: Inside Flap (Left When Folded) -->
    <div class="panel">
      <div>
        <h3>About The Initiative</h3>
        <p style="margin-bottom: 0.3rem;">
          The Israelite School of Universal Practical Knowledge (ISUPK) is a 501(c)(3) non-profit organization dedicated to scripture education, moral restoration, and community self-reliance.
        </p>
        <img src="{community_b64}" alt="Community Outreach Graphic" class="panel-image">
        
        <h4 style="font-family: 'Cinzel', serif; color: #d97706; font-size: 0.82rem; margin-top: 0.3rem; font-weight: bold;">3 REASONS TO GET INVOLVED NOW:</h4>
        <ol style="margin-left: 1rem; font-size: 0.72rem; margin-bottom: 0.3rem; color: #1e293b;">
          <li><strong>Reclaim Your True Identity:</strong> Stop living under assigned labels; discover your biblical heritage.</li>
          <li><strong>Protect Our Youth:</strong> Shield sons & daughters from gang culture, violence, and identity loss.</li>
          <li><strong>Build Local Self-Reliance:</strong> Support free food box drives, winter coat distribution, and mentorship in Flint & Saginaw.</li>
        </ol>

        <div class="quote-box">
          "Proclaim liberty throughout all the land unto all the inhabitants thereof..." — Leviticus 25:10
        </div>
      </div>

      <div style="background: #0f172a; color: #fff; padding: 0.4rem; border-radius: 4px; border-left: 3px solid #f59e0b; font-size: 0.7rem;">
        <strong>POWERFUL STATEMENT:</strong> "A community that does not know its true history is easily divided. Truth restores unity."
      </div>
    </div>

    <!-- Panel 6: Back Cover (Middle When Folded) -->
    <div class="panel">
      <div>
        <h3 style="text-align: center;">THE STAKES: WHO BENEFITS & WHO LOSES</h3>
        
        <div style="margin-bottom: 0.4rem;">
          <span class="benefit-tag">✓ WHO BENEFITS:</span>
          <ul style="font-size: 0.72rem; margin-left: 1rem; margin-top: 0.2rem; color: #1e293b;">
            <li><strong>Our Youth:</strong> Gain moral discipline, self-respect, and spiritual guidance.</li>
            <li><strong>Our Families:</strong> Restored through scriptural marriage principles and fatherhood.</li>
            <li><strong>Our Communities:</strong> Strengthened through food drives and local brotherhood.</li>
          </ul>
        </div>

        <div style="margin-bottom: 0.4rem;">
          <span class="loss-tag">✗ WHO LOSES:</span>
          <ul style="font-size: 0.72rem; margin-left: 1rem; margin-top: 0.2rem; color: #881337;">
            <li><strong>Street Crime & Addiction:</strong> Broken when individuals embrace scriptural health and brotherhood.</li>
            <li><strong>Systemic Ignorance:</strong> Overcome by reclaiming true biblical heritage.</li>
          </ul>
        </div>

        <div style="text-align: center; border-top: 1px solid #e2e8f0; padding-top: 0.4rem;">
          <img src="{logo_b64}" alt="ISUPK Emblem" style="width: 48px; height: 48px; border-radius: 6px; margin: 0.2rem auto; border: 1px solid #d97706;">
          <p style="font-weight: bold; font-size: 0.8rem; margin-bottom: 0.15rem;">Michigan Regional Hub</p>
          <p style="font-size: 0.72rem; color: #475569;">
            16134 Moross Rd, Detroit, MI 48205 | 📞 267-353-6021<br>
            🌐 <strong>isupk.com</strong> | Info Kit: <strong>http://localhost:8080/contact.html</strong>
          </p>
        </div>
      </div>

      <div style="border-top: 1px solid #e2e8f0; padding-top: 0.3rem; font-size: 0.65rem; color: #64748b; text-align: center;">
        © 2026 ISUPK 501(c)(3) Non-Profit Organization. All Rights Reserved.
      </div>
    </div>

    <!-- Panel 1: Front Cover (Right When Folded) -->
    <div class="panel panel-cover">
      <div>
        <span class="badge-gold">501(c)(3) Non-Profit Educational Series</span>
        <img src="{logo_b64}" alt="ISUPK Logo" class="cover-logo">
        <h2 class="cover-title">RESTORING IDENTITY & SCRIPTURE</h2>
        <p class="cover-subtitle">Heritage & Biblical Lineage Pamphlet for Mid-Michigan Communities</p>
        <img src="{tribes_b64}" alt="12 Tribes Chart Cover Graphic" style="width: 100%; height: 100px; object-fit: cover; border-radius: 6px; border: 1px solid #f59e0b; margin-bottom: 0.4rem;">
      </div>

      <div style="background: rgba(255,255,255,0.08); padding: 0.4rem; border-radius: 6px; font-size: 0.7rem;">
        <strong>POWERFUL STATEMENT:</strong><br>
        "You are not a byword. You are the descendants of biblical royalty."
      </div>
    </div>

  </div>

  <div style="text-align: center; color: #cbd5e1; font-size: 0.85rem;">
    📄 <strong>SIDE 2: INSIDE PANELS</strong> (Panels 2, 3, 4)
  </div>

  <!-- SHEET 2: INSIDE PANELS (Panels 2, 3, 4) -->
  <div class="trifold-sheet">

    <!-- Panel 2: Inside Left Column -->
    <div class="panel">
      <div>
        <h3>12 Tribes Scriptural Lineage</h3>
        <p style="margin-bottom: 0.3rem;">
          Scripture teaches that African American, Hispanic, and Native American peoples are the descendants of the Twelve Tribes of Israel.
        </p>
        <img src="{tribes_b64}" alt="12 Tribes Chart Illustration" class="panel-image">
        
        <div class="callout-box">
          <strong>PROPHETIC PROOFS IN SCRIPTURE:</strong>
          <ul style="margin-left: 0.8rem; margin-top: 0.2rem; font-size: 0.7rem;">
            <li><strong>Deut 28:68:</strong> Captivity by ships fulfilling transatlantic slave trade.</li>
            <li><strong>Deut 28:48:</strong> Yokes of iron upon the neck during colonial bondage.</li>
            <li><strong>Deut 28:37:</strong> Called by proverbs and bywords ("Negro", "Latino", "Indian").</li>
          </ul>
        </div>
      </div>

      <div class="quote-box">
        "Hear, LORD, the voice of Judah, and bring him unto his people..." — Deuteronomy 33:7
      </div>
    </div>

    <!-- Panel 3: Inside Center Column -->
    <div class="panel">
      <div>
        <h3>WHY IT MATTERS — THE COVENANT</h3>
        <p style="margin-bottom: 0.3rem;">
          Decades of poverty, incarceration, broken homes, and lost identity in urban centers are not accidental—they are scriptural consequences.
        </p>
        
        <div style="background: #fef3c7; border: 1px solid #d97706; padding: 0.45rem; border-radius: 5px; font-size: 0.72rem; margin: 0.3rem 0;">
          <strong style="color: #78350f;">WHY THIS MATTERS FOR YOUR FAMILY:</strong><br>
          True restoration does not come from political promises or empty slogans, but from returning to moral righteousness, divine commandments, and brotherhood.
        </div>

        <div class="callout-box">
          📜 <strong>16-PAGE PROPHECY STUDY BOOKLET:</strong><br>
          Request physical study booklets mailed directly to your home at <strong>isupk.com</strong> or <strong>http://localhost:8080/resources.html</strong>.
        </div>
      </div>

      <div style="background: #f8fafc; padding: 0.4rem; border-radius: 4px; border: 1px solid #e2e8f0; font-size: 0.7rem; text-align: center;">
        <strong>Free Info Kit Request:</strong> Call 📞 <strong>267-353-6021</strong>
      </div>
    </div>

    <!-- Panel 4: Inside Right Column -->
    <div class="panel">
      <div>
        <h3>HOW TO TAKE ACTION TODAY</h3>
        
        <div style="font-size: 0.73rem; margin-bottom: 0.4rem;">
          <p style="font-weight: bold; color: #d97706;">1. ATTEND OUR FLINT STREET TABLE</p>
          <p style="color: #475569;">Saturdays 1:00–4:00 PM | S. Saginaw St & E. 2nd St</p>

          <p style="font-weight: bold; color: #d97706; margin-top: 0.3rem;">2. JOIN LIVE ZOOM BIBLE CLASS</p>
          <p style="color: #475569;">Tuesdays & Thursdays 7:00 PM EST</p>

          <p style="font-weight: bold; color: #d97706; margin-top: 0.3rem;">3. VOLUNTEER FOR AID DRIVES</p>
          <p style="color: #475569;">3rd Sunday Monthly | Riverbank Park, Flint</p>
        </div>

        <img src="{community_b64}" alt="Community Support Illustration" style="width: 100%; height: 70px; object-fit: cover; border-radius: 4px; border: 1px solid #d97706;">
      </div>

      <div style="background: #0f172a; color: #fff; padding: 0.45rem; border-radius: 4px; text-align: center; font-size: 0.7rem; margin-top: 0.2rem;">
        📱 <strong>Register Online for Info Kit:</strong><br>
        <strong>http://localhost:8080/contact.html</strong>
      </div>
    </div>

  </div>

</body>
</html>
'''

with open(os.path.join(base_dir, "flyers", "trifold_heritage.html"), "w", encoding="utf-8") as f:
    f.write(trifold_heritage_html)

print("Generated Ultimate 100% Filled Heritage Trifold HTML.")
