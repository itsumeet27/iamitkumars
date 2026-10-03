# Dr. Amit Kumar Sharma

Static website for Dr. Amit Kumar Sharma, Materials Chemist. Built with HTML, CSS, and JavaScript so it can be served from Hostinger shared hosting with no build step and no database.

## Pages

- Home
- About
- Research
- Publications
- Contact — `iamitkumars@gmail.com`

## Run locally

```bash
python3 -m http.server 8080
```

Open `http://localhost:8080/`.

## Live site on GitHub Pages

Every push to `main` runs `.github/workflows/deploy-pages.yml` and republishes the site, the same pattern used for White Fox Creations.

After this repository’s first merge to `main`, GitHub Pages must use **GitHub Actions** as the source (Settings → Pages). The workflow then updates the live site on each later push to `main`.

## Hostinger Basic plan

The Basic plan includes FTP and does not include the Git or web-app connection in hPanel. `.github/workflows/deploy-hostinger.yml` uploads the site over FTP on every push to `main`. Hostinger never has to reach GitHub.

The site must be a custom PHP/HTML website. Hostinger does not open FTP for a site made with the AI website builder.

One-time setup:

1. In hPanel open **Websites → Dashboard → Files → FTP Accounts**.
2. Copy the FTP IP (hostname), username, and port **21**. The password is the one for that FTP account. The upload folder for the main domain is `public_html`.
3. On GitHub open this repository → **Settings → Secrets and variables → Actions → New repository secret** and add:
   - `FTP_SERVER` — the FTP IP or hostname
   - `FTP_USERNAME` — the FTP username
   - `FTP_PASSWORD` — the FTP password
4. Merge to `main`, or run **Deploy to Hostinger** from the Actions tab.

The FTP login opens above the website folder. The workflow looks two directories down for `public_html` (for example `domains/your-domain/public_html/`) and uploads there. If more than one site is on the account, set `FTP_SERVER_DIR` to the exact folder, including the trailing slash.

The workflow uploads only the website files. It does not wipe the rest of the hosting account. Until the three secrets exist, a push to `main` skips the upload and says so in the Actions log.

The contact form opens the visitor’s email app. It does not need PHP or MySQL.
