#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds the AGRILEAD site pages using shared components in _build_base."""
from _build_base import (
    page, field_panel, values_block, pills_block, ICONS,
    WHO_WE_SERVE, DISCLAIMER_COLLAB,
)

A = "index.html"

def cards3(items):
    out = '<div class="grid grid-3">'
    for icon, title, body in items:
        out += (f'<article class="card reveal"><span class="icon">{ICONS[icon]}</span>'
                f'<h3>{title}</h3><p>{body}</p></article>')
    out += '</div>'
    return out

def notice(text):
    return f'<div class="notice reveal">{text}</div>'

# ===========================================================================
# HOME
# ===========================================================================
home = f'''
<section class="hero">
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Naples, Florida &middot; Agricultural Training</p>
      <h1>Practical Agricultural Training for Resilient Producers</h1>
      <p class="hero-lead">AGRILEAD Training &amp; Consulting LLC provides practical agricultural training, applied agronomy support, bilingual outreach, and farmer capacity-building for beginning farmers, small-scale producers, multilingual producers, and underserved agricultural communities.</p>
      <div class="hero-cta">
        <a class="btn btn--primary" href="collaboration-opportunities.html">Discuss a Potential Collaboration {ICONS["arrow"]}</a>
        <a class="btn btn--secondary" href="services.html">Explore Services</a>
      </div>
      <div class="hero-meta">
        <div>{ICONS["pin"]}<span>Based in Naples, Florida</span></div>
        <div>{ICONS["globe"]}<span>Bilingual &amp; multilingual outreach</span></div>
        <div>{ICONS["sprout"]}<span>Field-oriented, practical learning</span></div>
      </div>
    </div>
    <div class="hero-visual">{field_panel("Field-based farmer training session", img="https://images.pexels.com/photos/30822728/pexels-photo-30822728.jpeg?auto=compress&cs=tinysrgb&w=1400", alt="Lush garden pathway with green plants")}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Who we are</p>
      <h2>Practical, field-oriented agricultural learning</h2>
    </div>
    <div class="grid grid-2">
      <p class="reveal">AGRILEAD Training &amp; Consulting LLC is based in Naples, Florida, United States. The company is designed to support accessible, practical, and field-oriented agricultural learning through training, technical assistance, curriculum development, bilingual outreach, and community-centered capacity-building.</p>
      <p class="reveal">AGRILEAD focuses on helping producers, organizations, and training stakeholders discuss practical learning needs in areas such as soil health, crop diversification, climate-smart agriculture, applied agronomy, and farmer-centered education.</p>
    </div>
  </div>
</section>

<section class="section section--field">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">What we do</p>
      <h2>Core areas of support</h2>
    </div>
    {cards3([
      ("book","Agricultural Training","Practical workshops, short courses, and learning activities designed to support farmer knowledge and field-level skills."),
      ("sprout","Applied Agronomy Support","Technical guidance related to soil health, crop production, crop diversification, sustainable practices, and climate-smart agriculture."),
      ("globe","Bilingual &amp; Multilingual Outreach","Training materials and outreach designed to improve language access for Haitian/Creole-speaking, Hispanic, immigrant, and multilingual producer communities."),
    ])}
    <div style="margin-top:2rem" class="reveal"><a class="link-arrow" href="services.html">See all services {ICONS["arrow"]}</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Who we serve</p>
      <h2>Designed for producers and the organizations that support them</h2>
      <p>AGRILEAD is designed to serve a range of producers, community groups, and training stakeholders.</p>
    </div>
    <div class="reveal">{pills_block(WHO_WE_SERVE)}</div>
  </div>
</section>

<section class="section section--field">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;gap:clamp(2rem,5vw,4rem)">
      <div class="reveal">
        <p class="eyebrow">Our approach</p>
        <h2>Practical, participatory, and adaptable</h2>
        <p>AGRILEAD uses a practical, participatory, field-oriented, and adaptable approach. Training activities may include workshops, technical sessions, farmer handouts, curriculum support, needs assessment, train-the-trainer activities, and pilot learning discussions.</p>
        <p>The company emphasizes practical knowledge, language access, sustainability, collaboration, responsible documentation, and farmer-centered learning.</p>
      </div>
      <div class="reveal">{values_block()}</div>
    </div>
  </div>
</section>

<section class="section band">
  <div class="container band-grid">
    <div class="reveal">
      <p class="eyebrow">Signature initiative</p>
      <h2>AgriLead Bilingual Agricultural Workforce &amp; Extension Training Initiative</h2>
      <p>A developing initiative focused on practical agricultural training, bilingual outreach, technical assistance, and capacity-building for beginning farmers, small-scale producers, immigrant and multilingual producers, and underserved agricultural communities.</p>
      <div class="hero-cta">
        <a class="btn btn--ghost-light" href="signature-initiative.html">Learn about the initiative {ICONS["arrow"]}</a>
      </div>
    </div>
    <ul class="mini-list reveal">
      <li>{ICONS["check"]}Soil health &amp; applied agronomy workshops</li>
      <li>{ICONS["check"]}Bilingual farmer handouts &amp; learning resources</li>
      <li>{ICONS["check"]}Train-the-trainer &amp; community outreach</li>
      <li>{ICONS["check"]}Needs assessment &amp; pilot training discussions</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Downloadable materials</p>
      <h2>Informational overviews</h2>
      <p>These materials are informational only. They do not represent confirmed partnerships, endorsements, funding, contracts, official affiliations, or guaranteed results.</p>
    </div>
    <div class="grid grid-3">
      <div class="doc-card reveal"><span class="icon icon--navy">{ICONS["doc"]}</span><h3>One-Page Project Summary</h3><p>A concise overview of the initiative, target audiences, training areas, and potential outreach discussion topics.</p><a class="link-arrow" href="#" aria-disabled="true">Download &mdash; coming soon</a></div>
      <div class="doc-card reveal"><span class="icon icon--navy">{ICONS["doc"]}</span><h3>Company Brochure</h3><p>A brief institutional brochure presenting the company, services, approach, and contact information.</p><a class="link-arrow" href="#" aria-disabled="true">Download &mdash; coming soon</a></div>
      <div class="doc-card reveal"><span class="icon icon--navy">{ICONS["doc"]}</span><h3>Signature Initiative Overview</h3><p>A short introduction to the AgriLead Bilingual Agricultural Workforce and Extension Training Initiative.</p><a class="link-arrow" href="#" aria-disabled="true">Download &mdash; coming soon</a></div>
    </div>
  </div>
</section>

<section class="section section--field cta-strip">
  <div class="container">
    <p class="eyebrow" style="justify-content:center">Collaboration</p>
    <h2>Interested in practical agricultural training?</h2>
    <p class="narrow" style="margin-inline:auto">AGRILEAD is available to discuss potential collaboration opportunities with agricultural organizations, producer groups, community-based institutions, and training stakeholders.</p>
    <div class="hero-cta">
      <a class="btn btn--primary" href="collaboration-opportunities.html">Discuss a Potential Collaboration</a>
      <a class="btn btn--secondary" href="contact.html">Contact AGRILEAD</a>
    </div>
  </div>
</section>
'''

