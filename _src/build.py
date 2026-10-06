"""Build devsathya.com from the page fragments in _src/pages.

Run from anywhere:  python _src/build.py
Writes index.html, advisory/, acquirers/, platforms/, about/, disclosures/, 404.html,
sitemap.xml and robots.txt at the site root. rescue/ and mail-mcp/ are separate and untouched.
"""
import html
import json
import pathlib
from urllib.parse import quote

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
SITE = "https://www.devsathya.com"
MAIL = "dev@devsathya.com"


def mailto(subject, body=""):
    q = "subject=" + quote(subject)
    if body:
        q += "&body=" + quote(body)
    return html.escape(f"mailto:{MAIL}?{q}", quote=True)


MAIL_OWNER = mailto("A private read", "A few lines about the firm (what it does, where, roughly how many people) are enough to start.\n\n")
MAIL_BUYER = mailto("Acquisition criteria",
                    "The firms we buy (platform, service line or software category):\n\n"
                    "Geography and size (regions, headcount or revenue range):\n\n"
                    "Structure (full or majority, earn-out, rollover):\n\n"
                    "Who decides, and the best address for a confidential profile:\n\n")
MAIL_PLATFORM = mailto("A platform problem")

PAGES = [
    # out path, fragment, nav key, title, description
    ("index.html", "home", "", "Dev Sathya | Sell-side M&A advisory for enterprise technology firms",
     "Independent sell-side M&A adviser to owners of Microsoft Dynamics, Sage, NetSuite and Salesforce partners, managed IT service providers and vertical software firms in the UK and the US. Success fee only."),
    ("advisory/index.html", "advisory", "advisory", "Sell-side M&A advisory | Dev Sathya",
     "How the sale of an enterprise technology firm is run: valuation and positioning, sale readiness, buyer universe, a competitive process, negotiation and completion. Owner-side only, success fee only."),
    ("acquirers/index.html", "acquirers", "acquirers", "For acquirers | Dev Sathya",
     "Owner-led ERP and CRM partners, managed service providers and vertical software firms in the UK and the US, brought to market in a defined process. Share your acquisition criteria."),
    ("platforms/index.html", "platforms", "platforms", "Enterprise platforms | Dev Sathya",
     "Architecture, strategy and delivery of enterprise platforms and governed AI systems by one architect who owns the thesis, the design, the build and the operations."),
    ("about/index.html", "about", "about", "About | Dev Sathya",
     "Dev Sathya, independent M&A adviser to owners of enterprise technology firms and architect of enterprise platforms, in enterprise technology since 1998."),
    ("disclosures/index.html", "disclosures", "", "Disclosures and privacy | Dev Sathya",
     "Regulatory status, the limits of the advice given, how market information is sourced, and the privacy notice for devsathya.com."),
    ("404.html", "404", "", "Page not found | Dev Sathya", "This page does not exist."),
]

NAV = [("advisory", "/advisory/", "Advisory"), ("acquirers", "/acquirers/", "Acquirers"),
       ("platforms", "/platforms/", "Platforms"), ("about", "/about/", "About")]

SECTORS = [
    ("ERP and finance platform partners", "Resellers and implementers of mid-market ERP, with support and subscription revenue.",
     "Sage &middot; Dynamics 365 Business Central &middot; NetSuite &middot; Acumatica &middot; SAP Business One"),
    ("CRM and workflow partners", "Consultancies built on one ecosystem, valued for certified people and repeat clients.",
     "Salesforce &middot; Dynamics 365 CE &middot; ServiceNow &middot; Workday"),
    ("Managed IT services", "MSPs and IT support firms with contracted monthly recurring revenue.",
     "Managed services &middot; Microsoft 365 and cloud &middot; Security &middot; Connectivity"),
    ("Vertical and niche software", "Founder-owned software vendors with a loyal installed base in one industry.",
     "Public sector &middot; Housing &middot; Professional services &middot; Manufacturing"),
    ("Technology-enabled B2B services", "Service firms whose margins depend on their own systems and data.",
     "Outsourced finance &middot; Document processing &middot; Data services"),
]

PRINCIPLES = [
    ("Owner-side only", "I act for the seller on every mandate and take no fee from acquirers, so advice on price and terms is not conflicted."),
    ("Paid on completion", "A success fee agreed in writing before any buyer is approached, paid from the proceeds at completion. No retainer."),
    ("Confidential by design", "Your firm's name reaches an acquirer only after a signed non-disclosure agreement. Staff, clients and vendors hear when you decide."),
    ("Evidence before narrative", "Every figure in a buyer document traces to a record a buyer can check. Acquirers pay for what diligence confirms."),
]

