#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for AGRILEAD Training & Consulting LLC.
Writes English-only HTML pages sharing a common header/footer.
All contact details use [Phone] / [Email] / [Website] placeholders
until final details are confirmed, per the brand handoff."""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ---- Shared bits -----------------------------------------------------------

BRAND = (
    '<a class="brand" href="index.html" aria-label="AGRILEAD Training and Consulting home">'
    '<svg class="mark" viewBox="0 0 64 64" width="32" height="32" aria-hidden="true">'
    '<rect width="64" height="64" rx="13" fill="#0D2B4D"/>'
    '<path d="M32 50V30" fill="none" stroke="#F3F4F6" stroke-width="3.4" stroke-linecap="round"/>'
    '<path d="M32 34c-9 0-15-4-16-13 9-1 15 3 16 13z" fill="#2E7D32"/>'
    '<path d="M32 30c7-1 12-5 13-12-7 0-12 3-13 12z" fill="#4a9d4e"/>'
    '<path d="M18 50h28" fill="none" stroke="#7A4E24" stroke-width="3.4" stroke-linecap="round"/>'
    '</svg>'
    '<span class="brand-word">AGRI<span class="lead">LEAD</span></span>'
    '</a>'
)

# icon helpers (inline line icons, one family, stroke = currentColor)
# Intrinsic width/height act as a safety net: if the stylesheet ever fails
# to load, the icons stay small instead of expanding to fill the page.
def ic(path):
    return ('<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" '
            'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">' + path + '</svg>')

ICONS = {
    "leaf":   ic('<path d="M11 20A7 7 0 0 1 4 13c0-6 8-9 15-9-1 8-4 16-8 16z"/><path d="M4 13c4-1 7-2 9-5"/>'),
    "book":   ic('<path d="M4 5a2 2 0 0 1 2-2h6v16H6a2 2 0 0 0-2 2z"/><path d="M20 5a2 2 0 0 0-2-2h-6v16h6a2 2 0 0 1 2 2z"/>'),
    "sprout": ic('<path d="M12 21v-8"/><path d="M12 13c-4 0-6-2-6-6 4 0 6 2 6 6z"/><path d="M12 11c3 0 5-2 5-5-3 0-5 2-5 5z"/>'),
    "globe":  ic('<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a15 15 0 0 1 0 18 15 15 0 0 1 0-18z"/>'),
    "group":  ic('<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 6a3 3 0 0 1 0 6"/><path d="M21 20a5 5 0 0 0-4-5"/>'),
    "soil":   ic('<path d="M4 16h16"/><path d="M4 20h16"/><path d="M12 12V6"/><path d="M12 8c-3 0-4-1-4-4 3 0 4 1 4 4z"/>'),
    "climate":ic('<circle cx="12" cy="9" r="3.2"/><path d="M12 2v2M12 14v2M5 9H3M21 9h-2M6.5 3.5 8 5M17.5 3.5 16 5"/><path d="M4 20h16"/>'),
    "doc":    ic('<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/><path d="M9 13h6M9 17h6"/>'),
    "wrench": ic('<path d="M14 6a3.5 3.5 0 0 0 4.5 4.5L21 13l-8 8-2.5-2.5A3.5 3.5 0 0 0 6 14L3 11l3-3 2.5 2.5A3.5 3.5 0 0 0 12 3.5z"/>'),
    "chart":  ic('<path d="M4 20V4"/><path d="M4 20h16"/><path d="M8 16v-4M12 16V8M16 16v-6"/>'),
    "chat":   ic('<path d="M20 15a2 2 0 0 1-2 2H8l-4 4V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2z"/>'),
    "hands":  ic('<path d="M8 13 4 9a2 2 0 0 1 3-3l3 3"/><path d="m16 13 4-4a2 2 0 0 0-3-3l-3 3"/><path d="M8 13v4a3 3 0 0 0 3 3h2a3 3 0 0 0 3-3v-4"/>'),
    "check":  ic('<path d="m20 6-11 11-5-5"/>'),
    "phone":  ic('<path d="M5 3h3l2 5-2 1a11 11 0 0 0 5 5l1-2 5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/>'),
    "mail":   ic('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>'),
    "pin":    ic('<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>'),
    "arrow":  ic('<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>'),
    "compass":ic('<circle cx="12" cy="12" r="9"/><path d="m15 9-2 6-4 0 2-6z" fill="currentColor" stroke="none"/><path d="m15 9-6 2"/>'),
    "shield": ic('<path d="M12 3 5 6v5c0 5 3 8 7 10 4-2 7-5 7-10V6z"/><path d="m9 12 2 2 4-4"/>'),
    "list":   ic('<path d="M8 6h13M8 12h13M8 18h13"/><path d="M3 6h.01M3 12h.01M3 18h.01"/>'),
}

def field_panel(caption="Field-based agricultural training", ratio_class="", note="Photo"):
    """Signature soil-horizon / crop-row motif used where a real photo will go."""
    svg = '''<svg viewBox="0 0 400 320" width="400" height="320" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#123a63"/><stop offset="1" stop-color="#0D2B4D"/>
    </linearGradient>
    <linearGradient id="fieldg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3a8f3e"/><stop offset="1" stop-color="#2E7D32"/>
    </linearGradient>
  </defs>
  <rect width="400" height="320" fill="url(#sky)"/>
  <circle cx="322" cy="70" r="30" fill="#e9c46a" opacity=".85"/>
  <path d="M0 150 Q100 118 200 138 T400 132 V210 H0 Z" fill="url(#fieldg)"/>
  <path d="M0 150 Q100 118 200 138 T400 132" fill="none" stroke="#4aa14e" stroke-width="2" opacity=".6"/>
  <g stroke="#256a29" stroke-width="2" opacity=".55">
    <path d="M40 210 L80 158"/><path d="M110 210 L140 152"/><path d="M190 210 L205 150"/>
    <path d="M270 210 L262 150"/><path d="M350 210 L322 154"/>
  </g>
  <rect y="205" width="400" height="115" fill="#7A4E24"/>
  <rect y="205" width="400" height="115" fill="url(#fieldg)" opacity="0"/>
  <g stroke="#5f3c1c" stroke-width="2" opacity=".7">
    <path d="M0 232 H400"/><path d="M0 260 H400"/><path d="M0 288 H400"/>
  </g>
  <g fill="none" stroke="#8fd18f" stroke-width="2.4" stroke-linecap="round" opacity=".95">
    <path d="M120 150 v-20"/><path d="M120 138 c-6 0-9-3-9-9 6 0 9 3 9 9z" fill="#8fd18f" stroke="none"/>
    <path d="M210 148 v-22"/><path d="M210 134 c6 0 9-3 9-9 -6 0-9 3-9 9z" fill="#b7e4b8" stroke="none"/>
    <path d="M298 150 v-18"/><path d="M298 140 c-6 0-9-3-9-9 6 0 9 3 9 9z" fill="#8fd18f" stroke="none"/>
  </g>
</svg>'''
    return (f'<div class="field-panel {ratio_class}">{svg}'
            f'<span class="photo-note">{note}</span>'
            f'<span class="panel-caption">{caption}</span></div>')

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("signature-initiative.html", "Signature Initiative"),
    ("collaboration-opportunities.html", "Collaboration"),
    ("contact.html", "Contact"),
]

def header(active):
    links = ""
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ""
        links += f'<a href="{href}"{cur}>{label}</a>'
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    {BRAND}
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="primary-nav">
      {ICONS["list"]}
    </button>
    <nav class="nav" id="primary-nav" aria-label="Primary">
      {links}
      <a class="btn btn--primary" href="collaboration-opportunities.html">Discuss a Potential Collaboration</a>
    </nav>
    <div class="header-actions">
      <a class="btn btn--primary" href="collaboration-opportunities.html">Discuss a Potential Collaboration</a>
    </div>
  </div>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        {BRAND}
        <p class="footer-tag">Practical Training for Resilient Agriculture</p>
        <p class="footer-desc">AGRILEAD Training &amp; Consulting LLC is a Florida-based agricultural training and consulting company focused on practical agricultural education, applied agronomy support, bilingual outreach, technical assistance, curriculum development, and farmer capacity-building.</p>
      </div>
      <div class="footer">
        <h4>Quick links</h4>
        <ul class="footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="signature-initiative.html">Signature Initiative</a></li>
          <li><a href="collaboration-opportunities.html">Collaboration Opportunities</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer">
        <h4>Contact</h4>
        <ul class="footer-contact">
          <li>{ICONS["phone"]}<span>[Phone]</span></li>
          <li>{ICONS["mail"]}<span>[Email]</span></li>
          <li>{ICONS["globe"]}<span>[Website]</span></li>
          <li>{ICONS["pin"]}<span>Naples, Florida, United States</span></li>
        </ul>
      </div>
    </div>
    <p class="footer-disclaimer">Potential collaboration does not imply a confirmed partnership unless formally documented. AGRILEAD is not presenting itself as an official representative, affiliate, or partner of any public agency, university, Extension office, or external institution unless such a relationship is formally documented in writing.</p>
    <div class="footer-bottom">
      <p>&copy; <span id="year">2025</span> AGRILEAD Training &amp; Consulting LLC. All rights reserved.</p>
      <p><a href="privacy.html">Privacy Policy</a></p>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
<script>document.getElementById("year").textContent = new Date().getFullYear();</script>'''

def page(filename, title, description, active, main_html):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Lato:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
{header(active)}
<main id="main">
{main_html}
</main>
{FOOTER}
</body>
</html>'''
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)

# ---------------------------------------------------------------------------
# Reusable content blocks
# ---------------------------------------------------------------------------

VALUES = [
    ("leaf",  "Practical Knowledge", "Clear, useful, field-oriented learning."),
    ("group", "Farmer-Centered Training", "Training adapted to producer needs and realities."),
    ("shield","Integrity", "Professional, transparent, and responsible communication."),
    ("globe", "Inclusion &amp; Language Access", "Support for bilingual and multilingual learning."),
    ("soil",  "Sustainability", "Emphasis on soil health, resilience, and long-term farm viability."),
]

def values_block():
    out = '<div class="values">'
    for icon, title, desc in VALUES:
        out += (f'<div class="value"><span class="icon">{ICONS[icon]}</span>'
                f'<div><h4>{title}</h4><p>{desc}</p></div></div>')
    out += '</div>'
    return out

WHO_WE_SERVE = [
    "Beginning farmers", "Small-scale producers", "Immigrant &amp; multilingual producers",
    "Haitian / Creole-speaking communities", "Hispanic agricultural communities",
    "Underserved rural communities", "Farmworker communities", "Producer groups",
    "Agricultural nonprofits", "Community-based organizations", "Training stakeholders",
]

def pills_block(items):
    return '<div class="pills">' + "".join(f'<span class="pill">{i}</span>' for i in items) + '</div>'

DISCLAIMER_COLLAB = (
    'AGRILEAD Training &amp; Consulting LLC is available to discuss potential collaboration '
    'opportunities with agricultural organizations, community-based institutions, producer groups, '
    'and training stakeholders. Any collaboration would be subject to each organization&rsquo;s policies, '
    'priorities, resources, timelines, and formal agreements. References to potential collaboration do '
    'not imply confirmed partnership, endorsement, funding, contract, official affiliation, or guaranteed '
    'results unless documented in writing.'
)
print("blocks ready")
