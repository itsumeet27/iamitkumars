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

## Hostinger shared hosting

The site is plain files at the repository root. In hPanel:

1. Open the website → **Advanced → Git**.
2. Connect this GitHub repository.
3. Set the branch to `main` and the deploy directory to `public_html`.
4. Deploy once. Later pushes to `main` are pulled automatically. There is no build command.

The contact form opens the visitor’s email app. It does not need PHP or MySQL.
