import os
from markdown import markdown
from xhtml2pdf import pisa

root = r"c:\Users\Marvin\Desktop\Knowleadgebase-Fachinformatiker-f-r-Systemintegration"
md_path = os.path.join(root, "141-Solution_Businessplan_ENHANCED.md")
pdf_path = os.path.join(root, "141-Solution_Businessplan_ENHANCED.pdf")

with open(md_path, "r", encoding="utf-8") as f:
    md_text = f.read()

html_body = markdown(md_text, extensions=["fenced_code", "tables", "toc", "attr_list"])

css = '''
@page {
  size: A4;
  margin: 30mm 25mm 35mm 25mm;
}

body {
  font-family: Verdana, Arial, sans-serif;
  color: #1a1a1a;
  line-height: 1.6;
  font-size: 11pt;
}

.cover {
  text-align: center;
  padding-top: 100px;
  padding-bottom: 120px;
  page-break-after: always;
  border-bottom: 3px solid #0b5394;
}

.cover h1 {
  font-size: 48px;
  color: #0b5394;
  margin: 0 0 12px 0;
  font-weight: 700;
}

.cover .tagline {
  font-size: 18px;
  color: #555;
  margin: 8px 0;
  font-weight: 300;
  letter-spacing: 0.5px;
}

.cover .meta {
  margin-top: 40px;
  font-size: 11pt;
  color: #666;
  line-height: 1.8;
}

.toc-page {
  page-break-after: always;
}

.toc-page h2 {
  color: #0b5394;
  border-bottom: 2px solid #0b5394;
  padding-bottom: 8px;
  margin-bottom: 20px;
}

.toc-page ul {
  list-style: none;
  padding-left: 0;
}

.toc-page li {
  margin: 6px 0;
  padding-left: 20px;
  font-size: 10pt;
}

.toc-page li:before {
  content: "·";
  margin-right: 10px;
  color: #0b5394;
}

h1 {
  font-size: 28px;
  color: #0b5394;
  margin-top: 30px;
  margin-bottom: 12px;
  border-bottom: 3px solid #0b5394;
  padding-bottom: 8px;
  page-break-after: avoid;
}

h2 {
  font-size: 18px;
  color: #0b5394;
  margin-top: 24px;
  margin-bottom: 10px;
  border-bottom: 1px solid #d0d0d0;
  padding-bottom: 6px;
  page-break-after: avoid;
}

h3 {
  font-size: 13px;
  color: #1a1a1a;
  margin-top: 16px;
  margin-bottom: 8px;
  font-weight: 700;
  page-break-after: avoid;
}

p {
  margin: 8px 0;
  text-align: justify;
}

strong { font-weight: 700; color: #0b5394; }

em { font-style: italic; color: #555; }

ul, ol {
  margin: 8px 0 8px 20px;
  padding-left: 20px;
}

li {
  margin: 4px 0;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 12px 0;
  background: #fafafa;
  font-size: 10pt;
  page-break-inside: avoid;
}

table th {
  background: #0b5394;
  color: white;
  padding: 8px 10px;
  text-align: left;
  font-weight: 700;
  border: 1px solid #0b5394;
}

table td {
  border: 1px solid #ddd;
  padding: 8px 10px;
}

table tr:nth-child(even) {
  background: #f0f4f8;
}

pre {
  background: #f0f4f8;
  border-left: 3px solid #0b5394;
  padding: 10px;
  overflow-x: auto;
  font-size: 9pt;
  margin: 10px 0;
  page-break-inside: avoid;
}

code {
  font-family: "Courier New", monospace;
  background: #f0f4f8;
  padding: 2px 4px;
  border-radius: 2px;
  color: #d63384;
}

hr {
  border: none;
  border-top: 2px solid #0b5394;
  margin: 30px 0;
  page-break-after: avoid;
}

.pagebreak {
  page-break-after: always;
}

a {
  color: #0b5394;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
'''

cover_html = '''
<div class="cover">
  <h1>141-SOLUTION</h1>
  <div class="tagline">Modulare SaaS-Suite für den Mittelstand</div>
  <div class="tagline" style="font-size: 14px;">Software. Einfach. Sicher.</div>
  <div class="meta">
    <strong>Geschäftsplan — Gründerwettbewerb 2025</strong><br/>
    Stand: Mai 2025<br/><br/>
    Gründer: Paul Buchwald, Till Hirch, Marvin Strauß, Tobias Mißbach<br/>
    <br/>
    🇩🇪 Made in Germany | 🛡️ DSGVO-konform | ⚡ Modular | 🤝 Transparent
  </div>
</div>
'''

toc_html = '''
<div class="toc-page">
  <h2>Inhaltsverzeichnis</h2>
  <ul>
    <li>EXECUTIVE SUMMARY</li>
    <li>1. MARKTANALYSE</li>
    <li style="margin-left: 20px;">1.1 Marktgröße & Potenzial</li>
    <li style="margin-left: 20px;">1.2 Markttrends & Treiber</li>
    <li style="margin-left: 20px;">1.3 Zielmarkt & Kundensegmente</li>
    <li style="margin-left: 20px;">1.4 Wettbewerbsanalyse</li>
    <li>2. GESCHÄFTSMODELL</li>
    <li style="margin-left: 20px;">2.1 Erlösmodell</li>
    <li style="margin-left: 20px;">2.2 Pricing-Strategie</li>
    <li style="margin-left: 20px;">2.3 Gewinnmargen & KPIs</li>
    <li style="margin-left: 20px;">2.4 Kundenakquisition</li>
    <li>3. PRODUKTE & DIENSTLEISTUNGEN</li>
    <li style="margin-left: 20px;">3.1 Produktportfolio</li>
    <li style="margin-left: 20px;">3.2 Entwicklungsstand & Roadmap</li>
    <li>4. TEAM & ORGANISATION</li>
    <li>5. FINANZPLANUNG</li>
    <li style="margin-left: 20px;">5.1 Finanzierungsbedarf</li>
    <li style="margin-left: 20px;">5.2 3-Jahres-Finanzprognose</li>
    <li style="margin-left: 20px;">5.3 Finanzierungsstrategie</li>
    <li>6. UMSETZUNG & STRATEGIE</li>
    <li>7. VISION & AUSBLICK</li>
    <li>8. BESONDERHEITEN & MARKENIDENTITÄT</li>
    <li>9. FINANZIERUNGSANFRAGE & NÄCHSTE SCHRITTE</li>
    <li>10. ANHANG: REGULATORISCHE ANFORDERUNGEN</li>
  </ul>
</div>
'''

full_html = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>{css}</style>
</head>
<body>
{cover_html}
{toc_html}
{html_body}
</body>
</html>'''

with open(pdf_path, "wb") as out:
    result = pisa.CreatePDF(full_html, dest=out)

if result.err:
    print(f"ERROR: {result.err}")
else:
    file_size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    print(f"✓ PDF erstellt: {pdf_path}")
    print(f"✓ Dateigröße: {file_size_mb:.2f} MB")
    print(f"✓ Features: Deckblatt, Inhaltsverzeichnis, Seitenzahlen, professionelle Formatierung")