page("index.html",
     "AGRILEAD Training & Consulting LLC | Agricultural Training in Florida",
     "AGRILEAD Training & Consulting LLC provides practical agricultural training, applied agronomy support, bilingual outreach, technical assistance, and farmer capacity-building services.",
     A, home)

# ===========================================================================
# ABOUT
# ===========================================================================
about = f'''
<section class="section section--tight">
  <div class="container">
    <p class="eyebrow reveal">About AGRILEAD</p>
    <h1 class="reveal" style="max-width:16ch">Practical, farmer-centered agricultural learning</h1>
    <p class="hero-lead reveal" style="max-width:60ch">AGRILEAD Training &amp; Consulting LLC is a Florida-based agricultural training and consulting company focused on practical education, applied agronomy, bilingual outreach, technical assistance, curriculum development, and producer capacity-building.</p>
  </div>
</section>

<section class="section section--field">
  <div class="container grid grid-2" style="gap:clamp(2rem,5vw,4rem)">
    <div class="reveal">
      <h2>About the company</h2>
      <p>AGRILEAD Training &amp; Consulting LLC is based in Naples, Florida, United States. The company supports practical, field-oriented agricultural learning for farmers, producer groups, community-based organizations, and agricultural stakeholders.</p>
      <p>Its work focuses on applied agronomy, technical assistance, bilingual and multilingual outreach, curriculum development, training materials, and farmer capacity-building &mdash; designed to make agricultural knowledge more accessible, practical, and adaptable to producer and community needs.</p>
    </div>
    <div class="reveal">{field_panel("Agricultural learning setting", img="https://images.pexels.com/photos/27176769/pexels-photo-27176769.jpeg?auto=compress&cs=tinysrgb&w=1400", alt="Hands planting seedlings in a garden")}</div>
  </div>
</section>

<section class="section">
  <div class="container grid grid-2" style="gap:1.4rem">
    <article class="card reveal"><span class="icon">{ICONS["compass"]}</span><h3>Mission</h3><p>AGRILEAD Training &amp; Consulting LLC provides practical, field-oriented agricultural training and applied agronomy support to strengthen the capacity of beginning farmers, small-scale producers, and underserved agricultural communities through bilingual and multilingual education focused on sustainability, productivity, and resilience.</p></article>
    <article class="card reveal"><span class="icon icon--navy">{ICONS["sprout"]}</span><h3>Vision</h3><p>To contribute to stronger agricultural communities where beginning farmers, small-scale producers, and underserved growers have access to practical knowledge, technical support, and adaptable training models that support local and regional food systems.</p></article>
  </div>
</section>

<section class="section section--field">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Core values</p><h2>What guides our work</h2></div>
    <div class="reveal">{values_block()}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Founder</p><h2>Founder profile</h2></div>
    <div class="founder">
      <div class="reveal">{field_panel("Founder portrait", note="Replace with photo")}</div>
      <div class="reveal">
        <h3>Wilbert Georges</h3>
        <p class="role">Founder &amp; Executive Lead</p>
        <p>Wilbert Georges is the Founder and Executive Lead of AGRILEAD Training &amp; Consulting LLC. He is an agricultural development professional with experience in farmer training, applied agronomy, rural capacity-building, climate-smart agriculture, cooperative strengthening, and agricultural project implementation.</p>
        <p>His work has focused on supporting producer groups and rural communities through practical training, multilingual communication, and field-oriented capacity-building. Through AGRILEAD, he is developing a professional platform to support agricultural training, bilingual outreach, technical assistance, and curriculum development.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--field cta-strip">
  <div class="container">
    <h2>Learn about our services</h2>
    <div class="hero-cta">
      <a class="btn btn--primary" href="services.html">Explore Services</a>
      <a class="btn btn--secondary" href="contact.html">Contact AGRILEAD</a>
    </div>
  </div>
</section>
'''

