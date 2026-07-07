#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds the AGRILEAD site pages (English + French) using shared components
in _build_base. English pages -> public/ ; French pages -> public/fr/."""
from _build_base import page, field_panel, values_block, pills_block, ICONS


def cards3(items):
    out = '<div class="grid grid-3">'
    for icon, title, body in items:
        out += (f'<article class="card reveal"><span class="icon">{ICONS[icon]}</span>'
                f'<h3>{title}</h3><p>{body}</p></article>')
    out += '</div>'
    return out


def notice(text):
    return f'<div class="notice reveal">{text}</div>'


def banner(eyebrow, title, img, alt):
    return (f'<section class="hero hero--banner">'
            f'<div class="hero-banner-media"><img src="{img}" alt="{alt}" loading="eager" decoding="async"></div>'
            f'<div class="container hero-banner-inner"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1></div>'
            f'</section>')


def post_cards(posts, read_label):
    out = '<div class="grid grid-3">'
    for fn, cat, title, date, read, excerpt in posts:
        out += (
            f'<article class="card reveal">'
            f'<p class="eyebrow">{cat}</p>'
            f'<h3>{title}</h3>'
            f'<p class="form-note" style="margin:.2rem 0 .6rem">{date} &middot; {read}</p>'
            f'<p>{excerpt}</p>'
            f'<a class="link-arrow" href="{fn}">{read_label} {ICONS["arrow"]}</a>'
            f'</article>')
    out += '</div>'
    return out


def options(items):
    return "".join(f'<option value="{i}">{i}</option>' for i in items)


# ===========================================================================
# ALL TRANSLATABLE CONTENT
# ===========================================================================
CONTENT = {
 "en": {
  "cta_collab": "Discuss a Potential Collaboration",
  "cta_services": "Explore Services",
  "cta_contact": "Contact AGRILEAD",
  "cta_submit": "Submit an Inquiry",
  "read_article": "Read article",
  "download_soon": "Download &mdash; coming soon",
  "see_all_services": "See all services",

  "home": {
    "title": "AGRILEAD Training & Consulting LLC | Agricultural Training in Florida",
    "desc": "AGRILEAD Training & Consulting LLC provides practical agricultural training, applied agronomy support, bilingual outreach, technical assistance, and farmer capacity-building services.",
    "eyebrow": "Naples, Florida &middot; Agricultural Training",
    "h1": "Practical Agricultural Training for Resilient Producers",
    "lead": "AGRILEAD Training &amp; Consulting LLC provides practical agricultural training, applied agronomy support, bilingual outreach, and farmer capacity-building for beginning farmers, small-scale producers, multilingual producers, and underserved agricultural communities.",
    "meta1": "Based in Naples, Florida",
    "meta2": "Bilingual &amp; multilingual outreach",
    "meta3": "Field-oriented, practical learning",
    "panel_cap": "Field-based farmer training session",
    "hero_alt": "Garden in bloom",
    "who_eyebrow": "Who we are",
    "who_h2": "Practical, field-oriented agricultural learning",
    "who_p1": "AGRILEAD Training &amp; Consulting LLC is based in Naples, Florida, United States. The company is designed to support accessible, practical, and field-oriented agricultural learning through training, technical assistance, curriculum development, bilingual outreach, and community-centered capacity-building.",
    "who_p2": "AGRILEAD focuses on helping producers, organizations, and training stakeholders discuss practical learning needs in areas such as soil health, crop diversification, climate-smart agriculture, applied agronomy, and farmer-centered education.",
    "do_eyebrow": "What we do",
    "do_h2": "Core areas of support",
    "cards": [
      ("book","Agricultural Training","Practical workshops, short courses, and learning activities designed to support farmer knowledge and field-level skills."),
      ("sprout","Applied Agronomy Support","Technical guidance related to soil health, crop production, crop diversification, sustainable practices, and climate-smart agriculture."),
      ("globe","Bilingual &amp; Multilingual Outreach","Training materials and outreach designed to improve language access for Haitian/Creole-speaking, Hispanic, immigrant, and multilingual producer communities."),
    ],
    "explore": [
      ("Services", "Agricultural training, applied agronomy, bilingual materials, and technical assistance.", "services.html"),
      ("Signature Initiative", "Our developing bilingual agricultural workforce and extension training initiative.", "signature-initiative.html"),
      ("Collaboration", "Ways to explore working together with producer groups and organizations.", "collaboration-opportunities.html"),
      ("Blog", "Practical notes on soil health, applied agronomy, and farmer education.", "blog.html"),
    ],
    "serve_eyebrow": "Who we serve",
    "serve_h2": "Designed for producers and the organizations that support them",
    "serve_p": "AGRILEAD is designed to serve a range of producers, community groups, and training stakeholders.",
    "approach_eyebrow": "Our approach",
    "approach_h2": "Practical, participatory, and adaptable",
    "approach_p1": "AGRILEAD uses a practical, participatory, field-oriented, and adaptable approach. Training activities may include workshops, technical sessions, farmer handouts, curriculum support, needs assessment, train-the-trainer activities, and pilot learning discussions.",
    "approach_p2": "The company emphasizes practical knowledge, language access, sustainability, collaboration, responsible documentation, and farmer-centered learning.",
    "sig_eyebrow": "Signature initiative",
    "sig_h2": "AgriLead Bilingual Agricultural Workforce &amp; Extension Training Initiative",
    "sig_p": "A developing initiative focused on practical agricultural training, bilingual outreach, technical assistance, and capacity-building for beginning farmers, small-scale producers, immigrant and multilingual producers, and underserved agricultural communities.",
    "sig_learn": "Learn about the initiative",
    "sig_list": ["Soil health &amp; applied agronomy workshops","Bilingual farmer handouts &amp; learning resources","Train-the-trainer &amp; community outreach","Needs assessment &amp; pilot training discussions"],
    "dl_eyebrow": "Downloadable materials",
    "dl_h2": "Informational overviews",
    "dl_p": "These materials are informational only. They do not represent confirmed partnerships, endorsements, funding, contracts, official affiliations, or guaranteed results.",
    "docs": [
      ("One-Page Project Summary","A concise overview of the initiative, target audiences, training areas, and potential outreach discussion topics."),
      ("Company Brochure","A brief institutional brochure presenting the company, services, approach, and contact information."),
      ("Signature Initiative Overview","A short introduction to the AgriLead Bilingual Agricultural Workforce and Extension Training Initiative."),
    ],
    "cta_eyebrow": "Collaboration",
    "cta_h2": "Interested in practical agricultural training?",
    "cta_p": "AGRILEAD is available to discuss potential collaboration opportunities with agricultural organizations, producer groups, community-based institutions, and training stakeholders.",
  },

  "who_we_serve": ["Beginning farmers","Small-scale producers","Immigrant &amp; multilingual producers","Haitian / Creole-speaking communities","Hispanic agricultural communities","Underserved rural communities","Farmworker communities","Producer groups","Agricultural nonprofits","Community-based organizations","Training stakeholders"],
  "values": [
    ("leaf","Practical Knowledge","Clear, useful, field-oriented learning."),
    ("group","Farmer-Centered Training","Training adapted to producer needs and realities."),
    ("shield","Integrity","Professional, transparent, and responsible communication."),
    ("globe","Inclusion &amp; Language Access","Support for bilingual and multilingual learning."),
    ("soil","Sustainability","Emphasis on soil health, resilience, and long-term farm viability."),
  ],

  "about": {
    "title": "About AGRILEAD Training & Consulting LLC",
    "desc": "Learn about AGRILEAD Training & Consulting LLC, a Florida-based agricultural training and consulting company supporting practical farmer education and bilingual outreach.",
    "eyebrow": "About AGRILEAD",
    "h1": "Practical, farmer-centered agricultural learning",
    "lead": "AGRILEAD Training &amp; Consulting LLC is a Florida-based agricultural training and consulting company focused on practical education, applied agronomy, bilingual outreach, technical assistance, curriculum development, and producer capacity-building.",
    "company_h2": "About the company",
    "company_p1": "AGRILEAD Training &amp; Consulting LLC is based in Naples, Florida, United States. The company supports practical, field-oriented agricultural learning for farmers, producer groups, community-based organizations, and agricultural stakeholders.",
    "company_p2": "Its work focuses on applied agronomy, technical assistance, bilingual and multilingual outreach, curriculum development, training materials, and farmer capacity-building &mdash; designed to make agricultural knowledge more accessible, practical, and adaptable to producer and community needs.",
    "panel_cap": "Agricultural learning setting",
    "mission_h3": "Mission",
    "mission_p": "AGRILEAD Training &amp; Consulting LLC provides practical, field-oriented agricultural training and applied agronomy support to strengthen the capacity of beginning farmers, small-scale producers, and underserved agricultural communities through bilingual and multilingual education focused on sustainability, productivity, and resilience.",
    "vision_h3": "Vision",
    "vision_p": "To contribute to stronger agricultural communities where beginning farmers, small-scale producers, and underserved growers have access to practical knowledge, technical support, and adaptable training models that support local and regional food systems.",
    "values_eyebrow": "Core values",
    "values_h2": "What guides our work",
    "founder_eyebrow": "Founder",
    "founder_h2": "Founder profile",
    "founder_cap": "Founder portrait",
    "founder_note": "Replace with photo",
    "founder_name": "Wilbert Georges",
    "founder_role": "Founder &amp; Executive Lead",
    "founder_p1": "Wilbert Georges is the Founder and Executive Lead of AGRILEAD Training &amp; Consulting LLC. He is an agricultural development professional with experience in farmer training, applied agronomy, rural capacity-building, climate-smart agriculture, cooperative strengthening, and agricultural project implementation.",
    "founder_p2": "His work has focused on supporting producer groups and rural communities through practical training, multilingual communication, and field-oriented capacity-building. Through AGRILEAD, he is developing a professional platform to support agricultural training, bilingual outreach, technical assistance, and curriculum development.",
    "cta_h2": "Learn about our services",
  },

  "services": {
    "title": "Agricultural Training and Consulting Services | AGRILEAD",
    "desc": "AGRILEAD offers agricultural training, applied agronomy support, soil health education, bilingual materials, technical assistance, and curriculum development.",
    "eyebrow": "Services",
    "h1": "Agricultural training and consulting services",
    "lead": "AGRILEAD provides practical agricultural training, applied agronomy support, technical assistance, curriculum development, and bilingual outreach services for producers and organizations.",
    "intro": "AGRILEAD&rsquo;s services are designed to support practical learning, technical guidance, and producer capacity-building. Services may be adapted based on organizational needs, available resources, and agreed scope of work.",
    "core_eyebrow": "Core services",
    "core_h2": "Areas of support available for discussion",
    "list": [
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
    ],
    "note": "<strong>Please note.</strong> Services may include the areas above and are available to discuss depending on scope and resources. Descriptions do not imply confirmed partnership, funding, contract, official affiliation, or guaranteed results unless documented in writing.",
    "cta_h2": "Request a services discussion",
  },

  "initiative": {
    "title": "AgriLead Bilingual Agricultural Workforce and Extension Training Initiative",
    "desc": "Learn about AGRILEAD's developing initiative focused on bilingual agricultural training, applied agronomy, technical assistance, and farmer capacity-building.",
    "eyebrow": "Signature initiative &middot; Developing",
    "h1": "AgriLead Bilingual Agricultural Workforce &amp; Extension Training Initiative",
    "lead": "A developing initiative designed to support practical agricultural training, bilingual outreach, technical assistance, and farmer capacity-building.",
    "purpose_eyebrow": "Purpose",
    "purpose_h2": "Practical, language-accessible learning",
    "purpose_p1": "The AgriLead Bilingual Agricultural Workforce and Extension Training Initiative is a developing initiative focused on supporting beginning farmers, small-scale producers, immigrant and multilingual producers, and underserved agricultural communities through practical training and language-accessible learning resources.",
    "purpose_p2": "Its purpose is to support practical agricultural education, applied agronomy learning, bilingual outreach, and producer capacity-building.",
    "panel_cap": "Multilingual farmer education",
    "benef_eyebrow": "Target beneficiaries",
    "benef_h2": "Who the initiative is designed for",
    "beneficiaries": ["Beginning farmers","Small-scale producers","Immigrant &amp; multilingual producers","Haitian / Creole-speaking communities","Hispanic agricultural communities","Underserved rural communities","Farmworker communities","Producer groups","Community-based organizations"],
    "act_eyebrow": "Potential activities",
    "act_h2": "What the initiative may include",
    "activities": [
      ("soil","Soil health training"),("sprout","Applied agronomy workshops"),("leaf","Crop diversification sessions"),
      ("climate","Climate-smart agriculture learning"),("globe","Bilingual farmer handouts"),("group","Train-the-trainer support"),
      ("chat","Community outreach"),("list","Needs assessment"),("book","Pilot training discussions"),
    ],
    "model_eyebrow": "Training model",
    "model_h2": "A flexible, modular platform",
    "model_p": "The initiative is designed as a flexible and modular training platform. Materials and activities may be adapted based on audience needs, language access, geographic context, agricultural priorities, available resources, and agreed scope of work.",
    "model_note": "<strong>Important note.</strong> This initiative does not imply confirmed partnerships, endorsements, funding, contracts, official affiliations, or guaranteed results unless documented in writing. Any collaboration would be subject to organizational policies, priorities, resources, timelines, and formal agreements.",
    "cta_h2": "Discuss a potential training activity",
  },

  "collab": {
    "title": "Collaboration Opportunities | AGRILEAD Training & Consulting LLC",
    "desc": "Explore potential collaboration opportunities with AGRILEAD in agricultural training, applied agronomy support, bilingual outreach, technical assistance, and farmer capacity-building.",
    "eyebrow": "Collaboration",
    "h1": "Collaboration opportunities",
    "lead": "Explore potential training, outreach, and technical assistance opportunities with AGRILEAD Training &amp; Consulting LLC.",
    "plat_eyebrow": "A professional platform",
    "plat_h2": "Available to discuss practical agricultural learning",
    "plat_p1": "AGRILEAD Training &amp; Consulting LLC is available to discuss potential collaboration opportunities with agricultural organizations, community-based institutions, producer groups, and training stakeholders interested in practical agricultural education, applied agronomy support, bilingual outreach, and farmer capacity-building.",
    "plat_p2": "Any collaboration would be subject to organizational policies, priorities, resources, timelines, and formal agreements.",
    "for_eyebrow": "Who this page is for",
    "for_h2": "Organizations and groups we may work with",
    "for_p": "This page is intended for organizations and groups that may be interested in practical agricultural training, technical assistance, bilingual outreach, or farmer-centered learning.",
    "for_whom": ["Beginning farmer programs","Small-scale producer groups","Agricultural nonprofits","Community-based organizations","Farmworker &amp; rural community organizations","Training institutions","Producer associations","Groups serving multilingual producers","Haitian/Creole-speaking communities","Hispanic agricultural communities"],
    "ways_eyebrow": "Potential collaboration opportunities",
    "ways_h2": "Ways to explore working together",
    "ways": [
      ("doc","Curriculum Review","Reviewing or providing feedback on practical agricultural training content."),
      ("book","Workshop Design","Discussing possible training topics, formats, and audience needs."),
      ("chat","Community Outreach Support","Exploring ways to communicate agricultural education opportunities to multilingual producer communities."),
      ("sprout","Technical Feedback","Discussing applied agronomy topics such as soil health, crop diversification, climate-smart practices, and producer capacity-building."),
      ("group","Train-the-Trainer Discussions","Exploring whether local facilitators, community leaders, or agricultural outreach workers may benefit from structured learning support."),
      ("list","Needs Assessment","Identifying training needs, language-access barriers, and practical learning priorities for producer groups."),
      ("hands","Pilot Training Discussions","Exploring whether a small-scale training session or learning activity may be appropriate, subject to organizational resources and formal arrangements."),
    ],
    "note": "<strong>Important note on collaboration.</strong> Potential collaboration does not imply confirmed partnership, endorsement, funding, contract, official affiliation, or guaranteed results unless documented in writing. AGRILEAD is not presenting itself as an official representative, affiliate, or partner of any public agency, university, Extension office, nonprofit organization, or external institution unless such relationship is formally documented.",
    "cta_h2": "Discuss a potential collaboration",
  },

  "contact": {
    "title": "Contact AGRILEAD Training & Consulting LLC",
    "desc": "Contact AGRILEAD Training & Consulting LLC to discuss potential agricultural training, applied agronomy, bilingual outreach, technical assistance, or curriculum development opportunities.",
    "eyebrow": "Contact",
    "h1": "Contact AGRILEAD Training &amp; Consulting LLC",
    "lead": "AGRILEAD is available to discuss potential training, technical assistance, curriculum development, bilingual outreach, and collaboration opportunities.",
    "info_h2": "Contact information",
    "l_location": "Location", "v_location": "Naples, Florida, United States",
    "l_phone": "Phone", "l_email": "Email", "l_website": "Website",
    "topics_h3": "Inquiry topics",
    "topics": ["Agricultural training","Applied agronomy support","Soil health education","Crop diversification","Climate-smart agriculture","Technical assistance","Bilingual outreach","Curriculum development","Train-the-trainer support","Potential collaboration opportunities"],
    "form_h2": "Send an inquiry",
    "f_name": "Name", "f_org": "Organization", "f_optional": "(optional)",
    "f_role": "Role / Title", "f_email": "Email", "f_phone": "Phone", "f_location": "Location",
    "f_orgtype": "Type of organization", "f_area": "Area of interest",
    "f_select": "Select one", "f_message": "Message",
    "f_followup": "Preferred follow-up method",
    "org_types": ["Agricultural organization","Community-based organization","Producer group","Training institution","Farmworker or rural community organization","Small farm program","Other"],
    "areas": ["Agricultural Training","Applied Agronomy Support","Soil Health Education","Crop Diversification","Climate-Smart Agriculture","Bilingual Outreach","Curriculum Development","Train-the-Trainer","Technical Assistance","Potential Collaboration","Other"],
    "followups": ["Email","Phone","No preference"],
    "submit": "Submit an Inquiry",
    "form_note": "Submitting an inquiry does not create a partnership, contract, funding commitment, or formal affiliation.",
  },

  "thankyou": {
    "title": "Thank You | AGRILEAD Training & Consulting LLC",
    "desc": "Your inquiry to AGRILEAD Training & Consulting LLC has been received.",
    "h1": "Thank you &mdash; your inquiry was received",
    "p": "We appreciate your message. AGRILEAD will review your inquiry and follow up as appropriate. Submitting an inquiry does not create a partnership, contract, funding commitment, or formal affiliation.",
    "back": "Back to Home",
  },

  "privacy": {
    "title": "Privacy Policy | AGRILEAD Training & Consulting LLC",
    "desc": "Privacy Policy for AGRILEAD Training & Consulting LLC.",
    "eyebrow": "Privacy",
    "h1": "Privacy Policy",
    "updated": "Last updated:",
    "updated_note": "This is a general template and should be reviewed for accuracy before final publication.",
    "s1_h": "Information we collect",
    "s1_p": "When you submit the contact form on this website, AGRILEAD Training &amp; Consulting LLC collects the information you choose to provide, such as your name, organization, role, email, phone, location, type of organization, area of interest, message, and preferred follow-up method.",
    "s2_h": "How we use it",
    "s2_p": "The information is used solely to respond to your inquiry and to discuss potential training, technical assistance, or collaboration. AGRILEAD does not sell your information.",
    "s3_h": "How the form works",
    "s3_p": "This site&rsquo;s contact form is processed through the website hosting provider&rsquo;s form service. Submissions may be stored by that provider to deliver your message to AGRILEAD.",
    "s4_h": "Your choices",
    "s4_p": "You may request that AGRILEAD update or delete the information you submitted by contacting us at [Email].",
    "s5_h": "Contact",
    "s5_p": "Questions about this policy can be sent to [Email], AGRILEAD Training &amp; Consulting LLC, Naples, Florida, United States.",
    "locale": "en-US",
  },

  "blog": {
    "title": "Blog | AGRILEAD Training & Consulting LLC",
    "desc": "Practical articles on agricultural training, applied agronomy, and bilingual farmer education from AGRILEAD Training & Consulting LLC.",
    "eyebrow": "Insights &amp; Updates",
    "h1": "AGRILEAD Blog",
    "intro": "Practical notes on agricultural training, applied agronomy, and language-accessible learning for beginning farmers, small-scale producers, and the organizations that support them.",
    "more": "More articles are on the way. Have a topic you would like us to cover? <a href=\"contact.html\">Get in touch</a>.",
    "posts": [
      ("blog-soil-health-starter.html","Applied Agronomy","Five Practical Habits for Healthier Farm Soil","July 1, 2026","4 min read","Simple, low-cost practices — keeping soil covered, reducing tillage, building organic matter, testing before treating, and keeping living roots in the ground — that beginning and small-scale producers can start this season."),
    ],
  },

  "article": {
    "title": "Five Practical Habits for Healthier Farm Soil | AGRILEAD",
    "desc": "Five simple, low-cost soil health practices for beginning and small-scale farmers: soil cover, reduced tillage, organic matter, soil testing, and living roots.",
    "cat": "Applied Agronomy",
    "h1": "Five Practical Habits for Healthier Farm Soil",
    "meta": "July 1, 2026 &middot; 4 min read",
    "intro": "Healthy soil is the foundation of a resilient farm. It holds water, feeds crops, resists erosion, and recovers more quickly after a hard season. The good news for beginning and small-scale producers is that better soil rarely requires expensive equipment — it comes from a few consistent habits practiced over time.",
    "h1_1": "1. Keep the soil covered",
    "p_1": "Bare soil bakes in the sun, crusts over, and washes away in heavy rain. Cover crops, crop residues, or mulch protect the surface, moderate soil temperature, and feed soil life. Even a simple cover between cash crops helps.",
    "h1_2": "2. Disturb the soil less",
    "p_2": "Frequent, deep tillage breaks down soil structure and burns through organic matter. Where practical, reducing tillage helps keep the soil&rsquo;s natural channels intact so water and roots can move freely.",
    "h1_3": "3. Build organic matter",
    "p_3": "Compost, well-managed manure, and returned crop residues add organic matter, which improves water-holding capacity and nutrient availability. Small, regular additions add up season after season.",
    "h1_4": "4. Test before you treat",
    "p_4": "A basic soil test takes the guesswork out of fertility. Knowing your soil&rsquo;s pH and nutrient levels helps you apply what the field actually needs — and avoid spending on what it does not.",
    "h1_5": "5. Keep living roots in the ground",
    "p_5": "Living roots feed the microbes that build healthy soil. Rotations and cover crops that keep something growing for more of the year support that underground community and help break pest and disease cycles.",
    "disclaimer": "This article is general educational information and is not a substitute for site-specific technical advice. Practices and results vary by soil type, climate, crop, and management.",
    "back": "&larr; Back to all articles",
  },
 },

 "fr": {
  "cta_collab": "Discuter d'une collaboration",
  "cta_services": "Découvrir les services",
  "cta_contact": "Contacter AGRILEAD",
  "cta_submit": "Envoyer une demande",
  "read_article": "Lire l'article",
  "download_soon": "Télécharger &mdash; bientôt disponible",
  "see_all_services": "Voir tous les services",

  "home": {
    "title": "AGRILEAD Training & Consulting LLC | Formation agricole en Floride",
    "desc": "AGRILEAD Training & Consulting LLC propose une formation agricole pratique, un appui en agronomie appliquée, une sensibilisation bilingue, une assistance technique et le renforcement des capacités des agriculteurs.",
    "eyebrow": "Naples, Floride &middot; Formation agricole",
    "h1": "Une formation agricole pratique pour des producteurs résilients",
    "lead": "AGRILEAD Training &amp; Consulting LLC propose une formation agricole pratique, un appui en agronomie appliquée, une sensibilisation bilingue et le renforcement des capacités pour les agriculteurs débutants, les petits producteurs, les producteurs multilingues et les communautés agricoles mal desservies.",
    "meta1": "Basée à Naples, Floride",
    "meta2": "Sensibilisation bilingue et multilingue",
    "meta3": "Apprentissage pratique, orienté terrain",
    "panel_cap": "Session de formation au champ",
    "hero_alt": "Jardin en fleurs",
    "who_eyebrow": "Qui nous sommes",
    "who_h2": "Un apprentissage agricole pratique et orienté terrain",
    "who_p1": "AGRILEAD Training &amp; Consulting LLC est basée à Naples, en Floride (États-Unis). La société vise à soutenir un apprentissage agricole accessible, pratique et orienté terrain, à travers la formation, l'assistance technique, l'élaboration de programmes, la sensibilisation bilingue et le renforcement des capacités centré sur la communauté.",
    "who_p2": "AGRILEAD aide les producteurs, les organisations et les acteurs de la formation à définir leurs besoins d'apprentissage pratiques dans des domaines tels que la santé des sols, la diversification des cultures, l'agriculture intelligente face au climat, l'agronomie appliquée et l'éducation centrée sur l'agriculteur.",
    "do_eyebrow": "Ce que nous faisons",
    "do_h2": "Nos principaux domaines d'appui",
    "cards": [
      ("book","Formation agricole","Ateliers pratiques, courtes formations et activités d'apprentissage conçus pour renforcer les connaissances des agriculteurs et les compétences de terrain."),
      ("sprout","Appui en agronomie appliquée","Conseils techniques sur la santé des sols, la production, la diversification des cultures, les pratiques durables et l'agriculture intelligente face au climat."),
      ("globe","Sensibilisation bilingue et multilingue","Supports de formation et actions de sensibilisation conçus pour améliorer l'accès linguistique des communautés créolophones/haïtiennes, hispaniques, immigrantes et multilingues."),
    ],
    "explore": [
      ("Services", "Formation agricole, agronomie appliquée, supports bilingues et assistance technique.", "services.html"),
      ("Initiative phare", "Notre initiative bilingue de formation de la main-d'œuvre agricole et de vulgarisation.", "signature-initiative.html"),
      ("Collaboration", "Des façons d'explorer une collaboration avec les groupes de producteurs et les organisations.", "collaboration-opportunities.html"),
      ("Blog", "Des notes pratiques sur la santé des sols, l'agronomie appliquée et l'éducation des agriculteurs.", "blog.html"),
    ],
    "serve_eyebrow": "Qui nous servons",
    "serve_h2": "Conçu pour les producteurs et les organisations qui les accompagnent",
    "serve_p": "AGRILEAD est conçue pour servir un large éventail de producteurs, de groupes communautaires et d'acteurs de la formation.",
    "approach_eyebrow": "Notre approche",
    "approach_h2": "Pratique, participative et adaptable",
    "approach_p1": "AGRILEAD adopte une approche pratique, participative, orientée terrain et adaptable. Les activités de formation peuvent inclure des ateliers, des séances techniques, des fiches pour agriculteurs, un appui aux programmes, l'évaluation des besoins, la formation de formateurs et des discussions de formation pilote.",
    "approach_p2": "La société met l'accent sur les connaissances pratiques, l'accès linguistique, la durabilité, la collaboration, une documentation responsable et un apprentissage centré sur l'agriculteur.",
    "sig_eyebrow": "Initiative phare",
    "sig_h2": "Initiative AgriLead de formation bilingue de la main-d'œuvre agricole et de vulgarisation",
    "sig_p": "Une initiative en développement axée sur la formation agricole pratique, la sensibilisation bilingue, l'assistance technique et le renforcement des capacités pour les agriculteurs débutants, les petits producteurs, les producteurs immigrants et multilingues et les communautés agricoles mal desservies.",
    "sig_learn": "En savoir plus sur l'initiative",
    "sig_list": ["Ateliers sur la santé des sols et l'agronomie appliquée","Fiches et ressources d'apprentissage bilingues","Formation de formateurs et sensibilisation communautaire","Évaluation des besoins et discussions de formation pilote"],
    "dl_eyebrow": "Documents à télécharger",
    "dl_h2": "Présentations informatives",
    "dl_p": "Ces documents sont fournis à titre informatif uniquement. Ils ne représentent aucun partenariat confirmé, soutien, financement, contrat, affiliation officielle ou résultat garanti.",
    "docs": [
      ("Résumé du projet (1 page)","Un aperçu concis de l'initiative, des publics cibles, des domaines de formation et des sujets de discussion possibles."),
      ("Brochure de l'entreprise","Une brève brochure institutionnelle présentant la société, les services, l'approche et les coordonnées."),
      ("Présentation de l'initiative phare","Une courte introduction à l'Initiative AgriLead de formation bilingue de la main-d'œuvre agricole et de vulgarisation."),
    ],
    "cta_eyebrow": "Collaboration",
    "cta_h2": "Intéressé par une formation agricole pratique ?",
    "cta_p": "AGRILEAD est disponible pour discuter d'opportunités de collaboration avec des organisations agricoles, des groupes de producteurs, des institutions communautaires et des acteurs de la formation.",
  },

  "who_we_serve": ["Agriculteurs débutants","Petits producteurs","Producteurs immigrants et multilingues","Communautés créolophones / haïtiennes","Communautés agricoles hispaniques","Communautés rurales mal desservies","Communautés de travailleurs agricoles","Groupes de producteurs","Associations agricoles à but non lucratif","Organisations communautaires","Acteurs de la formation"],
  "values": [
    ("leaf","Connaissances pratiques","Un apprentissage clair, utile et orienté terrain."),
    ("group","Formation centrée sur l'agriculteur","Une formation adaptée aux besoins et réalités des producteurs."),
    ("shield","Intégrité","Une communication professionnelle, transparente et responsable."),
    ("globe","Inclusion et accès linguistique","Un appui à l'apprentissage bilingue et multilingue."),
    ("soil","Durabilité","L'accent sur la santé des sols, la résilience et la viabilité à long terme des exploitations."),
  ],

  "about": {
    "title": "À propos d'AGRILEAD Training & Consulting LLC",
    "desc": "Découvrez AGRILEAD Training & Consulting LLC, une société de formation et de conseil agricoles basée en Floride qui soutient l'éducation pratique des agriculteurs et la sensibilisation bilingue.",
    "eyebrow": "À propos d'AGRILEAD",
    "h1": "Un apprentissage agricole pratique, centré sur l'agriculteur",
    "lead": "AGRILEAD Training &amp; Consulting LLC est une société de formation et de conseil agricoles basée en Floride, axée sur l'éducation pratique, l'agronomie appliquée, la sensibilisation bilingue, l'assistance technique, l'élaboration de programmes et le renforcement des capacités des producteurs.",
    "company_h2": "À propos de la société",
    "company_p1": "AGRILEAD Training &amp; Consulting LLC est basée à Naples, en Floride (États-Unis). La société soutient un apprentissage agricole pratique et orienté terrain pour les agriculteurs, les groupes de producteurs, les organisations communautaires et les acteurs du secteur agricole.",
    "company_p2": "Son travail porte sur l'agronomie appliquée, l'assistance technique, la sensibilisation bilingue et multilingue, l'élaboration de programmes, les supports de formation et le renforcement des capacités des agriculteurs &mdash; afin de rendre le savoir agricole plus accessible, pratique et adaptable aux besoins des producteurs et des communautés.",
    "panel_cap": "Cadre d'apprentissage agricole",
    "mission_h3": "Mission",
    "mission_p": "AGRILEAD Training &amp; Consulting LLC offre une formation agricole pratique et orientée terrain ainsi qu'un appui en agronomie appliquée pour renforcer les capacités des agriculteurs débutants, des petits producteurs et des communautés agricoles mal desservies, à travers une éducation bilingue et multilingue axée sur la durabilité, la productivité et la résilience.",
    "vision_h3": "Vision",
    "vision_p": "Contribuer à des communautés agricoles plus fortes où les agriculteurs débutants, les petits producteurs et les cultivateurs mal desservis ont accès à des connaissances pratiques, à un appui technique et à des modèles de formation adaptables qui soutiennent les systèmes alimentaires locaux et régionaux.",
    "values_eyebrow": "Valeurs fondamentales",
    "values_h2": "Ce qui guide notre travail",
    "founder_eyebrow": "Fondateur",
    "founder_h2": "Profil du fondateur",
    "founder_cap": "Portrait du fondateur",
    "founder_note": "Photo à venir",
    "founder_name": "Wilbert Georges",
    "founder_role": "Fondateur et Directeur exécutif",
    "founder_p1": "Wilbert Georges est le fondateur et le directeur exécutif d'AGRILEAD Training &amp; Consulting LLC. C'est un professionnel du développement agricole ayant une expérience en formation des agriculteurs, agronomie appliquée, renforcement des capacités rurales, agriculture intelligente face au climat, renforcement des coopératives et mise en œuvre de projets agricoles.",
    "founder_p2": "Son travail a consisté à accompagner des groupes de producteurs et des communautés rurales par la formation pratique, la communication multilingue et le renforcement des capacités orienté terrain. À travers AGRILEAD, il développe une plateforme professionnelle pour soutenir la formation agricole, la sensibilisation bilingue, l'assistance technique et l'élaboration de programmes.",
    "cta_h2": "Découvrez nos services",
  },

  "services": {
    "title": "Services de formation et de conseil agricoles | AGRILEAD",
    "desc": "AGRILEAD propose de la formation agricole, un appui en agronomie appliquée, l'éducation à la santé des sols, des supports bilingues, une assistance technique et l'élaboration de programmes.",
    "eyebrow": "Services",
    "h1": "Services de formation et de conseil agricoles",
    "lead": "AGRILEAD propose une formation agricole pratique, un appui en agronomie appliquée, une assistance technique, l'élaboration de programmes et des services de sensibilisation bilingue pour les producteurs et les organisations.",
    "intro": "Les services d'AGRILEAD visent à soutenir l'apprentissage pratique, l'accompagnement technique et le renforcement des capacités des producteurs. Ils peuvent être adaptés selon les besoins des organisations, les ressources disponibles et l'étendue des travaux convenue.",
    "core_eyebrow": "Services principaux",
    "core_h2": "Domaines d'appui disponibles pour discussion",
    "list": [
      ("book","Formation agricole","Ateliers, courtes formations et activités d'apprentissage orientées terrain pour les agriculteurs, les groupes de producteurs et les organisations communautaires."),
      ("sprout","Appui en agronomie appliquée","Conseils sur la production, la fertilité des sols, la gestion des cultures et les pratiques agricoles durables."),
      ("soil","Éducation à la santé et à la fertilité des sols","Formation sur la matière organique, le compostage, la gestion des nutriments, la conservation des sols et la planification de base de la fertilité."),
      ("leaf","Diversification des cultures","Appui éducatif à la production diversifiée, à la planification des exploitations, à la réduction des risques et aux systèmes de culture durables."),
      ("climate","Agriculture intelligente face au climat","Formations et sujets de discussion sur l'adaptation au climat, la gestion des ressources et des pratiques de production résilientes."),
      ("wrench","Assistance technique","Appui aux organisations agricoles, groupes de producteurs et initiatives communautaires cherchant des conseils agricoles pratiques."),
      ("globe","Supports de formation bilingues et multilingues","Fiches pour agriculteurs, outils de sensibilisation, supports d'ateliers et ressources d'apprentissage conçus pour favoriser l'accès linguistique."),
      ("group","Appui à la formation de formateurs","Renforcement des capacités des facilitateurs, des leaders communautaires et des agents de sensibilisation agricole."),
      ("doc","Élaboration de programmes","Modules de formation, plans de cours, guides de facilitateur et supports d'éducation pour agriculteurs."),
      ("chart","Suivi, évaluation et apprentissage","Outils de base pour documenter les activités de formation, recueillir les retours et soutenir l'amélioration de l'apprentissage."),
    ],
    "note": "<strong>À noter.</strong> Les services peuvent inclure les domaines ci-dessus et sont disponibles pour discussion selon l'étendue et les ressources. Les descriptions n'impliquent aucun partenariat confirmé, financement, contrat, affiliation officielle ou résultat garanti, sauf accord écrit.",
    "cta_h2": "Demander un échange sur les services",
  },

  "initiative": {
    "title": "Initiative AgriLead de formation bilingue de la main-d'œuvre agricole et de vulgarisation",
    "desc": "Découvrez l'initiative en développement d'AGRILEAD, axée sur la formation agricole bilingue, l'agronomie appliquée, l'assistance technique et le renforcement des capacités des agriculteurs.",
    "eyebrow": "Initiative phare &middot; En développement",
    "h1": "Initiative AgriLead de formation bilingue de la main-d'œuvre agricole et de vulgarisation",
    "lead": "Une initiative en développement conçue pour soutenir la formation agricole pratique, la sensibilisation bilingue, l'assistance technique et le renforcement des capacités des agriculteurs.",
    "purpose_eyebrow": "Objectif",
    "purpose_h2": "Un apprentissage pratique et accessible sur le plan linguistique",
    "purpose_p1": "L'Initiative AgriLead de formation bilingue de la main-d'œuvre agricole et de vulgarisation est une initiative en développement axée sur l'accompagnement des agriculteurs débutants, des petits producteurs, des producteurs immigrants et multilingues et des communautés agricoles mal desservies, grâce à une formation pratique et à des ressources d'apprentissage accessibles sur le plan linguistique.",
    "purpose_p2": "Son objectif est de soutenir l'éducation agricole pratique, l'apprentissage de l'agronomie appliquée, la sensibilisation bilingue et le renforcement des capacités des producteurs.",
    "panel_cap": "Éducation agricole multilingue",
    "benef_eyebrow": "Bénéficiaires cibles",
    "benef_h2": "À qui s'adresse l'initiative",
    "beneficiaries": ["Agriculteurs débutants","Petits producteurs","Producteurs immigrants et multilingues","Communautés créolophones / haïtiennes","Communautés agricoles hispaniques","Communautés rurales mal desservies","Communautés de travailleurs agricoles","Groupes de producteurs","Organisations communautaires"],
    "act_eyebrow": "Activités possibles",
    "act_h2": "Ce que l'initiative peut inclure",
    "activities": [
      ("soil","Formation à la santé des sols"),("sprout","Ateliers d'agronomie appliquée"),("leaf","Séances de diversification des cultures"),
      ("climate","Apprentissage de l'agriculture climato-intelligente"),("globe","Fiches bilingues pour agriculteurs"),("group","Appui à la formation de formateurs"),
      ("chat","Sensibilisation communautaire"),("list","Évaluation des besoins"),("book","Discussions de formation pilote"),
    ],
    "model_eyebrow": "Modèle de formation",
    "model_h2": "Une plateforme flexible et modulaire",
    "model_p": "L'initiative est conçue comme une plateforme de formation flexible et modulaire. Les supports et activités peuvent être adaptés selon les besoins du public, l'accès linguistique, le contexte géographique, les priorités agricoles, les ressources disponibles et l'étendue des travaux convenue.",
    "model_note": "<strong>Note importante.</strong> Cette initiative n'implique aucun partenariat confirmé, soutien, financement, contrat, affiliation officielle ou résultat garanti, sauf accord écrit. Toute collaboration serait soumise aux politiques, priorités, ressources, calendriers et accords formels des organisations.",
    "cta_h2": "Discuter d'une activité de formation potentielle",
  },

  "collab": {
    "title": "Opportunités de collaboration | AGRILEAD Training & Consulting LLC",
    "desc": "Explorez des opportunités de collaboration avec AGRILEAD en formation agricole, appui en agronomie appliquée, sensibilisation bilingue, assistance technique et renforcement des capacités.",
    "eyebrow": "Collaboration",
    "h1": "Opportunités de collaboration",
    "lead": "Explorez des opportunités de formation, de sensibilisation et d'assistance technique avec AGRILEAD Training &amp; Consulting LLC.",
    "plat_eyebrow": "Une plateforme professionnelle",
    "plat_h2": "Disponible pour échanger sur l'apprentissage agricole pratique",
    "plat_p1": "AGRILEAD Training &amp; Consulting LLC est disponible pour discuter d'opportunités de collaboration avec des organisations agricoles, des institutions communautaires, des groupes de producteurs et des acteurs de la formation intéressés par l'éducation agricole pratique, l'appui en agronomie appliquée, la sensibilisation bilingue et le renforcement des capacités.",
    "plat_p2": "Toute collaboration serait soumise aux politiques, priorités, ressources, calendriers et accords formels des organisations.",
    "for_eyebrow": "À qui s'adresse cette page",
    "for_h2": "Organisations et groupes avec lesquels nous pouvons travailler",
    "for_p": "Cette page s'adresse aux organisations et groupes susceptibles d'être intéressés par la formation agricole pratique, l'assistance technique, la sensibilisation bilingue ou l'apprentissage centré sur l'agriculteur.",
    "for_whom": ["Programmes pour agriculteurs débutants","Groupes de petits producteurs","Associations agricoles à but non lucratif","Organisations communautaires","Organisations de travailleurs agricoles et rurales","Institutions de formation","Associations de producteurs","Groupes servant des producteurs multilingues","Communautés créolophones/haïtiennes","Communautés agricoles hispaniques"],
    "ways_eyebrow": "Opportunités de collaboration possibles",
    "ways_h2": "Des façons d'explorer une collaboration",
    "ways": [
      ("doc","Revue de programmes","Relecture ou retours sur des contenus de formation agricole pratiques."),
      ("book","Conception d'ateliers","Discussion des thèmes, formats et besoins du public pour la formation."),
      ("chat","Appui à la sensibilisation communautaire","Explorer les moyens de communiquer les opportunités d'éducation agricole aux communautés de producteurs multilingues."),
      ("sprout","Retours techniques","Échanges sur des sujets d'agronomie appliquée : santé des sols, diversification des cultures, pratiques climato-intelligentes et renforcement des capacités."),
      ("group","Discussions sur la formation de formateurs","Explorer si des facilitateurs locaux, leaders communautaires ou agents de sensibilisation pourraient bénéficier d'un appui structuré."),
      ("list","Évaluation des besoins","Identifier les besoins de formation, les obstacles d'accès linguistique et les priorités d'apprentissage des groupes de producteurs."),
      ("hands","Discussions de formation pilote","Explorer si une séance de formation à petite échelle serait appropriée, sous réserve des ressources et d'accords formels."),
    ],
    "note": "<strong>Note importante sur la collaboration.</strong> Une collaboration potentielle n'implique aucun partenariat confirmé, soutien, financement, contrat, affiliation officielle ou résultat garanti, sauf accord écrit. AGRILEAD ne se présente pas comme représentant officiel, affilié ou partenaire d'une agence publique, université, service de vulgarisation, association à but non lucratif ou institution externe, sauf si une telle relation est formellement documentée.",
    "cta_h2": "Discuter d'une collaboration potentielle",
  },

  "contact": {
    "title": "Contacter AGRILEAD Training & Consulting LLC",
    "desc": "Contactez AGRILEAD Training & Consulting LLC pour discuter de formation agricole, d'agronomie appliquée, de sensibilisation bilingue, d'assistance technique ou d'élaboration de programmes.",
    "eyebrow": "Contact",
    "h1": "Contacter AGRILEAD Training &amp; Consulting LLC",
    "lead": "AGRILEAD est disponible pour discuter de formation, d'assistance technique, d'élaboration de programmes, de sensibilisation bilingue et d'opportunités de collaboration.",
    "info_h2": "Coordonnées",
    "l_location": "Lieu", "v_location": "Naples, Floride, États-Unis",
    "l_phone": "Téléphone", "l_email": "E-mail", "l_website": "Site web",
    "topics_h3": "Sujets de demande",
    "topics": ["Formation agricole","Appui en agronomie appliquée","Éducation à la santé des sols","Diversification des cultures","Agriculture climato-intelligente","Assistance technique","Sensibilisation bilingue","Élaboration de programmes","Appui à la formation de formateurs","Opportunités de collaboration"],
    "form_h2": "Envoyer une demande",
    "f_name": "Nom", "f_org": "Organisation", "f_optional": "(facultatif)",
    "f_role": "Fonction / Titre", "f_email": "E-mail", "f_phone": "Téléphone", "f_location": "Lieu",
    "f_orgtype": "Type d'organisation", "f_area": "Domaine d'intérêt",
    "f_select": "Sélectionner", "f_message": "Message",
    "f_followup": "Mode de suivi préféré",
    "org_types": ["Organisation agricole","Organisation communautaire","Groupe de producteurs","Institution de formation","Organisation de travailleurs agricoles ou rurale","Programme de petite exploitation","Autre"],
    "areas": ["Formation agricole","Appui en agronomie appliquée","Éducation à la santé des sols","Diversification des cultures","Agriculture climato-intelligente","Sensibilisation bilingue","Élaboration de programmes","Formation de formateurs","Assistance technique","Collaboration potentielle","Autre"],
    "followups": ["E-mail","Téléphone","Sans préférence"],
    "submit": "Envoyer une demande",
    "form_note": "L'envoi d'une demande ne crée aucun partenariat, contrat, engagement de financement ni affiliation formelle.",
  },

  "thankyou": {
    "title": "Merci | AGRILEAD Training & Consulting LLC",
    "desc": "Votre demande à AGRILEAD Training & Consulting LLC a bien été reçue.",
    "h1": "Merci &mdash; votre demande a bien été reçue",
    "p": "Nous vous remercions de votre message. AGRILEAD examinera votre demande et y donnera suite le cas échéant. L'envoi d'une demande ne crée aucun partenariat, contrat, engagement de financement ni affiliation formelle.",
    "back": "Retour à l'accueil",
  },

  "privacy": {
    "title": "Politique de confidentialité | AGRILEAD Training & Consulting LLC",
    "desc": "Politique de confidentialité d'AGRILEAD Training & Consulting LLC.",
    "eyebrow": "Confidentialité",
    "h1": "Politique de confidentialité",
    "updated": "Dernière mise à jour :",
    "updated_note": "Ceci est un modèle général qui devrait être vérifié avant publication finale.",
    "s1_h": "Informations que nous collectons",
    "s1_p": "Lorsque vous soumettez le formulaire de contact de ce site, AGRILEAD Training &amp; Consulting LLC collecte les informations que vous choisissez de fournir, telles que votre nom, organisation, fonction, e-mail, téléphone, lieu, type d'organisation, domaine d'intérêt, message et mode de suivi préféré.",
    "s2_h": "Comment nous les utilisons",
    "s2_p": "Ces informations servent uniquement à répondre à votre demande et à discuter d'une formation, d'une assistance technique ou d'une collaboration potentielles. AGRILEAD ne vend pas vos informations.",
    "s3_h": "Fonctionnement du formulaire",
    "s3_p": "Le formulaire de contact de ce site est traité via le service de formulaires de l'hébergeur du site. Les soumissions peuvent être stockées par ce prestataire afin de transmettre votre message à AGRILEAD.",
    "s4_h": "Vos choix",
    "s4_p": "Vous pouvez demander à AGRILEAD de mettre à jour ou de supprimer les informations que vous avez soumises en nous écrivant à [Email].",
    "s5_h": "Contact",
    "s5_p": "Toute question relative à cette politique peut être envoyée à [Email], AGRILEAD Training &amp; Consulting LLC, Naples, Floride, États-Unis.",
    "locale": "fr-FR",
  },

  "blog": {
    "title": "Blog | AGRILEAD Training & Consulting LLC",
    "desc": "Articles pratiques sur la formation agricole, l'agronomie appliquée et l'éducation bilingue des agriculteurs par AGRILEAD Training & Consulting LLC.",
    "eyebrow": "Analyses et actualités",
    "h1": "Blog AGRILEAD",
    "intro": "Des notes pratiques sur la formation agricole, l'agronomie appliquée et l'apprentissage accessible sur le plan linguistique, pour les agriculteurs débutants, les petits producteurs et les organisations qui les accompagnent.",
    "more": "D'autres articles arrivent bientôt. Un sujet que vous aimeriez voir traité ? <a href=\"contact.html\">Contactez-nous</a>.",
    "posts": [
      ("blog-soil-health-starter.html","Agronomie appliquée","Cinq habitudes pratiques pour des sols agricoles plus sains","1 juillet 2026","4 min de lecture","Des pratiques simples et peu coûteuses — garder le sol couvert, réduire le travail du sol, enrichir la matière organique, analyser avant de traiter et maintenir des racines vivantes — que les producteurs débutants et petits producteurs peuvent adopter dès cette saison."),
    ],
  },

  "article": {
    "title": "Cinq habitudes pratiques pour des sols agricoles plus sains | AGRILEAD",
    "desc": "Cinq pratiques simples et peu coûteuses pour la santé des sols : couverture du sol, réduction du travail du sol, matière organique, analyse de sol et racines vivantes.",
    "cat": "Agronomie appliquée",
    "h1": "Cinq habitudes pratiques pour des sols agricoles plus sains",
    "meta": "1 juillet 2026 &middot; 4 min de lecture",
    "intro": "Un sol sain est le fondement d'une exploitation résiliente. Il retient l'eau, nourrit les cultures, résiste à l'érosion et se rétablit plus vite après une saison difficile. La bonne nouvelle pour les producteurs débutants et petits producteurs : un meilleur sol nécessite rarement du matériel coûteux — il résulte de quelques habitudes régulières, pratiquées dans la durée.",
    "h1_1": "1. Garder le sol couvert",
    "p_1": "Un sol nu cuit au soleil, se croûte et est emporté par les fortes pluies. Les cultures de couverture, les résidus de culture ou le paillis protègent la surface, modèrent la température du sol et nourrissent la vie du sol. Même une simple couverture entre deux cultures aide.",
    "h1_2": "2. Travailler le sol moins souvent",
    "p_2": "Un travail du sol fréquent et profond détruit la structure du sol et épuise la matière organique. Lorsque c'est possible, réduire le travail du sol aide à préserver les canaux naturels du sol afin que l'eau et les racines circulent librement.",
    "h1_3": "3. Enrichir la matière organique",
    "p_3": "Le compost, le fumier bien géré et les résidus de culture restitués apportent de la matière organique, ce qui améliore la capacité de rétention d'eau et la disponibilité des nutriments. De petits apports réguliers s'additionnent saison après saison.",
    "h1_4": "4. Analyser avant de traiter",
    "p_4": "Une analyse de sol de base élimine les incertitudes sur la fertilité. Connaître le pH et les niveaux de nutriments de votre sol vous aide à apporter ce dont la parcelle a réellement besoin — et à éviter de dépenser pour ce qui est inutile.",
    "h1_5": "5. Maintenir des racines vivantes dans le sol",
    "p_5": "Les racines vivantes nourrissent les micro-organismes qui construisent un sol sain. Les rotations et les cultures de couverture qui maintiennent une végétation une plus grande partie de l'année soutiennent cette communauté souterraine et aident à briser les cycles de ravageurs et de maladies.",
    "disclaimer": "Cet article fournit des informations éducatives générales et ne remplace pas un conseil technique adapté au site. Les pratiques et les résultats varient selon le type de sol, le climat, la culture et la gestion.",
    "back": "&larr; Retour à tous les articles",
  },
 },

 "es": {
  "cta_collab": "Hablar de una posible colaboración",
  "cta_services": "Descubrir los servicios",
  "cta_contact": "Contactar a AGRILEAD",
  "cta_submit": "Enviar una solicitud",
  "read_article": "Leer el artículo",
  "download_soon": "Descargar &mdash; próximamente",
  "see_all_services": "Ver todos los servicios",

  "home": {
    "title": "AGRILEAD Training & Consulting LLC | Formación agrícola en Florida",
    "desc": "AGRILEAD Training & Consulting LLC ofrece formación agrícola práctica, apoyo en agronomía aplicada, divulgación bilingüe, asistencia técnica y fortalecimiento de capacidades de los agricultores.",
    "eyebrow": "Naples, Florida &middot; Formación agrícola",
    "h1": "Formación agrícola práctica para productores resilientes",
    "lead": "AGRILEAD Training &amp; Consulting LLC ofrece formación agrícola práctica, apoyo en agronomía aplicada, divulgación bilingüe y fortalecimiento de capacidades para agricultores principiantes, pequeños productores, productores multilingües y comunidades agrícolas desatendidas.",
    "meta1": "Con sede en Naples, Florida",
    "meta2": "Divulgación bilingüe y multilingüe",
    "meta3": "Aprendizaje práctico, orientado al campo",
    "panel_cap": "Sesión de formación en el campo",
    "hero_alt": "Jardín en flor",
    "who_eyebrow": "Quiénes somos",
    "who_h2": "Un aprendizaje agrícola práctico y orientado al campo",
    "who_p1": "AGRILEAD Training &amp; Consulting LLC tiene su sede en Naples, Florida (Estados Unidos). La empresa busca apoyar un aprendizaje agrícola accesible, práctico y orientado al campo mediante formación, asistencia técnica, desarrollo de programas, divulgación bilingüe y fortalecimiento de capacidades centrado en la comunidad.",
    "who_p2": "AGRILEAD ayuda a productores, organizaciones y actores de la formación a definir sus necesidades prácticas de aprendizaje en áreas como la salud del suelo, la diversificación de cultivos, la agricultura climáticamente inteligente, la agronomía aplicada y la educación centrada en el agricultor.",
    "do_eyebrow": "Lo que hacemos",
    "do_h2": "Nuestras principales áreas de apoyo",
    "explore": [
      ("Servicios", "Formación agrícola, agronomía aplicada, materiales bilingües y asistencia técnica.", "services.html"),
      ("Iniciativa insignia", "Nuestra iniciativa bilingüe de formación de la fuerza laboral agrícola y de extensión.", "signature-initiative.html"),
      ("Colaboración", "Formas de explorar el trabajo conjunto con grupos de productores y organizaciones.", "collaboration-opportunities.html"),
      ("Blog", "Notas prácticas sobre salud del suelo, agronomía aplicada y educación del agricultor.", "blog.html"),
    ],
    "serve_eyebrow": "A quién servimos",
    "serve_h2": "Diseñado para los productores y las organizaciones que los apoyan",
    "serve_p": "AGRILEAD está diseñada para servir a una amplia gama de productores, grupos comunitarios y actores de la formación.",
    "approach_eyebrow": "Nuestro enfoque",
    "approach_h2": "Práctico, participativo y adaptable",
    "approach_p1": "AGRILEAD adopta un enfoque práctico, participativo, orientado al campo y adaptable. Las actividades de formación pueden incluir talleres, sesiones técnicas, fichas para agricultores, apoyo a programas, evaluación de necesidades, formación de formadores y conversaciones sobre formación piloto.",
    "approach_p2": "La empresa hace hincapié en el conocimiento práctico, el acceso lingüístico, la sostenibilidad, la colaboración, la documentación responsable y el aprendizaje centrado en el agricultor.",
    "sig_eyebrow": "Iniciativa insignia",
    "sig_h2": "Iniciativa AgriLead de formación bilingüe de la fuerza laboral agrícola y de extensión",
    "sig_p": "Una iniciativa en desarrollo enfocada en la formación agrícola práctica, la divulgación bilingüe, la asistencia técnica y el fortalecimiento de capacidades para agricultores principiantes, pequeños productores, productores inmigrantes y multilingües y comunidades agrícolas desatendidas.",
    "sig_learn": "Conocer más sobre la iniciativa",
    "sig_list": ["Talleres sobre salud del suelo y agronomía aplicada","Fichas y recursos de aprendizaje bilingües","Formación de formadores y divulgación comunitaria","Evaluación de necesidades y conversaciones de formación piloto"],
    "dl_eyebrow": "Materiales descargables",
    "dl_h2": "Resúmenes informativos",
    "dl_p": "Estos materiales son solo informativos. No representan alianzas confirmadas, respaldos, financiamiento, contratos, afiliaciones oficiales ni resultados garantizados.",
    "docs": [
      ("Resumen del proyecto (1 página)","Una visión concisa de la iniciativa, los públicos objetivo, las áreas de formación y posibles temas de conversación."),
      ("Folleto de la empresa","Un breve folleto institucional que presenta la empresa, los servicios, el enfoque y los datos de contacto."),
      ("Presentación de la iniciativa insignia","Una breve introducción a la Iniciativa AgriLead de formación bilingüe de la fuerza laboral agrícola y de extensión."),
    ],
    "cta_eyebrow": "Colaboración",
    "cta_h2": "¿Le interesa una formación agrícola práctica?",
    "cta_p": "AGRILEAD está disponible para hablar de posibles oportunidades de colaboración con organizaciones agrícolas, grupos de productores, instituciones comunitarias y actores de la formación.",
  },

  "who_we_serve": ["Agricultores principiantes","Pequeños productores","Productores inmigrantes y multilingües","Comunidades criollo/haitianas","Comunidades agrícolas hispanas","Comunidades rurales desatendidas","Comunidades de trabajadores agrícolas","Grupos de productores","Organizaciones agrícolas sin fines de lucro","Organizaciones comunitarias","Actores de la formación"],
  "values": [
    ("leaf","Conocimiento práctico","Un aprendizaje claro, útil y orientado al campo."),
    ("group","Formación centrada en el agricultor","Formación adaptada a las necesidades y realidades de los productores."),
    ("shield","Integridad","Una comunicación profesional, transparente y responsable."),
    ("globe","Inclusión y acceso lingüístico","Apoyo al aprendizaje bilingüe y multilingüe."),
    ("soil","Sostenibilidad","Énfasis en la salud del suelo, la resiliencia y la viabilidad a largo plazo de las explotaciones."),
  ],

  "about": {
    "title": "Acerca de AGRILEAD Training & Consulting LLC",
    "desc": "Conozca AGRILEAD Training & Consulting LLC, una empresa de formación y consultoría agrícola con sede en Florida que apoya la educación práctica de los agricultores y la divulgación bilingüe.",
    "eyebrow": "Acerca de AGRILEAD",
    "h1": "Un aprendizaje agrícola práctico y centrado en el agricultor",
    "lead": "AGRILEAD Training &amp; Consulting LLC es una empresa de formación y consultoría agrícola con sede en Florida, enfocada en la educación práctica, la agronomía aplicada, la divulgación bilingüe, la asistencia técnica, el desarrollo de programas y el fortalecimiento de capacidades de los productores.",
    "company_h2": "Acerca de la empresa",
    "company_p1": "AGRILEAD Training &amp; Consulting LLC tiene su sede en Naples, Florida (Estados Unidos). La empresa apoya un aprendizaje agrícola práctico y orientado al campo para agricultores, grupos de productores, organizaciones comunitarias y actores del sector agrícola.",
    "company_p2": "Su trabajo se centra en la agronomía aplicada, la asistencia técnica, la divulgación bilingüe y multilingüe, el desarrollo de programas, los materiales de formación y el fortalecimiento de capacidades &mdash; con el fin de hacer que el conocimiento agrícola sea más accesible, práctico y adaptable a las necesidades de los productores y las comunidades.",
    "panel_cap": "Entorno de aprendizaje agrícola",
    "mission_h3": "Misión",
    "mission_p": "AGRILEAD Training &amp; Consulting LLC ofrece formación agrícola práctica y orientada al campo, así como apoyo en agronomía aplicada, para fortalecer las capacidades de los agricultores principiantes, los pequeños productores y las comunidades agrícolas desatendidas, mediante una educación bilingüe y multilingüe centrada en la sostenibilidad, la productividad y la resiliencia.",
    "vision_h3": "Visión",
    "vision_p": "Contribuir a comunidades agrícolas más fuertes donde los agricultores principiantes, los pequeños productores y los cultivadores desatendidos tengan acceso a conocimientos prácticos, apoyo técnico y modelos de formación adaptables que apoyen los sistemas alimentarios locales y regionales.",
    "values_eyebrow": "Valores fundamentales",
    "values_h2": "Lo que guía nuestro trabajo",
    "founder_eyebrow": "Fundador",
    "founder_h2": "Perfil del fundador",
    "founder_cap": "Retrato del fundador",
    "founder_note": "Foto próximamente",
    "founder_name": "Wilbert Georges",
    "founder_role": "Fundador y Director ejecutivo",
    "founder_p1": "Wilbert Georges es el fundador y director ejecutivo de AGRILEAD Training &amp; Consulting LLC. Es un profesional del desarrollo agrícola con experiencia en formación de agricultores, agronomía aplicada, fortalecimiento de capacidades rurales, agricultura climáticamente inteligente, fortalecimiento de cooperativas e implementación de proyectos agrícolas.",
    "founder_p2": "Su trabajo se ha centrado en acompañar a grupos de productores y comunidades rurales mediante la formación práctica, la comunicación multilingüe y el fortalecimiento de capacidades orientado al campo. A través de AGRILEAD, está desarrollando una plataforma profesional para apoyar la formación agrícola, la divulgación bilingüe, la asistencia técnica y el desarrollo de programas.",
    "cta_h2": "Conozca nuestros servicios",
  },

  "services": {
    "title": "Servicios de formación y consultoría agrícola | AGRILEAD",
    "desc": "AGRILEAD ofrece formación agrícola, apoyo en agronomía aplicada, educación sobre salud del suelo, materiales bilingües, asistencia técnica y desarrollo de programas.",
    "eyebrow": "Servicios",
    "h1": "Servicios de formación y consultoría agrícola",
    "lead": "AGRILEAD ofrece formación agrícola práctica, apoyo en agronomía aplicada, asistencia técnica, desarrollo de programas y servicios de divulgación bilingüe para productores y organizaciones.",
    "intro": "Los servicios de AGRILEAD están diseñados para apoyar el aprendizaje práctico, el acompañamiento técnico y el fortalecimiento de capacidades de los productores. Pueden adaptarse según las necesidades de las organizaciones, los recursos disponibles y el alcance del trabajo acordado.",
    "core_eyebrow": "Servicios principales",
    "core_h2": "Áreas de apoyo disponibles para conversar",
    "list": [
      ("book","Formación agrícola","Talleres, cursos cortos y actividades de aprendizaje orientadas al campo para agricultores, grupos de productores y organizaciones comunitarias."),
      ("sprout","Apoyo en agronomía aplicada","Orientación sobre producción de cultivos, fertilidad del suelo, manejo de cultivos y prácticas agrícolas sostenibles."),
      ("soil","Educación sobre salud y fertilidad del suelo","Formación sobre materia orgánica, compostaje, manejo de nutrientes, conservación del suelo y planificación básica de la fertilidad."),
      ("leaf","Diversificación de cultivos","Apoyo educativo para la producción diversificada, la planificación de fincas, la reducción de riesgos y los sistemas de cultivo sostenibles."),
      ("climate","Agricultura climáticamente inteligente","Formación y temas de conversación sobre adaptación al clima, gestión de recursos y prácticas de producción resilientes."),
      ("wrench","Asistencia técnica","Apoyo a organizaciones agrícolas, grupos de productores e iniciativas comunitarias que buscan orientación agrícola práctica."),
      ("globe","Materiales de formación bilingües y multilingües","Fichas para agricultores, herramientas de divulgación, materiales de taller y recursos de aprendizaje diseñados para favorecer el acceso lingüístico."),
      ("group","Apoyo a la formación de formadores","Fortalecimiento de capacidades de facilitadores, líderes comunitarios y agentes de divulgación agrícola."),
      ("doc","Desarrollo de programas","Módulos de formación, planes de clase, guías para facilitadores y materiales de educación para agricultores."),
      ("chart","Seguimiento, evaluación y aprendizaje","Herramientas básicas para documentar las actividades de formación, recoger comentarios y apoyar la mejora del aprendizaje."),
    ],
    "note": "<strong>Nota.</strong> Los servicios pueden incluir las áreas anteriores y están disponibles para conversar según el alcance y los recursos. Las descripciones no implican alianza confirmada, financiamiento, contrato, afiliación oficial ni resultados garantizados, salvo acuerdo por escrito.",
    "cta_h2": "Solicitar una conversación sobre servicios",
  },

  "initiative": {
    "title": "Iniciativa AgriLead de formación bilingüe de la fuerza laboral agrícola y de extensión",
    "desc": "Conozca la iniciativa en desarrollo de AGRILEAD, enfocada en la formación agrícola bilingüe, la agronomía aplicada, la asistencia técnica y el fortalecimiento de capacidades de los agricultores.",
    "eyebrow": "Iniciativa insignia &middot; En desarrollo",
    "h1": "Iniciativa AgriLead de formación bilingüe de la fuerza laboral agrícola y de extensión",
    "lead": "Una iniciativa en desarrollo diseñada para apoyar la formación agrícola práctica, la divulgación bilingüe, la asistencia técnica y el fortalecimiento de capacidades de los agricultores.",
    "purpose_eyebrow": "Propósito",
    "purpose_h2": "Aprendizaje práctico y accesible lingüísticamente",
    "purpose_p1": "La Iniciativa AgriLead de formación bilingüe de la fuerza laboral agrícola y de extensión es una iniciativa en desarrollo enfocada en apoyar a los agricultores principiantes, los pequeños productores, los productores inmigrantes y multilingües y las comunidades agrícolas desatendidas, mediante formación práctica y recursos de aprendizaje accesibles lingüísticamente.",
    "purpose_p2": "Su propósito es apoyar la educación agrícola práctica, el aprendizaje de la agronomía aplicada, la divulgación bilingüe y el fortalecimiento de capacidades de los productores.",
    "panel_cap": "Educación agrícola multilingüe",
    "benef_eyebrow": "Beneficiarios objetivo",
    "benef_h2": "A quién está dirigida la iniciativa",
    "beneficiaries": ["Agricultores principiantes","Pequeños productores","Productores inmigrantes y multilingües","Comunidades criollo/haitianas","Comunidades agrícolas hispanas","Comunidades rurales desatendidas","Comunidades de trabajadores agrícolas","Grupos de productores","Organizaciones comunitarias"],
    "act_eyebrow": "Actividades posibles",
    "act_h2": "Lo que la iniciativa puede incluir",
    "activities": [
      ("soil","Formación en salud del suelo"),("sprout","Talleres de agronomía aplicada"),("leaf","Sesiones de diversificación de cultivos"),
      ("climate","Aprendizaje de agricultura climáticamente inteligente"),("globe","Fichas bilingües para agricultores"),("group","Apoyo a la formación de formadores"),
      ("chat","Divulgación comunitaria"),("list","Evaluación de necesidades"),("book","Conversaciones de formación piloto"),
    ],
    "model_eyebrow": "Modelo de formación",
    "model_h2": "Una plataforma flexible y modular",
    "model_p": "La iniciativa está concebida como una plataforma de formación flexible y modular. Los materiales y las actividades pueden adaptarse según las necesidades del público, el acceso lingüístico, el contexto geográfico, las prioridades agrícolas, los recursos disponibles y el alcance del trabajo acordado.",
    "model_note": "<strong>Nota importante.</strong> Esta iniciativa no implica alianzas confirmadas, respaldos, financiamiento, contratos, afiliaciones oficiales ni resultados garantizados, salvo acuerdo por escrito. Toda colaboración estaría sujeta a las políticas, prioridades, recursos, cronogramas y acuerdos formales de las organizaciones.",
    "cta_h2": "Hablar de una posible actividad de formación",
  },

  "collab": {
    "title": "Oportunidades de colaboración | AGRILEAD Training & Consulting LLC",
    "desc": "Explore oportunidades de colaboración con AGRILEAD en formación agrícola, apoyo en agronomía aplicada, divulgación bilingüe, asistencia técnica y fortalecimiento de capacidades.",
    "eyebrow": "Colaboración",
    "h1": "Oportunidades de colaboración",
    "lead": "Explore oportunidades de formación, divulgación y asistencia técnica con AGRILEAD Training &amp; Consulting LLC.",
    "plat_eyebrow": "Una plataforma profesional",
    "plat_h2": "Disponible para conversar sobre el aprendizaje agrícola práctico",
    "plat_p1": "AGRILEAD Training &amp; Consulting LLC está disponible para hablar de posibles oportunidades de colaboración con organizaciones agrícolas, instituciones comunitarias, grupos de productores y actores de la formación interesados en la educación agrícola práctica, el apoyo en agronomía aplicada, la divulgación bilingüe y el fortalecimiento de capacidades.",
    "plat_p2": "Toda colaboración estaría sujeta a las políticas, prioridades, recursos, cronogramas y acuerdos formales de las organizaciones.",
    "for_eyebrow": "A quién está dirigida esta página",
    "for_h2": "Organizaciones y grupos con los que podemos trabajar",
    "for_p": "Esta página está dirigida a organizaciones y grupos que puedan estar interesados en la formación agrícola práctica, la asistencia técnica, la divulgación bilingüe o el aprendizaje centrado en el agricultor.",
    "for_whom": ["Programas para agricultores principiantes","Grupos de pequeños productores","Organizaciones agrícolas sin fines de lucro","Organizaciones comunitarias","Organizaciones de trabajadores agrícolas y rurales","Instituciones de formación","Asociaciones de productores","Grupos que atienden a productores multilingües","Comunidades criollo/haitianas","Comunidades agrícolas hispanas"],
    "ways_eyebrow": "Posibles oportunidades de colaboración",
    "ways_h2": "Formas de explorar una colaboración",
    "ways": [
      ("doc","Revisión de programas","Revisión o comentarios sobre contenidos prácticos de formación agrícola."),
      ("book","Diseño de talleres","Conversar sobre posibles temas, formatos y necesidades del público."),
      ("chat","Apoyo a la divulgación comunitaria","Explorar formas de comunicar las oportunidades de educación agrícola a las comunidades de productores multilingües."),
      ("sprout","Comentarios técnicos","Conversar sobre temas de agronomía aplicada como la salud del suelo, la diversificación de cultivos, las prácticas climáticamente inteligentes y el fortalecimiento de capacidades."),
      ("group","Conversaciones sobre formación de formadores","Explorar si los facilitadores locales, líderes comunitarios o agentes de divulgación podrían beneficiarse de un apoyo estructurado."),
      ("list","Evaluación de necesidades","Identificar las necesidades de formación, las barreras de acceso lingüístico y las prioridades de aprendizaje de los grupos de productores."),
      ("hands","Conversaciones de formación piloto","Explorar si una sesión de formación a pequeña escala sería apropiada, sujeto a los recursos y acuerdos formales."),
    ],
    "note": "<strong>Nota importante sobre la colaboración.</strong> Una posible colaboración no implica alianza confirmada, respaldo, financiamiento, contrato, afiliación oficial ni resultados garantizados, salvo acuerdo por escrito. AGRILEAD no se presenta como representante oficial, afiliado o socio de ninguna agencia pública, universidad, oficina de extensión, organización sin fines de lucro o institución externa, salvo que dicha relación esté formalmente documentada.",
    "cta_h2": "Hablar de una posible colaboración",
  },

  "contact": {
    "title": "Contactar a AGRILEAD Training & Consulting LLC",
    "desc": "Contacte a AGRILEAD Training & Consulting LLC para hablar de formación agrícola, agronomía aplicada, divulgación bilingüe, asistencia técnica o desarrollo de programas.",
    "eyebrow": "Contacto",
    "h1": "Contactar a AGRILEAD Training &amp; Consulting LLC",
    "lead": "AGRILEAD está disponible para hablar de formación, asistencia técnica, desarrollo de programas, divulgación bilingüe y oportunidades de colaboración.",
    "info_h2": "Datos de contacto",
    "l_location": "Ubicación", "v_location": "Naples, Florida, Estados Unidos",
    "l_phone": "Teléfono", "l_email": "Correo electrónico", "l_website": "Sitio web",
    "topics_h3": "Temas de la solicitud",
    "topics": ["Formación agrícola","Apoyo en agronomía aplicada","Educación sobre salud del suelo","Diversificación de cultivos","Agricultura climáticamente inteligente","Asistencia técnica","Divulgación bilingüe","Desarrollo de programas","Apoyo a la formación de formadores","Oportunidades de colaboración"],
    "form_h2": "Enviar una solicitud",
    "f_name": "Nombre", "f_org": "Organización", "f_optional": "(opcional)",
    "f_role": "Cargo / Título", "f_email": "Correo electrónico", "f_phone": "Teléfono", "f_location": "Ubicación",
    "f_orgtype": "Tipo de organización", "f_area": "Área de interés",
    "f_select": "Seleccione", "f_message": "Mensaje",
    "f_followup": "Método de seguimiento preferido",
    "org_types": ["Organización agrícola","Organización comunitaria","Grupo de productores","Institución de formación","Organización de trabajadores agrícolas o rural","Programa de pequeña finca","Otro"],
    "areas": ["Formación agrícola","Apoyo en agronomía aplicada","Educación sobre salud del suelo","Diversificación de cultivos","Agricultura climáticamente inteligente","Divulgación bilingüe","Desarrollo de programas","Formación de formadores","Asistencia técnica","Colaboración potencial","Otro"],
    "followups": ["Correo electrónico","Teléfono","Sin preferencia"],
    "submit": "Enviar una solicitud",
    "form_note": "El envío de una solicitud no crea ninguna alianza, contrato, compromiso de financiamiento ni afiliación formal.",
  },

  "thankyou": {
    "title": "Gracias | AGRILEAD Training & Consulting LLC",
    "desc": "Su solicitud a AGRILEAD Training & Consulting LLC se ha recibido correctamente.",
    "h1": "Gracias &mdash; su solicitud se ha recibido",
    "p": "Le agradecemos su mensaje. AGRILEAD revisará su solicitud y le dará seguimiento según corresponda. El envío de una solicitud no crea ninguna alianza, contrato, compromiso de financiamiento ni afiliación formal.",
    "back": "Volver al inicio",
  },

  "privacy": {
    "title": "Política de privacidad | AGRILEAD Training & Consulting LLC",
    "desc": "Política de privacidad de AGRILEAD Training & Consulting LLC.",
    "eyebrow": "Privacidad",
    "h1": "Política de privacidad",
    "updated": "Última actualización:",
    "updated_note": "Esta es una plantilla general y debe revisarse antes de su publicación final.",
    "s1_h": "Información que recopilamos",
    "s1_p": "Cuando usted envía el formulario de contacto de este sitio, AGRILEAD Training &amp; Consulting LLC recopila la información que decide proporcionar, como su nombre, organización, cargo, correo electrónico, teléfono, ubicación, tipo de organización, área de interés, mensaje y método de seguimiento preferido.",
    "s2_h": "Cómo la usamos",
    "s2_p": "La información se utiliza únicamente para responder a su solicitud y para hablar de una posible formación, asistencia técnica o colaboración. AGRILEAD no vende su información.",
    "s3_h": "Cómo funciona el formulario",
    "s3_p": "El formulario de contacto de este sitio se procesa a través del servicio de formularios del proveedor de alojamiento del sitio. Las solicitudes pueden ser almacenadas por dicho proveedor para entregar su mensaje a AGRILEAD.",
    "s4_h": "Sus opciones",
    "s4_p": "Puede solicitar a AGRILEAD que actualice o elimine la información que envió escribiéndonos a [Email].",
    "s5_h": "Contacto",
    "s5_p": "Las preguntas sobre esta política pueden enviarse a [Email], AGRILEAD Training &amp; Consulting LLC, Naples, Florida, Estados Unidos.",
    "locale": "es-ES",
  },

  "blog": {
    "title": "Blog | AGRILEAD Training & Consulting LLC",
    "desc": "Artículos prácticos sobre formación agrícola, agronomía aplicada y educación bilingüe de agricultores de AGRILEAD Training & Consulting LLC.",
    "eyebrow": "Análisis y novedades",
    "h1": "Blog de AGRILEAD",
    "intro": "Notas prácticas sobre formación agrícola, agronomía aplicada y aprendizaje accesible lingüísticamente, para agricultores principiantes, pequeños productores y las organizaciones que los apoyan.",
    "more": "Pronto habrá más artículos. ¿Hay algún tema que le gustaría que tratáramos? <a href=\"contact.html\">Contáctenos</a>.",
    "posts": [
      ("blog-soil-health-starter.html","Agronomía aplicada","Cinco hábitos prácticos para un suelo agrícola más sano","1 de julio de 2026","4 min de lectura","Prácticas sencillas y de bajo costo — mantener el suelo cubierto, reducir la labranza, aumentar la materia orgánica, analizar antes de tratar y mantener raíces vivas — que los productores principiantes y pequeños pueden adoptar esta temporada."),
    ],
  },

  "article": {
    "title": "Cinco hábitos prácticos para un suelo agrícola más sano | AGRILEAD",
    "desc": "Cinco prácticas sencillas y de bajo costo para la salud del suelo: cobertura del suelo, menor labranza, materia orgánica, análisis de suelo y raíces vivas.",
    "cat": "Agronomía aplicada",
    "h1": "Cinco hábitos prácticos para un suelo agrícola más sano",
    "meta": "1 de julio de 2026 &middot; 4 min de lectura",
    "intro": "Un suelo sano es la base de una finca resiliente. Retiene el agua, alimenta los cultivos, resiste la erosión y se recupera más rápido tras una temporada difícil. La buena noticia para los productores principiantes y pequeños es que un mejor suelo rara vez requiere equipos costosos: proviene de unos pocos hábitos constantes practicados con el tiempo.",
    "h1_1": "1. Mantener el suelo cubierto",
    "p_1": "El suelo desnudo se recuece al sol, se encostra y se lava con las lluvias fuertes. Los cultivos de cobertura, los residuos de cultivo o el mantillo protegen la superficie, moderan la temperatura del suelo y alimentan la vida del suelo. Incluso una cobertura sencilla entre cultivos ayuda.",
    "h1_2": "2. Alterar menos el suelo",
    "p_2": "Una labranza frecuente y profunda destruye la estructura del suelo y consume la materia orgánica. Cuando sea posible, reducir la labranza ayuda a mantener intactos los canales naturales del suelo para que el agua y las raíces circulen libremente.",
    "h1_3": "3. Aumentar la materia orgánica",
    "p_3": "El compost, el estiércol bien manejado y los residuos de cultivo restituidos aportan materia orgánica, lo que mejora la capacidad de retención de agua y la disponibilidad de nutrientes. Los aportes pequeños y regulares se suman temporada tras temporada.",
    "h1_4": "4. Analizar antes de tratar",
    "p_4": "Un análisis básico de suelo elimina las conjeturas sobre la fertilidad. Conocer el pH y los niveles de nutrientes de su suelo le ayuda a aplicar lo que la parcela realmente necesita y a evitar gastar en lo que no.",
    "h1_5": "5. Mantener raíces vivas en el suelo",
    "p_5": "Las raíces vivas alimentan a los microorganismos que construyen un suelo sano. Las rotaciones y los cultivos de cobertura que mantienen algo creciendo durante más tiempo del año apoyan a esa comunidad subterránea y ayudan a romper los ciclos de plagas y enfermedades.",
    "disclaimer": "Este artículo ofrece información educativa general y no sustituye el asesoramiento técnico adaptado al sitio. Las prácticas y los resultados varían según el tipo de suelo, el clima, el cultivo y el manejo.",
    "back": "&larr; Volver a todos los artículos",
  },
 },
}


# ===========================================================================
# PAGE BUILDER (one language)
# ===========================================================================
def build(lang):
    d = CONTENT[lang]
    form_name = "contact" if lang == "en" else "contact-" + lang
    form_action = "/thank-you.html" if lang == "en" else f"/{lang}/thank-you.html"

    # ---- HOME ----
    h = d["home"]
    explore_grid = '<div class="linkgrid">' + "".join(
        f'<div class="lg-item reveal"><a class="lg-title" href="{href}">{title} {ICONS["arrow"]}</a><p>{desc}</p></div>'
        for title, desc, href in h["explore"]) + '</div>'
    sig_list = "".join(f'<li>{ICONS["check"]}{x}</li>' for x in h["sig_list"])
    docs = "".join(
        f'<div class="doc-card reveal"><span class="icon icon--navy">{ICONS["doc"]}</span>'
        f'<h3>{t}</h3><p>{b}</p>'
        f'<a class="link-arrow" href="#" aria-disabled="true">{d["download_soon"]}</a></div>'
        for t, b in h["docs"])
    home = f'''
<section class="hero hero--banner">
  <div class="hero-banner-media">
    <img src="/assets/img/home_hero.jpg" alt="{h["hero_alt"]}" loading="eager" decoding="async">
  </div>
  <div class="container hero-banner-inner">
    <p class="eyebrow">{h["eyebrow"]}</p>
    <h1>{h["h1"]}</h1>
  </div>
</section>

<section class="section section--tight">
  <div class="container narrow center">
    <p class="lead-statement">{h["lead"]}</p>
    <div class="hero-cta" style="justify-content:center">
      <a class="btn btn--primary" href="services.html">{d["cta_services"]} {ICONS["arrow"]}</a>
      <a class="btn btn--secondary" href="contact.html">{d["cta_contact"]}</a>
    </div>
    <div class="hero-meta" style="justify-content:center">
      <div>{ICONS["pin"]}<span>{h["meta1"]}</span></div>
      <div>{ICONS["globe"]}<span>{h["meta2"]}</span></div>
      <div>{ICONS["sprout"]}<span>{h["meta3"]}</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">{h["who_eyebrow"]}</p>
      <h2>{h["who_h2"]}</h2>
    </div>
    <div class="grid grid-2">
      <p class="reveal">{h["who_p1"]}</p>
      <p class="reveal">{h["who_p2"]}</p>
    </div>
  </div>
</section>

<section class="section section--field">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">{h["do_eyebrow"]}</p>
      <h2>{h["do_h2"]}</h2>
    </div>
    {explore_grid}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">{h["serve_eyebrow"]}</p>
      <h2>{h["serve_h2"]}</h2>
      <p>{h["serve_p"]}</p>
    </div>
    <div class="reveal">{pills_block(d["who_we_serve"])}</div>
  </div>
</section>

<section class="section section--field">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;gap:clamp(2rem,5vw,4rem)">
      <div class="reveal">
        <p class="eyebrow">{h["approach_eyebrow"]}</p>
        <h2>{h["approach_h2"]}</h2>
        <p>{h["approach_p1"]}</p>
        <p>{h["approach_p2"]}</p>
      </div>
      <div class="reveal">{values_block(d["values"])}</div>
    </div>
  </div>
</section>

<section class="section band">
  <div class="container band-grid">
    <div class="reveal">
      <p class="eyebrow">{h["sig_eyebrow"]}</p>
      <h2>{h["sig_h2"]}</h2>
      <p>{h["sig_p"]}</p>
      <div class="hero-cta">
        <a class="btn btn--ghost-light" href="signature-initiative.html">{h["sig_learn"]} {ICONS["arrow"]}</a>
      </div>
    </div>
    <ul class="mini-list reveal">
      {sig_list}
    </ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">{h["dl_eyebrow"]}</p>
      <h2>{h["dl_h2"]}</h2>
      <p>{h["dl_p"]}</p>
    </div>
    <div class="grid grid-3">
      {docs}
    </div>
  </div>
</section>

<section class="section section--field cta-strip">
  <div class="container">
    <p class="eyebrow" style="justify-content:center">{h["cta_eyebrow"]}</p>
    <h2>{h["cta_h2"]}</h2>
    <p class="narrow" style="margin-inline:auto">{h["cta_p"]}</p>
    <div class="hero-cta">
      <a class="btn btn--primary" href="collaboration-opportunities.html">{d["cta_collab"]}</a>
      <a class="btn btn--secondary" href="contact.html">{d["cta_contact"]}</a>
    </div>
  </div>
</section>
'''
    page("index.html", h["title"], h["desc"], "index.html", home, lang)

    # ---- ABOUT ----
    a = d["about"]
    about = f'''
{banner(a["eyebrow"], a["h1"], "/assets/img/about_banner.jpg", a["h1"])}

<section class="section section--tight">
  <div class="container narrow center">
    <p class="hero-lead reveal" style="margin-inline:auto">{a["lead"]}</p>
  </div>
</section>

<section class="section section--field">
  <div class="container grid grid-2" style="gap:clamp(2rem,5vw,4rem)">
    <div class="reveal">
      <h2>{a["company_h2"]}</h2>
      <p>{a["company_p1"]}</p>
      <p>{a["company_p2"]}</p>
    </div>
    <div class="reveal">{field_panel(a["panel_cap"], img="/assets/img/about_side.jpg", alt=a["panel_cap"])}</div>
  </div>
</section>

<section class="section">
  <div class="container grid grid-2" style="gap:1.4rem">
    <article class="card reveal"><span class="icon">{ICONS["compass"]}</span><h3>{a["mission_h3"]}</h3><p>{a["mission_p"]}</p></article>
    <article class="card reveal"><span class="icon icon--navy">{ICONS["sprout"]}</span><h3>{a["vision_h3"]}</h3><p>{a["vision_p"]}</p></article>
  </div>
</section>

<section class="section section--field">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">{a["values_eyebrow"]}</p><h2>{a["values_h2"]}</h2></div>
    <div class="reveal">{values_block(d["values"])}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">{a["founder_eyebrow"]}</p><h2>{a["founder_h2"]}</h2></div>
    <div class="founder">
      <div class="reveal">{field_panel(a["founder_cap"], img="/assets/img/founder.jpg", alt=a["founder_name"])}</div>
      <div class="reveal">
        <h3>{a["founder_name"]}</h3>
        <p class="role">{a["founder_role"]}</p>
        <p>{a["founder_p1"]}</p>
        <p>{a["founder_p2"]}</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--field cta-strip">
  <div class="container">
    <h2>{a["cta_h2"]}</h2>
    <div class="hero-cta">
      <a class="btn btn--primary" href="services.html">{d["cta_services"]}</a>
      <a class="btn btn--secondary" href="contact.html">{d["cta_contact"]}</a>
    </div>
  </div>
</section>
'''
    page("about.html", a["title"], a["desc"], "about.html", about, lang)

    # ---- SERVICES ----
    s = d["services"]
    svc_items = ""
    for icon, title, body in s["list"]:
        svc_items += (f'<div class="svc-item reveal"><span class="icon">{ICONS[icon]}</span>'
                      f'<div><h3>{title}</h3><p>{body}</p></div></div>')
    services = f'''
{banner(s["eyebrow"], s["h1"], "/assets/img/services_banner.jpg", s["h1"])}

<section class="section section--tight">
  <div class="container narrow center">
    <p class="hero-lead reveal" style="margin-inline:auto">{s["lead"]}</p>
  </div>
</section>

<section class="section section--field section--tight">
  <div class="container narrow">
    <p class="reveal" style="margin:0">{s["intro"]}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">{s["core_eyebrow"]}</p><h2>{s["core_h2"]}</h2></div>
    <div class="svc">{svc_items}</div>
  </div>
</section>

<section class="section section--field">
  <div class="container">{notice(s["note"])}</div>
</section>

<section class="section cta-strip">
  <div class="container">
    <h2>{s["cta_h2"]}</h2>
    <div class="hero-cta">
      <a class="btn btn--primary" href="collaboration-opportunities.html">{d["cta_collab"]}</a>
      <a class="btn btn--secondary" href="contact.html">{d["cta_contact"]}</a>
    </div>
  </div>
</section>
'''
    page("services.html", s["title"], s["desc"], "services.html", services, lang)

    # ---- SIGNATURE INITIATIVE ----
    i = d["initiative"]
    act_cards = '<div class="grid grid-3">'
    for icon, label in i["activities"]:
        act_cards += (f'<div class="card reveal" style="padding:1.3rem 1.4rem">'
                      f'<span class="icon" style="width:40px;height:40px;margin-bottom:.7rem">{ICONS[icon]}</span>'
                      f'<h3 style="font-size:1.02rem;margin:0">{label}</h3></div>')
    act_cards += '</div>'
    initiative = f'''
{banner(i["eyebrow"], i["h1"], "/assets/img/signature_banner.jpg", i["h1"])}

<section class="section section--tight">
  <div class="container narrow center">
    <p class="hero-lead reveal" style="margin-inline:auto">{i["lead"]}</p>
  </div>
</section>

<section class="section section--field">
  <div class="container grid grid-2" style="gap:clamp(2rem,5vw,4rem)">
    <div class="reveal">
      <p class="eyebrow">{i["purpose_eyebrow"]}</p>
      <h2>{i["purpose_h2"]}</h2>
      <p>{i["purpose_p1"]}</p>
      <p>{i["purpose_p2"]}</p>
    </div>
    <div class="reveal">{field_panel(i["panel_cap"], img="/assets/img/signature_side.jpg", alt=i["panel_cap"])}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">{i["benef_eyebrow"]}</p><h2>{i["benef_h2"]}</h2></div>
    <div class="reveal">{pills_block(i["beneficiaries"])}</div>
  </div>
</section>

<section class="section section--field">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">{i["act_eyebrow"]}</p><h2>{i["act_h2"]}</h2></div>
    {act_cards}
  </div>
</section>

<section class="section">
  <div class="container grid grid-2" style="gap:clamp(2rem,5vw,4rem);align-items:center">
    <div class="reveal">
      <p class="eyebrow">{i["model_eyebrow"]}</p>
      <h2>{i["model_h2"]}</h2>
      <p>{i["model_p"]}</p>
    </div>
    <div class="reveal">{notice(i["model_note"])}</div>
  </div>
</section>

<section class="section band cta-strip">
  <div class="container">
    <h2>{i["cta_h2"]}</h2>
    <div class="hero-cta">
      <a class="btn btn--ghost-light" href="collaboration-opportunities.html">{d["cta_collab"]}</a>
      <a class="btn btn--ghost-light" href="contact.html">{d["cta_contact"]}</a>
    </div>
  </div>
</section>
'''
    page("signature-initiative.html", i["title"], i["desc"], "signature-initiative.html", initiative, lang)

    # ---- COLLABORATION ----
    c = d["collab"]
    collab_items = ""
    for icon, title, body in c["ways"]:
        collab_items += (f'<div class="svc-item reveal"><span class="icon">{ICONS[icon]}</span>'
                         f'<div><h3>{title}</h3><p>{body}</p></div></div>')
    collaboration = f'''
{banner(c["eyebrow"], c["h1"], "/assets/img/collab_banner.jpg", c["h1"])}

<section class="section section--tight">
  <div class="container narrow center">
    <p class="hero-lead reveal" style="margin-inline:auto">{c["lead"]}</p>
  </div>
</section>

<section class="section section--field">
  <div class="container narrow">
    <p class="eyebrow reveal">{c["plat_eyebrow"]}</p>
    <h2 class="reveal">{c["plat_h2"]}</h2>
    <p class="reveal">{c["plat_p1"]}</p>
    <p class="reveal">{c["plat_p2"]}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">{c["for_eyebrow"]}</p><h2>{c["for_h2"]}</h2>
    <p>{c["for_p"]}</p></div>
    <div class="reveal">{pills_block(c["for_whom"])}</div>
  </div>
</section>

<section class="section section--field">
  <div class="container">
    <div class="section-head reveal"><p class="eyebrow">{c["ways_eyebrow"]}</p><h2>{c["ways_h2"]}</h2></div>
    <div class="svc">{collab_items}</div>
  </div>
</section>

<section class="section">
  <div class="container">{notice(c["note"])}</div>
</section>

<section class="section section--field cta-strip">
  <div class="container">
    <h2>{c["cta_h2"]}</h2>
    <div class="hero-cta">
      <a class="btn btn--primary" href="contact.html">{d["cta_submit"]}</a>
      <a class="btn btn--secondary" href="contact.html">{d["cta_contact"]}</a>
    </div>
  </div>
</section>
'''
    page("collaboration-opportunities.html", c["title"], c["desc"], "collaboration-opportunities.html", collaboration, lang)

    # ---- CONTACT ----
    ct = d["contact"]
    topics_list = "".join(f'<li>{ICONS["check"]}<span>{t}</span></li>' for t in ct["topics"])
    followup_opts = "".join(f'<option>{x}</option>' for x in ct["followups"])
    contact = f'''
{banner(ct["eyebrow"], ct["h1"], "/assets/img/contact_banner.jpg", ct["h1"])}

<section class="section section--tight">
  <div class="container narrow center">
    <p class="hero-lead reveal" style="margin-inline:auto">{ct["lead"]}</p>
  </div>
</section>

<section class="section">
  <div class="container contact-grid">
    <div class="reveal">
      <img class="contact-photo" src="/assets/img/contact_vertical.jpg" alt="{ct["eyebrow"]} AGRILEAD" loading="lazy" decoding="async">
      <h2 style="font-size:1.35rem">{ct["info_h2"]}</h2>
      <div class="info-row"><span class="icon icon--navy">{ICONS["pin"]}</span><div><p class="label">{ct["l_location"]}</p><p class="val">{ct["v_location"]}</p></div></div>
      <div class="info-row"><span class="icon icon--navy">{ICONS["phone"]}</span><div><p class="label">{ct["l_phone"]}</p><p class="val">[Phone]</p></div></div>
      <div class="info-row"><span class="icon icon--navy">{ICONS["mail"]}</span><div><p class="label">{ct["l_email"]}</p><p class="val">[Email]</p></div></div>
      <div class="info-row"><span class="icon icon--navy">{ICONS["globe"]}</span><div><p class="label">{ct["l_website"]}</p><p class="val">[Website]</p></div></div>

      <h3 style="margin-top:2rem;font-size:1.1rem">{ct["topics_h3"]}</h3>
      <ul class="footer-contact" style="gap:.55rem;margin-top:.8rem">{topics_list}</ul>
    </div>

    <div class="reveal">
      <h2 style="font-size:1.35rem">{ct["form_h2"]}</h2>
      <form class="form" name="{form_name}" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="{form_action}">
        <input type="hidden" name="form-name" value="{form_name}">
        <p class="hp"><label>Do not fill this out: <input name="bot-field"></label></p>

        <div class="form-row">
          <div class="field"><label for="name">{ct["f_name"]}</label><input id="name" name="name" type="text" required></div>
          <div class="field"><label for="org">{ct["f_org"]} <span class="opt">{ct["f_optional"]}</span></label><input id="org" name="organization" type="text"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="role">{ct["f_role"]} <span class="opt">{ct["f_optional"]}</span></label><input id="role" name="role" type="text"></div>
          <div class="field"><label for="email">{ct["f_email"]}</label><input id="email" name="email" type="email" required></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="phone">{ct["f_phone"]} <span class="opt">{ct["f_optional"]}</span></label><input id="phone" name="phone" type="tel"></div>
          <div class="field"><label for="location">{ct["f_location"]} <span class="opt">{ct["f_optional"]}</span></label><input id="location" name="location" type="text"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="orgtype">{ct["f_orgtype"]}</label><select id="orgtype" name="organization_type"><option value="" selected disabled>{ct["f_select"]}</option>{options(ct["org_types"])}</select></div>
          <div class="field"><label for="area">{ct["f_area"]}</label><select id="area" name="area_of_interest"><option value="" selected disabled>{ct["f_select"]}</option>{options(ct["areas"])}</select></div>
        </div>
        <div class="field"><label for="message">{ct["f_message"]}</label><textarea id="message" name="message" required></textarea></div>
        <div class="field"><label for="followup">{ct["f_followup"]} <span class="opt">{ct["f_optional"]}</span></label><select id="followup" name="preferred_followup"><option value="" selected disabled>{ct["f_select"]}</option>{followup_opts}</select></div>

        <button class="btn btn--primary" type="submit">{ct["submit"]}</button>
        <p class="form-note">{ct["form_note"]}</p>
      </form>
    </div>
  </div>
</section>
'''
    page("contact.html", ct["title"], ct["desc"], "contact.html", contact, lang)

    # ---- THANK YOU ----
    ty = d["thankyou"]
    thankyou = f'''
<section class="section" style="min-height:52vh;display:flex;align-items:center">
  <div class="container narrow center">
    <span class="icon" style="width:64px;height:64px;margin-inline:auto">{ICONS["check"]}</span>
    <h1 style="margin-top:1.2rem">{ty["h1"]}</h1>
    <p>{ty["p"]}</p>
    <div class="hero-cta" style="justify-content:center">
      <a class="btn btn--primary" href="index.html">{ty["back"]}</a>
      <a class="btn btn--secondary" href="services.html">{d["cta_services"]}</a>
    </div>
  </div>
</section>
'''
    page("thank-you.html", ty["title"], ty["desc"], "", thankyou, lang)

    # ---- PRIVACY ----
    pv = d["privacy"]
    privacy = f'''
<section class="section section--tight">
  <div class="container narrow">
    <p class="eyebrow">{pv["eyebrow"]}</p>
    <h1>{pv["h1"]}</h1>
    <p class="form-note">{pv["updated"]} <span id="pdate"></span>. {pv["updated_note"]}</p>

    <h3 style="margin-top:2rem">{pv["s1_h"]}</h3>
    <p>{pv["s1_p"]}</p>

    <h3>{pv["s2_h"]}</h3>
    <p>{pv["s2_p"]}</p>

    <h3>{pv["s3_h"]}</h3>
    <p>{pv["s3_p"]}</p>

    <h3>{pv["s4_h"]}</h3>
    <p>{pv["s4_p"]}</p>

    <h3>{pv["s5_h"]}</h3>
    <p>{pv["s5_p"]}</p>
  </div>
</section>
<script>document.getElementById("pdate").textContent = new Date().toLocaleDateString("{pv["locale"]}",{{year:"numeric",month:"long",day:"numeric"}});</script>
'''
    page("privacy.html", pv["title"], pv["desc"], "", privacy, lang)

    # ---- BLOG ----
    bl = d["blog"]
    blog = f'''
{banner(bl["eyebrow"], bl["h1"], "/assets/img/blog_banner.jpg", bl["h1"])}

<section class="section section--tight">
  <div class="container">
    <p class="hero-lead reveal" style="max-width:70ch">{bl["intro"]}</p>
    {post_cards(bl["posts"], d["read_article"])}
    <div class="notice reveal" style="margin-top:2.2rem">{bl["more"]}</div>
  </div>
</section>
'''
    page("blog.html", bl["title"], bl["desc"], "blog.html", blog, lang)

    # ---- ARTICLE ----
    ar = d["article"]
    article = f'''
<article class="section section--tight">
  <div class="container narrow">
    <p class="eyebrow">{ar["cat"]}</p>
    <h1>{ar["h1"]}</h1>
    <p class="form-note">{ar["meta"]}</p>

    <p>{ar["intro"]}</p>

    <h3 style="margin-top:2rem">{ar["h1_1"]}</h3>
    <p>{ar["p_1"]}</p>

    <h3>{ar["h1_2"]}</h3>
    <p>{ar["p_2"]}</p>

    <h3>{ar["h1_3"]}</h3>
    <p>{ar["p_3"]}</p>

    <h3>{ar["h1_4"]}</h3>
    <p>{ar["p_4"]}</p>

    <h3>{ar["h1_5"]}</h3>
    <p>{ar["p_5"]}</p>

    <p class="footer-disclaimer" style="margin-top:2.2rem">{ar["disclaimer"]}</p>

    <p style="margin-top:1.6rem"><a href="blog.html">{ar["back"]}</a></p>
  </div>
</article>
'''
    page("blog-soil-health-starter.html", ar["title"], ar["desc"], "blog.html", article, lang)


for _lang in ("en", "fr", "es"):
    build(_lang)

print("ALL PAGES BUILT")
