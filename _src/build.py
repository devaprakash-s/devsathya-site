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


MAIL_OWNER = mailto("Confidential M&A inquiry", "A few lines by email about the firm (approximate revenue and EBITDA, headcount, recurring revenue mix, and ecosystem) are enough to confirm fit.\n\n")
MAIL_BUYER = mailto("Acquisition criteria & buy-side mandate",
                    "The firms we acquire (MSP, ERP/CRM ecosystem, or vertical software category):\n\n"
                    "Geography and size floor (regions, minimum revenue and EBITDA):\n\n"
                    "Structure (full buyout, majority recap, permanent-hold vs sponsor cycle):\n\n"
                    "Decision-maker and conflict-check contact email:\n\n")
MAIL_PLATFORM = mailto("A platform problem")

PAGES = [
    # out path, fragment, nav key, title, description
    ("index.html", "home", "", "Dev Sathya | M&A advisory & origination for enterprise technology firms",
     "Independent M&A adviser to founders and institutional acquirers of Microsoft Dynamics, Sage, Acumatica, NetSuite and Salesforce partners, managed IT service providers and vertical software firms in the US and the UK. Success fee only."),
    ("advisory/index.html", "advisory", "advisory", "M&A advisory & fast-track introductions | Dev Sathya",
     "Two paths to an exit for enterprise technology founders: a zero-fee direct introduction to a contracted permanent-hold buyer, or a full competitive sell-side process. Written-first, success fee only."),
    ("acquirers/index.html", "acquirers", "acquirers", "For acquirers & PE platforms | Dev Sathya",
     "Proprietary, off-market MSP, ERP/CRM and vertical software acquisition opportunities across the US and the UK. Structured target clearance, dedicated first-look windows, and normalized financials."),
    ("platforms/index.html", "platforms", "platforms", "Enterprise platforms | Dev Sathya",
     "Architecture, strategy and delivery of enterprise platforms and governed AI systems by one architect who owns the thesis, the design, the build and the operations."),
    ("about/index.html", "about", "about", "About | Dev Sathya",
     "Dev Sathya, independent M&A adviser for enterprise technology firms in the US and the UK and architect of enterprise platforms, in enterprise technology since 1998."),
    ("disclosures/index.html", "disclosures", "", "Disclosures and privacy | Dev Sathya",
     "Regulatory status, the limits of the advice given, how market information is sourced, and the privacy notice for devsathya.com."),
    ("404.html", "404", "", "Page not found | Dev Sathya", "This page does not exist."),
]

NAV = [("advisory", "/advisory/", "For Owners"), ("acquirers", "/acquirers/", "For Acquirers"),
       ("platforms", "/platforms/", "Platforms"), ("about", "/about/", "About")]

SECTORS = [
    ("ERP and finance platform partners", "Resellers and implementers of mid-market ERP, with recurring support and subscription revenue.",
     "Sage &middot; Acumatica &middot; NetSuite &middot; Dynamics 365 Business Central &middot; Epicor &middot; SAP Business One"),
    ("CRM and cloud consultancies", "Consultancies built on enterprise cloud ecosystems, valued for certified bench depth and repeat clients.",
     "Salesforce &middot; Dynamics 365 CE &amp; F&amp;O &middot; ServiceNow &middot; Workday &middot; AWS"),
    ("Managed IT services (MSPs)", "Regional and national MSPs and cybersecurity firms with contracted monthly recurring revenue.",
     "Managed IT &middot; Microsoft 365 &amp; Azure &middot; Cybersecurity &middot; Compliance"),
    ("Vertical and niche B2B software", "Founder-owned software vendors with high gross retention and mission-critical domain workflows.",
     "Industry SaaS &middot; Supply chain &amp; CargoWise &middot; Legal &amp; accounting tech &middot; Manufacturing ERP"),
    ("Technology-enabled B2B services", "Specialized service firms whose margins and retention rest on proprietary workflows and recurring contracts.",
     "Document automation &middot; Compliance &amp; billing &middot; Data &amp; integration services"),
]