page("about.html",
     "About AGRILEAD Training & Consulting LLC",
     "Learn about AGRILEAD Training & Consulting LLC, a Florida-based agricultural training and consulting company supporting practical farmer education and bilingual outreach.",
     "about.html", about)

# ===========================================================================
# SERVICES
# ===========================================================================
SERVICES = [
    ("book","Agricultural Training","Workshops, short courses, and field-oriented learning activities for farmers, producer groups, and community-based organizations."),
    ("sprout","Applied Agronomy Support","Guidance on crop production, soil fertility, crop management, and sustainable agricultural practices."),
    ("soil","Soil Health &amp; Fertility Education","Training on organic matter, composting, nutrient management, soil conservation, and basic fertility planning."),
    ("leaf","Crop Diversification","Educational support for diversified production, farm planning, risk reduction, and sustainable crop systems."),
    ("climate","Climate-Smart Agriculture","Training and discussion topics related to climate adaptation, resource stewardship, and resilient production practices."),
    ("wrench","Technical Assistance","Support for agricultural organizations, producer groups, and community-based initiatives seeking practical agricultural guidance."),
    ("globe","Bilingual &amp; Multilingual Training Materials","Farmer handouts, outreach tools, workshop materials, and practical learning resources designed to support language access."),
    ("group","Train-the-Trainer Support","Capacity-building for facilitators, community leaders, and agricultural outreach workers."),
    ("doc","Curriculum Development","Training modules, lesson plans, facilitator guides, and farmer education materials."),
    ("chart","Monitoring, Evaluation &amp; Learning","Basic tools to document training activities, gather feedback, and support learning improvement."),
]

svc_items = ""
for icon, title, body in SERVICES:
    svc_items += (f'<div class="svc-item reveal"><span class="icon">{ICONS[icon]}</span>'
                  f'<div><h3>{title}</h3><p>{body}</p></div></div>')

