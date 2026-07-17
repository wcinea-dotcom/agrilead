#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for AGRILEAD Training & Consulting LLC.
Bilingual (English + French). English pages live in public/, French pages in
public/fr/. A language switcher (EN/FR) and hreflang tags link the two.
All contact details use <a href="tel:+17863937333">+1 (786) 393 7333</a> / <a href="mailto:ingwilbert@agrileadtraining.com">ingwilbert@agrileadtraining.com</a> / <a href="https://www.agrileadtraining.com">www.agrileadtraining.com</a> placeholders
until final details are confirmed, per the brand handoff."""

import os
import time

# Bump ASSET_VER whenever CSS/JS changes — it cache-busts the year-long
# immutable asset cache so returning visitors get the new styles.
ASSET_VER = "20260702g"

# Supported languages: English (root), French (/fr/), Spanish (/es/).
LANGS = ("en", "fr", "es")
LANG_DIR = {"en": "", "fr": "fr/", "es": "es/"}
LANG_LABEL = {"en": "English", "fr": "Français", "es": "Español"}

# When AGRI_COLLECT is set, page() collects (target, bytes) here instead of writing.
_PENDING = []


def url_for(cur, target, filename):
    """Relative URL to `target` language's copy of `filename`, from a page in `cur`."""
    if target == cur:
        return filename
    up = "" if cur == "en" else "../"
    return up + LANG_DIR[target] + filename


# The publishable site lives in public/ (Netlify's publish directory).
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
for _d in LANG_DIR.values():
    os.makedirs(os.path.join(OUT, _d) if _d else OUT, exist_ok=True)

# ---- Shared bits -----------------------------------------------------------

BRAND = (
    '<a class="brand" href="index.html" aria-label="AGRILEAD Training and Consulting home">'
    '<img class="brand-logo" src="/assets/img/logo.png" alt="AGRILEAD Training &amp; Consulting" width="330" height="97">'
    '</a>'
)

# icon helpers (inline line icons, one family, stroke = currentColor)
def ic(path):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
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

