# AGRILEAD Training & Consulting LLC — Website

A static, English-only marketing website for **AGRILEAD Training & Consulting LLC**
(Naples, Florida). Built with plain HTML, CSS, and a little JavaScript — no build
step, no framework — so it deploys anywhere and is easy to hand to any developer.

Brand, colors, typography, page structure, and cautionary language follow the
approved content handoff document.

---

## Pages

| File | Page |
|------|------|
| `index.html` | Home |
| `about.html` | About (company + founder profile) |
| `services.html` | Services (10 core services) |
| `signature-initiative.html` | Signature Initiative |
| `collaboration-opportunities.html` | Collaboration Opportunities |
| `contact.html` | Contact (with working Netlify form) |
| `thank-you.html` | Form confirmation page |
| `privacy.html` | Privacy Policy |

Shared assets live in `assets/` (`css/styles.css`, `js/main.js`, `img/favicon.svg`).

---

## Deploy to Netlify via GitHub

1. **Create a GitHub repository** and push these files to it:
   ```bash
   git init
   git add .
   git commit -m "AGRILEAD website — initial version"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/agrilead-website.git
   git push -u origin main
   ```
2. **Connect it to Netlify:** log in at netlify.com → *Add new site* → *Import an
   existing project* → pick GitHub → select the repo.
3. **Build settings:** leave the build command **empty** and set the publish
   directory to **`.`** (the repo root). `netlify.toml` already sets this.
4. Click **Deploy**. Netlify gives you a temporary `*.netlify.app` address.
5. **Custom domain:** *Domain settings* → *Add a custom domain*, then point your
   domain's DNS to Netlify (Netlify walks you through it).

Any future `git push` to `main` re-deploys automatically.

---

## The contact form (already working)

The form on `contact.html` uses **Netlify Forms** — no server or code needed.
Once the site is on Netlify:

- Submissions appear under **Forms** in the Netlify dashboard.
- To get email alerts: *Site settings → Forms → Form notifications → add your email.*
- A hidden honeypot field reduces spam automatically.

The form is only processed when hosted on Netlify (it won't submit from a local
file preview — that's expected).

---

## Preview locally

Just open `index.html` in a browser, or run a tiny local server:
```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

---

## Before you launch

See **`HANDOFF-CHECKLIST.md`** — it lists every placeholder to replace
(phone, email, website, logo, photos) and the do-not-use language rules.

## Regenerating the pages (optional)

`_build_base.py` and `_build_pages.py` are the generator that produced the HTML,
kept so headers/footers stay identical across pages. You do **not** need them to
run the site. To regenerate after editing content: `python3 _build_pages.py`.
If you prefer, you can delete both `.py` files and edit the HTML directly.