services = f'''
<section class="section section--tight">
  <div class="container">
    <p class="eyebrow reveal">Services</p>
    <h1 class="reveal" style="max-width:18ch">Agricultural training and consulting services</h1>
    <p class="hero-lead reveal" style="max-width:60ch">AGRILEAD provides practical agricultural training, applied agronomy support, technical assistance, curriculum development, and bilingual outreach services for producers and organizations.</p>
  </div>
</section>

<section class="section section--field section--tight">
  <div class="container narrow">
    <p class="reveal" style="margin:0">AGRILEAD&rsquo;s services are designed to support practical learning, technical guidance, and producer capacity-building. Services may be adapted based on organizational needs, available resources, and agreed scope of work.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Core services</p><h2>Areas of support available for discussion</h2></div>
    <div class="svc">{svc_items}</div>
  </div>
</section>

<section class="section section--field">
  <div class="container">{notice('<strong>Please note.</strong> Services may include the areas above and are available to discuss depending on scope and resources. Descriptions do not imply confirmed partnership, funding, contract, official affiliation, or guaranteed results unless documented in writing.')}</div>
</section>

<section class="section cta-strip">
  <div class="container">
    <h2>Request a services discussion</h2>
    <div class="hero-cta">
      <a class="btn btn--primary" href="collaboration-opportunities.html">Discuss a Potential Collaboration</a>
      <a class="btn btn--secondary" href="contact.html">Contact AGRILEAD</a>
    </div>
  </div>
</section>
'''

page("services.html",
     "Agricultural Training and Consulting Services | AGRILEAD",
     "AGRILEAD offers agricultural training, applied agronomy support, soil health education, bilingual materials, technical assistance, and curriculum development.",
     "services.html", services)

# ===========================================================================
# SIGNATURE INITIATIVE
# ===========================================================================
BENEFICIARIES = [
    "Beginning farmers", "Small-scale producers", "Immigrant &amp; multilingual producers",
    "Haitian / Creole-speaking communities", "Hispanic agricultural communities",
    "Underserved rural communities", "Farmworker communities", "Producer groups",
    "Community-based organizations",
]
ACTIVITIES = [
    ("soil","Soil health training"),
    ("sprout","Applied agronomy workshops"),
    ("leaf","Crop diversification sessions"),
    ("climate","Climate-smart agriculture learning"),
    ("globe","Bilingual farmer handouts"),
    ("group","Train-the-trainer support"),
    ("chat","Community outreach"),
    ("list","Needs assessment"),
    ("book","Pilot training discussions"),
]
act_cards = '<div class="grid grid-3">'
for icon, label in ACTIVITIES:
    act_cards += f'<div class="card reveal" style="padding:1.3rem 1.4rem"><span class="icon" style="width:40px;height:40px;margin-bottom:.7rem">{ICONS[icon]}</span><h3 style="font-size:1.02rem;margin:0">{label}</h3></div>'
act_cards += '</div>'

initiative = f'''
<section class="section section--tight">
  <div class="container">
    <p class="eyebrow reveal">Signature initiative &middot; Developing</p>
    <h1 class="reveal">AgriLead Bilingual Agricultural Workforce &amp; Extension Training Initiative</h1>
    <p class="hero-lead reveal" style="max-width:62ch">A developing initiative designed to support practical agricultural training, bilingual outreach, technical assistance, and farmer capacity-building.</p>
  </div>
</section>

<section class="section section--field">
  <div class="container grid grid-2" style="gap:clamp(2rem,5vw,4rem)">
    <div class="reveal">
      <p class="eyebrow">Purpose</p>
      <h2>Practical, language-accessible learning</h2>
      <p>The AgriLead Bilingual Agricultural Workforce and Extension Training Initiative is a developing initiative focused on supporting beginning farmers, small-scale producers, immigrant and multilingual producers, and underserved agricultural communities through practical training and language-accessible learning resources.</p>
      <p>Its purpose is to support practical agricultural education, applied agronomy learning, bilingual outreach, and producer capacity-building.</p>
    </div>
    <div class="reveal">{field_panel("Multilingual farmer education", img="https://images.pexels.com/photos/9890612/pexels-photo-9890612.jpeg?auto=compress&cs=tinysrgb&w=1400", alt="Garden path between green plants and flowers")}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Target beneficiaries</p><h2>Who the initiative is designed for</h2></div>
    <div class="reveal">{pills_block(BENEFICIARIES)}</div>
  </div>
</section>

<section class="section section--field">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Potential activities</p><h2>What the initiative may include</h2></div>
    {act_cards}
  </div>
</section>

<section class="section">
  <div class="container grid grid-2" style="gap:clamp(2rem,5vw,4rem);align-items:center">
    <div class="reveal">
      <p class="eyebrow">Training model</p>
      <h2>A flexible, modular platform</h2>
      <p>The initiative is designed as a flexible and modular training platform. Materials and activities may be adapted based on audience needs, language access, geographic context, agricultural priorities, available resources, and agreed scope of work.</p>
    </div>
    <div class="reveal">{notice('<strong>Important note.</strong> This initiative does not imply confirmed partnerships, endorsements, funding, contracts, official affiliations, or guaranteed results unless documented in writing. Any collaboration would be subject to organizational policies, priorities, resources, timelines, and formal agreements.')}</div>
  </div>
</section>

<section class="section band cta-strip">
  <div class="container">
    <h2>Discuss a potential training activity</h2>
    <div class="hero-cta">
      <a class="btn btn--ghost-light" href="collaboration-opportunities.html">Discuss a Potential Collaboration</a>
      <a class="btn btn--ghost-light" href="contact.html">Contact AGRILEAD</a>
    </div>
  </div>
</section>
'''

