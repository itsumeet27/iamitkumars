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

## Hostinger Git deploy

Hostinger’s Git connection publishes this repository. In hPanel the repository is `itsumeet27/iamitkumars`, the branch is `main`, and the deploy directory is the website `public_html` (the one two folders below the FTP login). There is no build command. The homepage is `index.html` at the repository root.

After the first deploy, every push to `main` updates the live site. Hostinger pulls the files itself.

The contact form opens the visitor’s email app. It does not need PHP or MySQL.

## FTP upload

`.github/workflows/deploy-hostinger.yml` is a spare upload over FTP. It does nothing until `FTP_SERVER`, `FTP_USERNAME`, and `FTP_PASSWORD` are saved under Settings → Secrets and variables → Actions. With the Git connection in place, that workflow can stay unused.