BUY_BOXES = [
    ("US-MSP-01", "ACTIVE &middot; CAPITAL ALLOCATED",
     "US Managed IT Services (MSPs)",
     "Permanent-hold US platform (PE-backed)",
     "$3.0M - $15.0M rev &middot; $500k+ EBITDA &middot; 12+ staff &middot; &gt;50% recurring",
     "United States (Midwest, Mid-Atlantic, South, Mountain West, Northeast)",
     "Acquirer-paid (0% seller fee)"),
    ("NA-ERP-02", "ACTIVE &middot; PERMANENT HOLD",
     "Enterprise ERP &amp; Accounting Partners",
     "Dedicated ERP holding company (Permanent-hold)",
     "$3.0M - $15.0M rev &middot; $500k+ EBITDA &middot; Sage, Acumatica, NetSuite, Epicor",
     "United States, Canada &amp; United Kingdom",
     "Acquirer-paid (0% seller fee)"),
    ("UK-DYN-03", "ACTIVE &middot; CONSOLIDATION",
     "Microsoft Dynamics 365 Consultancies",
     "PE-backed Microsoft cloud consolidators",
     "&pound;500k - &pound;5.0M (UK) / $2.0M - $12.0M (US) &middot; Business Central, F&amp;O, CE",
     "United Kingdom, Ireland &amp; United States",
     "Acquirer-paid or Sell-side"),
    ("GL-VMS-04", "ACTIVE &middot; PERMANENT HOLD",
     "Vertical Market B2B Software (SaaS)",
     "Permanent buy-and-hold software groups",
     "$1.5M - $8.0M ARR &middot; High gross retention &middot; Proprietary IP",
     "North America, United Kingdom &amp; Europe",
     "Acquirer-paid or Sell-side"),
    ("GL-LOG-05", "ACTIVE &middot; STRATEGIC",
     "Logistics &amp; Supply Chain Integration",
     "Strategic logistics &amp; enterprise IT acquirers",
     "$500k - $5.0M rev &middot; CargoWise partners, customs &amp; ERP integration",
     "United States &amp; Global delivery",
     "Active sell-side &amp; strategic"),
]

PRINCIPLES = [
    ("Single-side fee alignment", "The practice is compensated by one side only, never both. On a sell-side mandate the owner pays the success fee; on a buy-side origination mandate the acquiring platform pays the introduction fee at zero cost to the seller."),
    ("Paid on completion only", "There is no upfront retainer, no monthly maintenance fee, and no charge for an initial valuation or buy-box qualification. Compensation is earned exclusively when a transaction closes."),
    ("100% written-first &amp; confidential", "Every qualification step, conflict check, and NDA runs asynchronously in writing by email, without calendar friction or preliminary phone calls. No target identity is ever disclosed without prior written consent."),
    ("Evidence before narrative", "Every figure in a buyer summary or information memorandum traces to a primary financial or technical record that confirmatory diligence can verify."),
]