PHASES = [
    ("Engagement and preparation", "Weeks 1 to 4",
     "We agree the objectives, the fee and the scope in an engagement letter. I take in the records and build the financial picture a buyer will test.",
     ["Engagement letter and data request", "Normalised earnings and add-back schedule", "Valuation range and value ladder", "Diligence issues list"],
     "Your floor price, agreed in writing and supported by the evidence."),
    ("Materials and buyer universe", "Weeks 3 to 6",
     "The firm is presented in the terms acquirers use to price it, and the buyer list is built on dated evidence.",
     ["Anonymous teaser and NDA", "Confidential information memorandum", "Buyer universe, with a reason for each", "Data room index"],
     "The materials and the buyer list."),
    ("Marketing", "Weeks 6 to 12",
     "Every approved acquirer is approached at once, so no buyer gets a head start.",
     ["Single-wave outreach", "NDAs signed before the name is shared", "CIM released", "Written management Q&amp;A"],
     "Which buyers go forward."),
    ("Offers and selection", "Weeks 10 to 16",
     "Indications of interest narrow the field. Management meetings and letters of intent decide it.",
     ["IOIs compared on price and structure", "Management meetings", "LOIs pressed on cash at completion, escrow, earn-out and conditions"],
     "A signed letter of intent with one buyer."),
    ("Exclusivity and confirmatory diligence", "Weeks 16 to 24",
     "One buyer confirms what the CIM said. A complete data room and a prepared seller keep the price where the LOI set it.",
     ["A complete data room", "Diligence questions managed to the timetable", "Re-trade defence from the evidence", "Disclosure schedules with your counsel"],
     "Final terms."),
    ("Signing and completion", "At the close",
     "Your counsel drafts and negotiates the purchase agreement. I hold the terms to what was agreed and the timetable to its dates.",
     ["Share or asset purchase agreement", "Customer, landlord and partner programme consents", "Funds flow and completion statement", "Handover and transition plan"],
     "Signed agreements and funds received."),
]

SHORT_PROCESS = [
    ("Preparation", "Weeks 1 to 4", "Normalised earnings, a valuation range, and the issues diligence would find."),
    ("Positioning", "Weeks 3 to 6", "Anonymous teaser, confidential information memorandum and a defined buyer universe."),
    ("Marketing", "Weeks 6 to 12", "One wave of approaches, NDAs, the CIM released and written management Q&amp;A."),
    ("Offers", "Weeks 10 to 16", "Indications of interest, management meetings, then letters of intent compared and improved."),
    ("Diligence", "Weeks 16 to 24", "Exclusivity with one buyer, a complete data room and confirmatory diligence."),
    ("Completion", "At the close", "Purchase agreement by your counsel, consents, funds flow and an orderly handover."),
]


def cta(title, lede, href, label, image, alt, line):
    return f"""<section class="cta" aria-label="Contact">
  <div class="cta-media"><img src="/assets/img/{image}" alt="{alt}" loading="lazy" decoding="async"></div>
  <div class="wrap reveal">
    <p class="eyebrow">Next step</p>
    <h2>{title}</h2>
    <p class="lede">{lede}</p>
    <a class="btn btn-primary" href="{href}">{label} <span class="arr" aria-hidden="true">&rarr;</span></a>
    <p class="mail-line"><a href="mailto:{MAIL}">{MAIL}</a> &middot; {line}</p>
  </div>
</section>"""


CTAS = {
    "{{CTA_OWNER}}": cta("Considering a sale, now or in a few years?",
                         "Begin with a private read: five questions by email, then a written view of what the firm could be worth, to whom, and what would raise the figure. No charge and no obligation.",
                         MAIL_OWNER, "Write in confidence", "offices.jpg", "A modern office building at dusk, every floor lit",
                         "every reply in writing, in confidence"),
    "{{CTA_BUYER}}": cta("Tell me what you would buy next.",
                         "Two lines by email are enough to start. Anonymous profiles follow when a firm fits, and the name only after a signed NDA.",
                         MAIL_BUYER, "Send your criteria", "hero-city.jpg", "A dense city skyline at night",
                         "no fee from acquirers"),
    "{{CTA_PLATFORM}}": cta("Bring me a problem.",
                            "A short description by email is enough. You get a written answer on whether it can be solved, how, and how quickly. If it is not a fit, I will say who is.",
                            MAIL_PLATFORM, "Write to me", "corridor.jpg", "A long corridor of glass and steel",
                            "fixed price, agreed before we start"),
}


def market_rows(rows, with_source):
    out = []
    for r in rows:
        cells = [f"<td>{html.escape(r['date'])}</td>", f"<td><strong>{html.escape(r['acquirer'])}</strong></td>",
                 f"<td>{html.escape(r['target'])}</td>", f"<td>{html.escape(r['segment'])}</td>", f"<td>{html.escape(r['market'])}</td>"]
        if with_source:
            cells.append(f'<td><a href="{html.escape(r["url"], quote=True)}" rel="noopener" target="_blank">Announcement</a></td>')
        out.append("          <tr>" + "".join(cells) + "</tr>")
    return "\n".join(out)