page("signature-initiative.html",
     "AgriLead Bilingual Agricultural Workforce and Extension Training Initiative",
     "Learn about AGRILEAD's developing initiative focused on bilingual agricultural training, applied agronomy, technical assistance, and farmer capacity-building.",
     "signature-initiative.html", initiative)

# ===========================================================================
# COLLABORATION OPPORTUNITIES
# ===========================================================================
COLLAB = [
    ("doc","Curriculum Review","Reviewing or providing feedback on practical agricultural training content."),
    ("book","Workshop Design","Discussing possible training topics, formats, and audience needs."),
    ("chat","Community Outreach Support","Exploring ways to communicate agricultural education opportunities to multilingual producer communities."),
    ("sprout","Technical Feedback","Discussing applied agronomy topics such as soil health, crop diversification, climate-smart practices, and producer capacity-building."),
    ("group","Train-the-Trainer Discussions","Exploring whether local facilitators, community leaders, or agricultural outreach workers may benefit from structured learning support."),
    ("list","Needs Assessment","Identifying training needs, language-access barriers, and practical learning priorities for producer groups."),
    ("hands","Pilot Training Discussions","Exploring whether a small-scale training session or learning activity may be appropriate, subject to organizational resources and formal arrangements."),
]
collab_items = ""
for icon, title, body in COLLAB:
    collab_items += (f'<div class="svc-item reveal"><span class="icon">{ICONS[icon]}</span>'
                     f'<div><h3>{title}</h3><p>{body}</p></div></div>')

FOR_WHOM = [
    "Beginning farmer programs", "Small-scale producer groups", "Agricultural nonprofits",
    "Community-based organizations", "Farmworker &amp; rural community organizations",
    "Training institutions", "Producer associations", "Groups serving multilingual producers",
    "Haitian/Creole-speaking communities", "Hispanic agricultural communities",
]

collaboration = f'''
<section class="section section--tight">
  <div class="container">
    <p class="eyebrow reveal">Collaboration</p>
    <h1 class="reveal">Collaboration opportunities</h1>
    <p class="hero-lead reveal" style="max-width:60ch">Explore potential training, outreach, and technical assistance opportunities with AGRILEAD Training &amp; Consulting LLC.</p>
  </div>
</section>

<section class="section section--field">
  <div class="container narrow">
    <p class="eyebrow reveal">A professional platform</p>
    <h2 class="reveal">Available to discuss practical agricultural learning</h2>
    <p class="reveal">AGRILEAD Training &amp; Consulting LLC is available to discuss potential collaboration opportunities with agricultural organizations, community-based institutions, producer groups, and training stakeholders interested in practical agricultural education, applied agronomy support, bilingual outreach, and farmer capacity-building.</p>
    <p class="reveal">Any collaboration would be subject to organizational policies, priorities, resources, timelines, and formal agreements.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Who this page is for</p><h2>Organizations and groups we may work with</h2>
    <p>This page is intended for organizations and groups that may be interested in practical agricultural training, technical assistance, bilingual outreach, or farmer-centered learning.</p></div>
    <div class="reveal">{pills_block(FOR_WHOM)}</div>
  </div>
</section>

<section class="section section--field">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">Potential collaboration opportunities</p><h2>Ways to explore working together</h2></div>
    <div class="svc">{collab_items}</div>
  </div>
</section>

<section class="section">
  <div class="container">{notice('<strong>Important note on collaboration.</strong> Potential collaboration does not imply confirmed partnership, endorsement, funding, contract, official affiliation, or guaranteed results unless documented in writing. AGRILEAD is not presenting itself as an official representative, affiliate, or partner of any public agency, university, Extension office, nonprofit organization, or external institution unless such relationship is formally documented.')}</div>
</section>

<section class="section section--field cta-strip">
  <div class="container">
    <h2>Discuss a potential collaboration</h2>
    <div class="hero-cta">
      <a class="btn btn--primary" href="contact.html">Submit an Inquiry</a>
      <a class="btn btn--secondary" href="contact.html">Contact AGRILEAD</a>
    </div>
  </div>
</section>
'''