PHASES = [
    ("Written qualification and NDA", "Days 1 to 5",
     "Everything starts asynchronously in writing by email. Four headline metrics (revenue, adjusted EBITDA, recurring mix, and concentration) are confirmed under a one-page mutual NDA, with zero calendar friction.",
     ["1-page Mutual Confidentiality Agreement", "Four-point written qualification check", "Selection of path: zero-fee buyer fast-track or competitive sell-side process", "Normalized EBITDA and add-back review"],
     "Signed NDA and written confirmation of mandate path."),
    ("Materials and target clearance", "Weeks 1 to 3",
     "For a direct platform introduction, a 3-business-day blind conflict check runs with the acquirer before disclosing your company name. For a competitive sale, the anonymous teaser and normalized financial schedule are prepared.",
     ["Anonymous two-page investment teaser", "Normalized financial summary and recurring revenue schedule", "3-day buyer conflict-clearance protocol (on fast-track intros)", "Virtual data room index"],
     "Written owner approval of materials or target clearance confirmation."),
    ("Introductions and marketing", "Weeks 3 to 8",
     "On the fast-track path, a direct double opt-in written introduction is made with a dedicated first-look window. On a competitive mandate, approved acquirers are approached in a coordinated wave.",
     ["Double opt-in email introduction or coordinated outreach wave", "Mutual NDAs executed before identity disclosure", "Financial summary and memorandum released", "Asynchronous written management Q&amp;A"],
     "Qualified buyer engagement and Q&amp;A completion."),
    ("Indications of interest and LOI", "Weeks 6 to 12",
     "Buyers submit written indications of interest (IOIs) followed by focused leadership discussions and binding letters of intent (LOIs) detailing price, cash at close, working capital, and transition terms.",
     ["Written IOIs evaluated on headline price and net cash at close", "Focused executive alignment sessions", "LOIs negotiated on cash at completion, escrow, earn-out and rollover equity"],
     "Countersigned Letter of Intent with one buyer."),
    ("Exclusivity and confirmatory diligence", "Weeks 10 to 18",
     "The selected acquirer conducts financial, tax, legal, and technical diligence against a pre-organized virtual data room, keeping the price anchored to what the LOI set.",
     ["Structured Virtual Data Room (VDR) management", "Quality of earnings (QoE) and technical diligence coordination", "Re-trade defense grounded in pre-disclosed records", "Disclosure schedules prepared with your counsel"],
     "Confirmatory diligence sign-off and final purchase agreement."),
    ("Signing and completion", "At the close",
     "Legal counsel finalizes the definitive purchase agreement, third-party consents are completed, and closing funds are wired directly through escrow.",
     ["Definitive Share or Asset Purchase Agreement", "Partner programme and key contract consents", "Closing funds flow and escrow distribution", "Structured founder and team transition"],
     "Executed closing documents and wire settlement."),
]