def field_panel(caption="Field-based agricultural training", ratio_class="", note="Photo", img="", alt=""):
    """Signature soil-horizon / crop-row motif used where a real photo will go.
    If img (a URL) is provided, a real photo is rendered instead of the SVG placeholder."""
    if img:
        return (f'<div class="field-panel {ratio_class}">'
                f'<img src="{img}" alt="{alt or caption}" loading="lazy" decoding="async">'
                f'<span class="panel-caption">{caption}</span></div>')
    svg = '''<svg viewBox="0 0 400 320" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
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

# ---- Translatable chrome (header / footer / meta) --------------------------

TR = {
    "en": {
        "html_lang": "en",
        "skip": "Skip to content",
        "menu": "Open menu",
        "nav_aria": "Primary",
        "nav_tree": [
            ("index.html", "Home", [
                ("about.html", "About"),
                ("collaboration-opportunities.html", "Collaboration"),
            ]),
            ("services.html", "Services", [
                ("signature-initiative.html", "Signature Initiative"),
            ]),
            ("blog.html", "Media", [
                ("blog.html", "Blog"),
            ]),
            ("contact.html", "Contact", []),
        ],
        "cta": "Discuss a Potential Collaboration",
        "switch_label": "FR",
        "switch_aria": "Passer en français",
        "foot_tag": "Practical Agricultural Training for Resilient Communities",
        "foot_desc": ("AGRILEAD Training &amp; Consulting LLC is a Florida-based agricultural training and "
                      "consulting company focused on practical agricultural education, applied agronomy support, "
                      "bilingual outreach, technical assistance, curriculum development, and farmer capacity-building."),
        "foot_quick": "Quick links",
        "foot_quick_links": [
            ("index.html", "Home"),
            ("about.html", "About"),
            ("services.html", "Services"),
            ("signature-initiative.html", "Signature Initiative"),
            ("collaboration-opportunities.html", "Collaboration Opportunities"),
            ("blog.html", "Blog"),
            ("contact.html", "Contact"),
        ],
        "foot_contact": "Contact",
        "foot_loc": "Naples, Florida, United States",
        "foot_disclaimer": ("Potential collaboration does not imply a confirmed partnership unless formally documented. "
                            "AGRILEAD is not presenting itself as an official representative, affiliate, or partner of any "
                            "public agency, university, Extension office, or external institution unless such a relationship "
                            "is formally documented in writing."),
        "rights": "All rights reserved.",
        "privacy": "Privacy Policy",
    },
    "fr": {
        "html_lang": "fr",
        "skip": "Aller au contenu",
        "menu": "Ouvrir le menu",
        "nav_aria": "Navigation principale",
        "nav_tree": [
            ("index.html", "Accueil", [
                ("about.html", "À propos"),
                ("collaboration-opportunities.html", "Collaboration"),
            ]),
            ("services.html", "Services", [
                ("signature-initiative.html", "Initiative phare"),
            ]),
            ("blog.html", "Médias", [
                ("blog.html", "Blog"),
            ]),
            ("contact.html", "Contact", []),
        ],
        "cta": "Discuter d'une collaboration",
        "switch_label": "EN",
        "switch_aria": "Switch to English",
        "foot_tag": "Formation agricole pratique pour des communautés résilientes",
        "foot_desc": ("AGRILEAD Training &amp; Consulting LLC est une société de formation et de conseil agricoles "
                      "basée en Floride, axée sur l'éducation agricole pratique, l'appui en agronomie appliquée, la "
                      "sensibilisation bilingue, l'assistance technique, l'élaboration de programmes et le renforcement "
                      "des capacités des agriculteurs."),
        "foot_quick": "Liens rapides",
        "foot_quick_links": [
            ("index.html", "Accueil"),
            ("about.html", "À propos"),
            ("services.html", "Services"),
            ("signature-initiative.html", "Initiative phare"),
            ("collaboration-opportunities.html", "Opportunités de collaboration"),
            ("blog.html", "Blog"),
            ("contact.html", "Contact"),
        ],
        "foot_contact": "Contact",
        "foot_loc": "Naples, Floride, États-Unis",
        "foot_disclaimer": ("Une collaboration potentielle n'implique pas un partenariat confirmé sauf accord formel écrit. "
                            "AGRILEAD ne se présente pas comme représentant officiel, affilié ou partenaire d'une agence "
                            "publique, d'une université, d'un service de vulgarisation (Extension) ou d'une institution "
                            "externe, sauf si une telle relation est formellement documentée par écrit."),
        "rights": "Tous droits réservés.",
        "privacy": "Politique de confidentialité",
    },
    "es": {
        "html_lang": "es",
        "skip": "Ir al contenido",
        "menu": "Abrir el menú",
        "nav_aria": "Principal",
        "nav_tree": [
            ("index.html", "Inicio", [
                ("about.html", "Acerca de"),
                ("collaboration-opportunities.html", "Colaboración"),
            ]),
            ("services.html", "Servicios", [
                ("signature-initiative.html", "Iniciativa insignia"),
            ]),
            ("blog.html", "Medios", [
                ("blog.html", "Blog"),
            ]),
            ("contact.html", "Contacto", []),
        ],
        "cta": "Hablar de una posible colaboración",
        "foot_tag": "Formación agrícola práctica para comunidades resilientes",
        "foot_desc": ("AGRILEAD Training &amp; Consulting LLC es una empresa de formación y consultoría "
                      "agrícola con sede en Florida, enfocada en la educación agrícola práctica, el apoyo en "
                      "agronomía aplicada, la divulgación bilingüe, la asistencia técnica, el desarrollo de "
                      "programas y el fortalecimiento de capacidades de los agricultores."),
        "foot_quick": "Enlaces rápidos",
        "foot_quick_links": [
            ("index.html", "Inicio"),
            ("about.html", "Acerca de"),
            ("services.html", "Servicios"),
            ("signature-initiative.html", "Iniciativa insignia"),
            ("collaboration-opportunities.html", "Oportunidades de colaboración"),
            ("blog.html", "Blog"),
            ("contact.html", "Contacto"),
        ],
        "foot_contact": "Contacto",
        "foot_loc": "Naples, Florida, Estados Unidos",
        "foot_disclaimer": ("Una posible colaboración no implica una alianza confirmada salvo acuerdo formal por "
                            "escrito. AGRILEAD no se presenta como representante oficial, afiliado o socio de ninguna "
                            "agencia pública, universidad, oficina de extensión (Extension) o institución externa, "
                            "salvo que dicha relación esté formalmente documentada por escrito."),
        "rights": "Todos los derechos reservados.",
        "privacy": "Política de privacidad",
    },
}


def _nav_links(t, active):
    out = ""
    for href, label, children in t["nav_tree"]:
        child_hrefs = [c[0] for c in children]
        is_active = (href == active) or (active in child_hrefs)
        cur = ' aria-current="page"' if is_active else ""
        if children:
            subs = ""
            for ch, cl in children:
                ccur = ' aria-current="page"' if ch == active else ""
                subs += f'<a href="{ch}"{ccur}>{cl}</a>'
            out += (f'<div class="nav-item has-sub">'
                    f'<a class="nav-top" href="{href}"{cur}>{label}'
                    f'<span class="caret" aria-hidden="true">&#9662;</span></a>'
                    f'<div class="submenu">{subs}</div></div>')
        else:
            out += f'<a class="nav-top" href="{href}"{cur}>{label}</a>'
    return out


def lang_toggle(lang, filename):
    """Language toggle: globe + English | Français | Español (nature.org style)."""
    parts = []
    for code in LANGS:
        cls = ' class="is-active"' if code == lang else ""
        url = url_for(lang, code, filename)
        parts.append(f'<a href="{url}"{cls} hreflang="{code}">{LANG_LABEL[code]}</a>')
    links = '<span class="sep">|</span>'.join(parts)
    return f'<div class="lang-toggle">{ICONS["globe"]}{links}</div>'


def header(active, lang, filename):
    t = TR[lang]
    links = _nav_links(t, active)
    return f'''<a class="skip-link" href="#main">{t["skip"]}</a>