page("collaboration-opportunities.html",
     "Collaboration Opportunities | AGRILEAD Training & Consulting LLC",
     "Explore potential collaboration opportunities with AGRILEAD in agricultural training, applied agronomy support, bilingual outreach, technical assistance, and farmer capacity-building.",
     "collaboration-opportunities.html", collaboration)

# ===========================================================================
# CONTACT  (Netlify Forms)
# ===========================================================================
INQUIRY_TOPICS = [
    "Agricultural training", "Applied agronomy support", "Soil health education",
    "Crop diversification", "Climate-smart agriculture", "Technical assistance",
    "Bilingual outreach", "Curriculum development", "Train-the-trainer support",
    "Potential collaboration opportunities",
]
ORG_TYPES = ["Agricultural organization","Community-based organization","Producer group",
             "Training institution","Farmworker or rural community organization","Small farm program","Other"]
AREAS = ["Agricultural Training","Applied Agronomy Support","Soil Health Education","Crop Diversification",
         "Climate-Smart Agriculture","Bilingual Outreach","Curriculum Development","Train-the-Trainer",
         "Technical Assistance","Potential Collaboration","Other"]

def options(items):
    return "".join(f'<option value="{i}">{i}</option>' for i in items)

topics_list = "".join(f'<li>{ICONS["check"]}<span>{t}</span></li>' for t in INQUIRY_TOPICS)

contact = f'''
<section class="section section--tight">
  <div class="container">
    <p class="eyebrow reveal">Contact</p>
    <h1 class="reveal">Contact AGRILEAD Training &amp; Consulting LLC</h1>
    <p class="hero-lead reveal" style="max-width:62ch">AGRILEAD is available to discuss potential training, technical assistance, curriculum development, bilingual outreach, and collaboration opportunities.</p>
  </div>
</section>

<section class="section">
  <div class="container contact-grid">
    <div class="reveal">
      <h2 style="font-size:1.35rem">Contact information</h2>
      <div class="info-row"><span class="icon icon--navy">{ICONS["pin"]}</span><div><p class="label">Location</p><p class="val">Naples, Florida, United States</p></div></div>
      <div class="info-row"><span class="icon icon--navy">{ICONS["phone"]}</span><div><p class="label">Phone</p><p class="val">[Phone]</p></div></div>
      <div class="info-row"><span class="icon icon--navy">{ICONS["mail"]}</span><div><p class="label">Email</p><p class="val">[Email]</p></div></div>
      <div class="info-row"><span class="icon icon--navy">{ICONS["globe"]}</span><div><p class="label">Website</p><p class="val">[Website]</p></div></div>

      <h3 style="margin-top:2rem;font-size:1.1rem">Inquiry topics</h3>
      <ul class="footer-contact" style="gap:.55rem;margin-top:.8rem">{topics_list}</ul>
    </div>

    <div class="reveal">
      <h2 style="font-size:1.35rem">Send an inquiry</h2>
      <!-- Netlify Forms: this works automatically once deployed to Netlify.
           No backend needed. Submissions appear in the Netlify dashboard. -->
      <form class="form" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/thank-you.html">
        <input type="hidden" name="form-name" value="contact">
        <p class="hp"><label>Do not fill this out: <input name="bot-field"></label></p>

        <div class="form-row">
          <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" required></div>
          <div class="field"><label for="org">Organization <span class="opt">(optional)</span></label><input id="org" name="organization" type="text"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="role">Role / Title <span class="opt">(optional)</span></label><input id="role" name="role" type="text"></div>
          <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="phone">Phone <span class="opt">(optional)</span></label><input id="phone" name="phone" type="tel"></div>
          <div class="field"><label for="location">Location <span class="opt">(optional)</span></label><input id="location" name="location" type="text"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="orgtype">Type of organization</label><select id="orgtype" name="organization_type"><option value="" selected disabled>Select one</option>{options(ORG_TYPES)}</select></div>
          <div class="field"><label for="area">Area of interest</label><select id="area" name="area_of_interest"><option value="" selected disabled>Select one</option>{options(AREAS)}</select></div>
        </div>
        <div class="field"><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
        <div class="field"><label for="followup">Preferred follow-up method <span class="opt">(optional)</span></label><select id="followup" name="preferred_followup"><option value="" selected disabled>Select one</option><option>Email</option><option>Phone</option><option>No preference</option></select></div>

        <button class="btn btn--primary" type="submit">Submit an Inquiry</button>
        <p class="form-note">Submitting an inquiry does not create a partnership, contract, funding commitment, or formal affiliation.</p>
      </form>
    </div>
  </div>
</section>
'''