def blocks():
    market = json.loads((SRC / "market.json").read_text(encoding="utf-8"))
    order = {"Oct": 10, "Sep": 9, "Aug": 8, "Jul": 7, "Jun": 6, "May": 5, "Apr": 4, "Mar": 3, "Feb": 2, "Jan": 1, "Nov": 11, "Dec": 12}

    def key(r):
        p = r["date"].split()
        day = int(p[0]) if len(p) == 3 else 15
        return (int(p[-1]), order[p[-2][:3]], day)
    market.sort(key=key, reverse=True)
    b = {
        "{{MARKET_TOP}}": market_rows(market[:5], False),
        "{{MARKET_ALL}}": market_rows(market, True),
        "{{SECTORS}}": "\n".join(f'      <div class="sector"><h3>{t}</h3><p>{d}</p><p class="plats">{p}</p></div>' for t, d, p in SECTORS),
        "{{PRINCIPLES}}": "\n".join(f'      <div class="principle"><h3>{t}</h3><p>{d}</p></div>' for t, d in PRINCIPLES),
        "{{PROCESS_SHORT}}": "\n".join(f'      <li><span class="when">{w}</span><h3>{t}</h3><p>{d}</p></li>' for t, w, d in SHORT_PROCESS),
        "{{PHASES}}": "\n".join(
            f'      <div class="phase reveal"><div class="ph-n">{i:02d}</div><div><h3>{t}</h3><span class="when">{w}</span></div>'
            f'<div><p>{d}</p><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul><p class="gate"><span>Gate</span>{g}</p></div></div>'
            for i, (t, w, d, items, g) in enumerate(PHASES, 1)),
        "{{MAIL_OWNER}}": MAIL_OWNER, "{{MAIL_BUYER}}": MAIL_BUYER, "{{MAIL_PLATFORM}}": MAIL_PLATFORM,
    }
    b.update(CTAS)
    return b


def header(nav_key):
    cur = ' aria-current="page"'
    links = "\n".join(
        f'      <a href="{href}"{cur if key == nav_key else ""}>{label}</a>' for key, href, label in NAV)
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Dev Sathya, home"><span class="brand-name">Dev Sathya</span><span class="brand-sub">M&amp;A advisory &middot; Enterprise platforms</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
{links}
      <a class="btn btn-primary" href="{MAIL_OWNER}">Write in confidence</a>
    </nav>
  </div>
</header>"""


FOOTER = f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="/"><span class="brand-name">Dev Sathya</span><span class="brand-sub">M&amp;A advisory &middot; Enterprise platforms</span></a>
        <p class="foot-about">Independent sell-side M&amp;A adviser to owners of enterprise technology firms in the United Kingdom and the United States, and an architect of enterprise platforms.</p>
      </div>
      <div><h4>Advisory</h4><ul><li><a href="/advisory/">Sell-side advisory</a></li><li><a href="/advisory/#process">The process</a></li><li><a href="/advisory/#readiness">Sale readiness</a></li><li><a href="/advisory/#activity">Market activity</a></li></ul></div>
      <div><h4>Acquirers</h4><ul><li><a href="/acquirers/">For acquirers</a></li><li><a href="/acquirers/#criteria">Share your criteria</a></li><li><a href="/platforms/">Enterprise platforms</a></li></ul></div>
      <div><h4>Contact</h4><ul><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="/about/">About</a></li><li><a href="https://www.linkedin.com/in/devaprakash/" rel="me noopener" target="_blank">LinkedIn</a></li><li><a href="/disclosures/">Disclosures and privacy</a></li></ul></div>
    </div>
    <div class="foot-legal">
      <p>&copy; <span id="year">2026</span> Dev Sathya, the trading name of Devaprakash Sathyanarayanan. Independent M&amp;A adviser: not a registered broker-dealer and not authorised by the Financial Conduct Authority. Nothing on this site is an offer of securities or investment advice. <a class="link" href="/disclosures/">Disclosures</a>.</p>
    </div>
  </div>
</footer>"""


def page(out, frag, nav_key, title, desc, b):
    body = (SRC / "pages" / f"{frag}.html").read_text(encoding="utf-8")
    for k, v in b.items():
        body = body.replace(k, v)
    assert "{{" not in body, f"unfilled block in {frag}"
    path = "" if out == "index.html" else out.replace("index.html", "")
    canonical = f"{SITE}/{path}"
    ld = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Dev Sathya",
          "description": PAGES[0][4], "url": SITE + "/", "email": MAIL, "areaServed": ["GB", "US"],
          "founder": {"@type": "Person", "name": "Dev Sathya", "jobTitle": "Independent M&A adviser",
                      "sameAs": ["https://www.linkedin.com/in/devaprakash/"]}}
    robots = '\n<meta name="robots" content="noindex">' if frag == "404" else ""
    doc = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{canonical}">{robots}
<meta name="theme-color" content="#01040d">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Dev Sathya">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@200;300;400;600&family=DM+Sans:ital,opsz,wght@0,9..40,300..700;1,9..40,300..700&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{json.dumps(ld)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header(nav_key)}
<main id="main">
{body}
</main>
{FOOTER}
<script src="/assets/site.js" defer></script>
</body>
</html>
"""
    dest = ROOT / out
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(doc, encoding="utf-8", newline="\n")
    return canonical


def main():
    b = blocks()
    urls = [page(*p, b) for p in PAGES]
    urls = [u for u, p in zip(urls, PAGES) if p[1] != "404"]
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc><lastmod>2026-10-06</lastmod></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /_src/\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print("built", len(PAGES), "pages")


if __name__ == "__main__":
    main()