SHORT_PROCESS = [
    ("Written Check", "Days 1 to 5", "Four headline numbers confirmed by email under a 1-page Mutual NDA. Zero call friction."),
    ("Clearance", "Weeks 1 to 3", "Normalized earnings schedule, blind profile, and 3-day buyer conflict clearance."),
    ("Introduction", "Weeks 3 to 8", "Direct double opt-in introduction (first-look) or coordinated multi-buyer wave."),
    ("Offers (IOI/LOI)", "Weeks 6 to 12", "Written valuation ranges compared and negotiated into a signed Letter of Intent."),
    ("Diligence", "Weeks 10 to 18", "Exclusivity with the winning buyer, VDR management, and confirmatory diligence."),
    ("Completion", "At the close", "Purchase agreement execution, funds wired at closing, and orderly handover."),
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
    "{{CTA_OWNER}}": cta("Considering a sale, or curious if your firm fits a live buyer mandate?",
                         "Everything is handled in writing by email, with zero obligation and no preliminary phone calls. Send four rough numbers by email to see whether your practice qualifies for a zero-fee institutional introduction or a competitive sale process.",
                         MAIL_OWNER, "Write in confidence", "offices.jpg", "A modern office building at dusk, every floor lit",
                         "100% written-first &middot; strict confidentiality under NDA"),
    "{{CTA_BUYER}}": cta("Register your acquisition criteria.",
                         "Two lines by email are enough to register your buy-box. The practice originates off-market MSP, ERP/CRM, and vertical software targets with normalized financials and a 3-day conflict-clearance protocol.",
                         MAIL_BUYER, "Send your criteria", "hero-city.jpg", "A dense city skyline at night",
                         "success fee at completion only &middot; 24-month introduction protection"),
    "{{CTA_PLATFORM}}": cta("Bring a platform problem.",
                            "A short description by email is enough. You get a written answer on whether it can be solved, how, and how quickly. If it is not a fit, I will say who is.",
                            MAIL_PLATFORM, "Write in confidence", "corridor.jpg", "A long corridor of glass and steel",
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


def buy_box_rows():
    out = []
    for code, status, sector, buyer, criteria, geo, fee in BUY_BOXES:
        fee_cls = "fee-badge fee-zero" if "0%" in fee else "fee-badge"
        cells = [
            f'<td><span class="mandate-code">{code}</span><span class="status-pill"><span class="dot" aria-hidden="true"></span>{status}</span></td>',
            f"<td><strong>{sector}</strong><span class=\"cell-sub\">{buyer}</span></td>",
            f"<td>{criteria}</td>",
            f"<td>{geo}</td>",
            f'<td><span class="{fee_cls}">{fee}</span></td>',
        ]
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
        "{{BUY_BOX_ROWS}}": buy_box_rows(),
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
    <a class="brand" href="/" aria-label="Dev Sathya, home"><span class="brand-name">Dev Sathya</span><span class="brand-sub">M&amp;A Advisory &amp; Origination &middot; New York &amp; London</span></a>
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
        <a class="brand" href="/"><span class="brand-name">Dev Sathya</span><span class="brand-sub">M&amp;A Advisory &amp; Origination &middot; New York &amp; London</span></a>
        <p class="foot-about">Independent M&amp;A advisory and buy-side origination practice for enterprise technology firms in the United States and the United Kingdom, and an architecture practice for enterprise platforms.<br><span style="display:inline-block;margin-top:8px;font-size:13.5px;color:var(--ink-2)">Commercial office: 1178 Broadway, 3rd Floor #3433, New York, NY 10001, USA</span></p>
      </div>
      <div><h4>For Owners</h4><ul><li><a href="/advisory/">Advisory &amp; Fast-Track</a></li><li><a href="/#mandates">Active buyer mandates</a></li><li><a href="/advisory/#process">The process</a></li><li><a href="/advisory/#readiness">Sale readiness</a></li></ul></div>
      <div><h4>For Acquirers</h4><ul><li><a href="/acquirers/">Buy-side origination</a></li><li><a href="/acquirers/#criteria">Share your criteria</a></li><li><a href="/advisory/#activity">Market activity</a></li><li><a href="/platforms/">Enterprise platforms</a></li></ul></div>
      <div><h4>Contact</h4><ul><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="/about/">About</a></li><li><a href="/disclosures/">Disclosures and privacy</a></li></ul></div>
    </div>
    <div class="foot-legal">
      <p>&copy; <span id="year">2026</span> Dev Sathya (1178 Broadway, 3rd Floor #3433, New York, NY 10001, USA). Independent M&amp;A adviser: not a registered broker-dealer and not authorised by the Financial Conduct Authority. Nothing on this site is an offer of securities or investment advice. <a class="link" href="/disclosures/">Disclosures</a>.</p>
    </div>
  </div>
</footer>"""


def page(out, frag, nav_key, title, desc, b):
    body = (SRC / "pages" / f"{frag}.html").read_text(encoding="utf-8")
    for k, v in b.items():
        body = body.replace(k, v)
    assert "{{" not in body, f"unfilled block in {frag}"
    path = "" if out == "index.html" else out.replace("index.html", "")
    rel_prefix = "../" if "/" in out else ""
    canonical = f"{SITE}/{path}"
    ld = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "Dev Sathya M&A Advisory",
        "description": PAGES[0][4],
        "url": SITE + "/",
        "email": MAIL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "1178 Broadway, 3rd Floor #3433",
            "addressLocality": "New York",
            "addressRegion": "NY",
            "postalCode": "10001",
            "addressCountry": "US"
        },
        "areaServed": ["US", "GB"],
        "founder": {"@type": "Person", "name": "Dev Sathya", "jobTitle": "Independent M&A Adviser"}
    }
    robots = '\n<meta name="robots" content="noindex">' if frag == "404" else ""
    body_rel = body.replace('"/assets/', f'"{rel_prefix}assets/')
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
<link rel="icon" href="{rel_prefix}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@200;300;400;600&family=DM+Sans:ital,opsz,wght@0,9..40,300..700;1,9..40,300..700&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{rel_prefix}assets/site.css">
<script type="application/ld+json">{json.dumps(ld)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header(nav_key)}
<main id="main">
{body_rel}
</main>
{FOOTER}
<script src="{rel_prefix}assets/site.js" defer></script>
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
        + "".join(f"  <url><loc>{u}</loc><lastmod>2026-10-15</lastmod></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /_src/\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print("built", len(PAGES), "pages")


if __name__ == "__main__":
    main()