page("contact.html",
     "Contact AGRILEAD Training & Consulting LLC",
     "Contact AGRILEAD Training & Consulting LLC to discuss potential agricultural training, applied agronomy, bilingual outreach, technical assistance, or curriculum development opportunities.",
     "contact.html", contact)

# ===========================================================================
# THANK YOU (form redirect target)
# ===========================================================================
thankyou = f'''
<section class="section" style="min-height:52vh;display:flex;align-items:center">
  <div class="container narrow center">
    <span class="icon" style="width:64px;height:64px;margin-inline:auto">{ICONS["check"]}</span>
    <h1 style="margin-top:1.2rem">Thank you &mdash; your inquiry was received</h1>
    <p>We appreciate your message. AGRILEAD will review your inquiry and follow up as appropriate. Submitting an inquiry does not create a partnership, contract, funding commitment, or formal affiliation.</p>
    <div class="hero-cta" style="justify-content:center">
      <a class="btn btn--primary" href="index.html">Back to Home</a>
      <a class="btn btn--secondary" href="services.html">Explore Services</a>
    </div>
  </div>
</section>
'''
page("thank-you.html",
     "Thank You | AGRILEAD Training & Consulting LLC",
     "Your inquiry to AGRILEAD Training & Consulting LLC has been received.",
     "", thankyou)

# ===========================================================================
# PRIVACY POLICY (recommended addition)
# ===========================================================================
privacy = f'''
<section class="section section--tight">
  <div class="container narrow">
    <p class="eyebrow">Privacy</p>
    <h1>Privacy Policy</h1>
    <p class="form-note">Last updated: <span id="pdate"></span>. This is a general template and should be reviewed for accuracy before final publication.</p>

    <h3 style="margin-top:2rem">Information we collect</h3>
    <p>When you submit the contact form on this website, AGRILEAD Training &amp; Consulting LLC collects the information you choose to provide, such as your name, organization, role, email, phone, location, type of organization, area of interest, message, and preferred follow-up method.</p>

    <h3>How we use it</h3>
    <p>The information is used solely to respond to your inquiry and to discuss potential training, technical assistance, or collaboration. AGRILEAD does not sell your information.</p>

    <h3>How the form works</h3>
    <p>This site&rsquo;s contact form is processed through the website hosting provider&rsquo;s form service. Submissions may be stored by that provider to deliver your message to AGRILEAD.</p>

    <h3>Your choices</h3>
    <p>You may request that AGRILEAD update or delete the information you submitted by contacting us at [Email].</p>

    <h3>Contact</h3>
    <p>Questions about this policy can be sent to [Email], AGRILEAD Training &amp; Consulting LLC, Naples, Florida, United States.</p>
  </div>
</section>
<script>document.getElementById("pdate").textContent = new Date().toLocaleDateString("en-US",{{year:"numeric",month:"long",day:"numeric"}});</script>
'''
page("privacy.html",
     "Privacy Policy | AGRILEAD Training & Consulting LLC",
     "Privacy Policy for AGRILEAD Training & Consulting LLC.",
     "", privacy)