<div class="topbar">
  <div class="container topbar-inner">
    {lang_toggle(lang, filename)}
  </div>
</div>
<header class="site-header">
  <div class="container header-inner">
    {BRAND}
    <nav class="nav" id="primary-nav" aria-label="{t["nav_aria"]}">
      {links}
      <div class="nav-lang">{lang_toggle(lang, filename)}</div>
    </nav>
    <div class="header-actions">
      <button class="nav-toggle" aria-label="{t["menu"]}" aria-expanded="false" aria-controls="primary-nav">
        {ICONS["list"]}
      </button>
    </div>
  </div>
</header>'''


def footer(lang, prefix):
    t = TR[lang]
    quick = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in t["foot_quick_links"])
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        {BRAND}
        <p class="footer-tag">{t["foot_tag"]}</p>
        <p class="footer-desc">{t["foot_desc"]}</p>
      </div>
      <div class="footer">
        <h4>{t["foot_quick"]}</h4>
        <ul class="footer-links">
          {quick}
        </ul>
      </div>
      <div class="footer">
        <h4>{t["foot_contact"]}</h4>
        <ul class="footer-contact">
          <li>{ICONS["phone"]}<span><a href="tel:+17863937333">+1 (786) 393 7333</a></span></li>
          <li>{ICONS["mail"]}<span><a href="mailto:ingwilbert@agrileadtraining.com">ingwilbert@agrileadtraining.com</a></span></li>
          <li>{ICONS["globe"]}<span><a href="https://www.agrileadtraining.com">www.agrileadtraining.com</a></span></li>
          <li>{ICONS["pin"]}<span>{t["foot_loc"]}</span></li>
        </ul>
      </div>
    </div>
    <p class="footer-disclaimer">{t["foot_disclaimer"]}</p>
    <div class="footer-bottom">
      <p>&copy; <span id="year">2025</span> AGRILEAD Training &amp; Consulting LLC. {t["rights"]}</p>
      <p><a href="privacy.html">{t["privacy"]}</a></p>
    </div>
  </div>
</footer>
<script src="{prefix}assets/js/main.js?v={ASSET_VER}"></script>
<script>document.getElementById("year").textContent = new Date().getFullYear();</script>'''


def page(filename, title, description, active, main_html, lang="en"):
    t = TR[lang]
    prefix = "" if lang == "en" else "../"
    outdir = os.path.join(OUT, LANG_DIR[lang]) if LANG_DIR[lang] else OUT
    # Alternate-language URLs (relative) for hreflang
    hl = [f'<link rel="alternate" hreflang="{code}" href="{url_for(lang, code, filename)}">'
          for code in LANGS]
    hl.append(f'<link rel="alternate" hreflang="x-default" href="{url_for(lang, "en", filename)}">')
    hreflang = "\n  ".join(hl)
    html = f'''<!DOCTYPE html>
<html lang="{t["html_lang"]}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  {hreflang}
  <link rel="icon" type="image/svg+xml" href="{prefix}assets/img/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Lato:wght@400;700&family=Merriweather:wght@400;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}assets/css/styles.css?v={ASSET_VER}">
</head>
<body>
{header(active, lang, filename)}
<main id="main">
{main_html}
</main>
{footer(lang, prefix)}
</body>
</html>'''
    target = os.path.join(outdir, filename)
    data = html.encode("utf-8")
    if os.environ.get("AGRI_COLLECT"):
        _PENDING.append((target, data))
        return
    for attempt in range(4):
        try:
            fd = os.open(target, os.O_WRONLY | os.O_CREAT, 0o644)
            try:
                os.write(fd, data)
                os.ftruncate(fd, len(data))
            finally:
                os.close(fd)
            break
        except OSError:
            time.sleep(0.4)
    else:
        print("LOCKED (skipped):", lang, filename)
        return
    print("wrote", lang, filename)


# ---------------------------------------------------------------------------
# Reusable content blocks (data passed in per language)
# ---------------------------------------------------------------------------

def values_block(values):
    out = '<div class="values">'
    for icon, title, desc in values:
        out += (f'<div class="value"><span class="icon">{ICONS[icon]}</span>'
                f'<div><h4>{title}</h4><p>{desc}</p></div></div>')
    out += '</div>'
    return out


def pills_block(items):
    return '<div class="pills">' + "".join(f'<span class="pill">{i}</span>' for i in items) + '</div>'


print("blocks ready")
