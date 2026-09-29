# devsathya.com

Personal site for Dev Sathya. One static page, no framework, no build step.

Version 5 (2 Sep 2026): "One architect who also ships." Dark navy ground with electric blue bokeh
orbs and glass panels. Sora for headlines, DM Sans for text, JetBrains Mono for labels. A live
"handoffs versus one architect" animation in the hero, a click-through of the six request
governance layers, a ten day sprint scrubber, and a three signal fit test that writes the email for
the visitor. Public copy follows the public signal rail: no venture names, no product list, day job
described generically, and no city named (India only).

## Files

- `index.html` - the whole site, styles and scripts included. Edit this.
- `favicon.svg` - the blue glow dot mark.
- `CNAME` - tells GitHub Pages to serve the site at www.devsathya.com. Do not remove.

## Preview locally

```bash
python -m http.server 8765 --directory .
```

Then open http://localhost:8765.

## Deploy (GitHub Pages)

The site is served by GitHub Pages from the `main` branch of `devaprakash-s/devsathya-site`.
Commit and push, and the live site updates within a minute or two:

```bash
git add index.html favicon.svg
git commit -m "Describe the change"
git push
```

DNS is at Namecheap: `www` is a CNAME to `devaprakash-s.github.io`, and the bare domain has
GitHub Pages' four A records, so devsathya.com redirects to https://www.devsathya.com.

## Contact and mail

The contact address on the site is hello@devsathya.com, an alias of the dev@devsathya.com mailbox
(Zoho Mail). The mail records (MX, SPF, DKIM, DMARC) sit at Namecheap next to the site records;
leave them alone when changing the site.