# ===========================================================================
# BLOG
# ===========================================================================
# To add an article: write its page (see the example below) and add one entry
# to POSTS — newest first. The listing page and nav update automatically.
POSTS = [
    ("blog-soil-health-starter.html", "Applied Agronomy",
     "Five Practical Habits for Healthier Farm Soil",
     "July 1, 2026", "4 min read",
     "Simple, low-cost practices — keeping soil covered, reducing tillage, "
     "building organic matter, testing before treating, and keeping living roots "
     "in the ground — that beginning and small-scale producers can start this season."),
]

def post_cards(posts):
    out = '<div class="grid grid-3">'
    for fn, cat, title, date, read, excerpt in posts:
        out += (
            f'<article class="card reveal">'
            f'<p class="eyebrow">{cat}</p>'
            f'<h3>{title}</h3>'
            f'<p class="form-note" style="margin:.2rem 0 .6rem">{date} &middot; {read}</p>'
            f'<p>{excerpt}</p>'
            f'<a class="link-arrow" href="{fn}">Read article {ICONS["arrow"]}</a>'
            f'</article>')
    out += '</div>'
    return out

blog = f'''
<section class="section section--tight">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Insights &amp; Updates</p>
      <h1>AGRILEAD Blog</h1>
      <p>Practical notes on agricultural training, applied agronomy, and language-accessible learning for beginning farmers, small-scale producers, and the organizations that support them.</p>
    </div>
    {post_cards(POSTS)}
    <div class="notice reveal" style="margin-top:2.2rem">More articles are on the way. Have a topic you would like us to cover? <a href="contact.html">Get in touch</a>.</div>
  </div>
</section>
'''
page("blog.html",
     "Blog | AGRILEAD Training & Consulting LLC",
     "Practical articles on agricultural training, applied agronomy, and bilingual farmer education from AGRILEAD Training & Consulting LLC.",
     "blog.html", blog)

# --- Example article --------------------------------------------------------
article_soil = f'''
<article class="section section--tight">
  <div class="container narrow">
    <p class="eyebrow">Applied Agronomy</p>
    <h1>Five Practical Habits for Healthier Farm Soil</h1>
    <p class="form-note">July 1, 2026 &middot; 4 min read</p>

    <p>Healthy soil is the foundation of a resilient farm. It holds water, feeds crops, resists erosion, and recovers more quickly after a hard season. The good news for beginning and small-scale producers is that better soil rarely requires expensive equipment — it comes from a few consistent habits practiced over time.</p>

    <h3 style="margin-top:2rem">1. Keep the soil covered</h3>
    <p>Bare soil bakes in the sun, crusts over, and washes away in heavy rain. Cover crops, crop residues, or mulch protect the surface, moderate soil temperature, and feed soil life. Even a simple cover between cash crops helps.</p>

    <h3>2. Disturb the soil less</h3>
    <p>Frequent, deep tillage breaks down soil structure and burns through organic matter. Where practical, reducing tillage helps keep the soil&rsquo;s natural channels intact so water and roots can move freely.</p>

    <h3>3. Build organic matter</h3>
    <p>Compost, well-managed manure, and returned crop residues add organic matter, which improves water-holding capacity and nutrient availability. Small, regular additions add up season after season.</p>

    <h3>4. Test before you treat</h3>
    <p>A basic soil test takes the guesswork out of fertility. Knowing your soil&rsquo;s pH and nutrient levels helps you apply what the field actually needs — and avoid spending on what it does not.</p>

    <h3>5. Keep living roots in the ground</h3>
    <p>Living roots feed the microbes that build healthy soil. Rotations and cover crops that keep something growing for more of the year support that underground community and help break pest and disease cycles.</p>

    <p class="footer-disclaimer" style="margin-top:2.2rem">This article is general educational information and is not a substitute for site-specific technical advice. Practices and results vary by soil type, climate, crop, and management.</p>

    <p style="margin-top:1.6rem"><a href="blog.html">&larr; Back to all articles</a></p>
  </div>
</article>
'''
page("blog-soil-health-starter.html",
     "Five Practical Habits for Healthier Farm Soil | AGRILEAD",
     "Five simple, low-cost soil health practices for beginning and small-scale farmers: soil cover, reduced tillage, organic matter, soil testing, and living roots.",
     "blog.html", article_soil)

print("ALL PAGES BUILT")
