from html import escape
from pathlib import Path
import json

from portfolio_content import ARCHIVE, GITHUB, DESIGN, DESIGN_DETAILS, PROJECTS
from evidence import CASES, COMPONENTS, FIGMA_PROJECTS, ROLES, TILES
from work_samples import DOCS, case_extras, section, table

DIST = Path(__file__).parent / "dist"
BASE = "https://jillnguyen2311.github.io/portfolio"
NEW_TAB = ' target="_blank" rel="noopener noreferrer"'
ORIGINAL_SITE = "https://jill-nguyen-portfolio.finiteseahorse1.chatgpt.site"


def shell(title, description, content, *, case=None):
    root = "../" if case else ""
    home = root if case else "./"
    canonical = BASE + ("/projects/" + case + ".html" if case else "/")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="theme-color" content="#fdfbff">
  <title>{escape(title)}</title>
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/png" href="{root}assets/jill-mark.png">
  <link rel="stylesheet" href="{root}style.css">
  <script src="{root}site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="header">
  <div class="wrap header-inner">
    <a class="brand" href="{home}"><img class="brand-mark" src="{root}assets/jill-mark.png" alt="" width="34" height="34"><span>Jill Nguyen</span></a>
    <nav class="nav" aria-label="Main navigation">
      <a href="{home}#work">Projects</a><a href="{home}#about">About</a><a href="{home}#contact">Contact</a>
    </nav>
    <a class="button button-outline" href="{root}assets/Jill_Nguyen_Resume.pdf"{NEW_TAB}>Resume <span class="arrow out-arrow" aria-hidden="true">↑</span></a>
  </div>
</header>
{content}
<footer class="site-footer"><div class="wrap footer-inner"><strong>Jill Nguyen</strong><span>Business Analysis Portfolio · Vancouver, BC</span></div></footer>
</body>
</html>
"""


def link(label, url):
    target = NEW_TAB if url.startswith(("https://", "http://", "//")) else ""
    return f'<a class="text-link" href="{escape(url, quote=True)}"{target}>{escape(label)} <span class="out-arrow" aria-hidden="true">↑</span></a>'


def cover(project):
    item = TILES.get(project["id"])
    if not item and project.get("image"):
        item = (project["image"] + ".webp", project["image_caption"])
    if not item:
        return ""
    filename, alt = item
    return f'<div class="cover cover-{project["id"]}"><img class="art-image" src="assets/{filename}" alt="{escape(alt, quote=True)}" loading="lazy"></div>'


def card(project, *, catalog=False):
    category = f' data-category="{project["category"]}"' if catalog else ""
    tags = "".join(f"<li>{escape(t)}</li>" for t in project["tags"])
    direct = project.get("direct")
    url = escape(direct, quote=True) if direct else f'projects/{project["id"]}.html'
    cta = "Visit website" if direct else "Read case study"
    target = NEW_TAB if direct else ""
    title = escape(project["name"])
    title_link = title if direct else f'<a href="{url}">{title}</a>'
    tag_list = f'<ul class="tags" aria-label="Skills demonstrated">{tags}</ul>' if tags else ""
    return f"""
<article class="project-card"{category}>
  {cover(project)}
  <div class="card-body">
    <p class="card-kicker">{escape(project["type"])}</p>
    <h3>{title_link}</h3>
    <p>{escape(project["summary"])}</p>
    {tag_list}
    <div class="card-end"><a class="text-link" href="{url}"{target} aria-label="{cta} · {escape(project["name"], quote=True)}">{cta} <span aria-hidden="true">→</span></a></div>
  </div>
</article>"""


def archive_entries():
    return "".join(
        f'<li><a href="{GITHUB}{escape(repo, quote=True)}"{NEW_TAB} aria-label="{escape(name, quote=True)} source repository">'
        f'{escape(name)} <span class="out-arrow" aria-hidden="true">↑</span></a><span>{escape(description)}</span></li>'
        for name, description, repo in ARCHIVE
    )


def design_entries():
    return "".join(f"""<article class="design-card"><img src="assets/{image}.webp" alt="" loading="lazy"><div><h4><a href="projects/{image}.html">{escape(name)} <span class="out-arrow" aria-hidden="true">↑</span></a></h4><p>{escape(description)}</p></div></article>"""
                   for name, description, image in DESIGN)


def home_page():
    feature_cards = "".join(card(p) for p in PROJECTS[:2])
    suite_cards = "".join(card(p) for p in PROJECTS if p["id"] in ("lms360", "elib360", "test360"))
    catalog_cards = "".join(card(p, catalog=True) for p in PROJECTS[2:] if p["id"] not in ("lms360", "elib360", "test360"))
    return f"""
<main id="main">
  <section class="hero" aria-labelledby="hero-title">
    <div class="wrap hero-inner">
      <div>
        <p class="eyebrow"><span class="dot" aria-hidden="true"></span> Jill Nguyen · Business Analyst</p>
        <h1 id="hero-title">From requirements<br>to <em>deliverables</em></h1>
        <p class="intro">I turn stakeholder needs into business rules, Figma prototypes, data models and API specifications that delivery teams can build and test.</p>
        <div class="hero-actions">
          <a class="button button-main" href="#work">Explore Projects <span class="arrow" aria-hidden="true">↓</span></a>
        </div>
        <p class="hero-meta"><span>Vancouver, BC</span><span>ECBA, IIBA</span><span>BBA candidate, BCIT</span></p>
      </div>
      <figure class="hero-art" aria-label="A business rule traced through design and testing">
        <div class="diagram-window">
          <div class="window-top">
            <span class="window-dots" aria-hidden="true"><i></i><i></i><i></i></span>
            <span>Requirements to validation</span>
          </div>
          <div class="diagram-body">
            <p class="eyebrow">Business rule</p>
            <p class="diagram-title">Review incomplete requests</p>
            <dl class="diagram-trace">
              <div class="rule-row"><dt>Rule</dt><dd>Required fields missing</dd></div>
              <div class="rule-row"><dt>Prototype</dt><dd>Highlight fields to fix</dd></div>
              <div class="rule-row"><dt>Test</dt><dd>Preserve entered details</dd></div>
            </dl>
          </div>
        </div>
        <img class="art-sticker" src="assets/jill-mark.png" alt="" width="76" height="76">
        <figcaption class="art-caption">Example · Requirements traceability</figcaption>
      </figure>
    </div>
  </section>
  <section class="section wrap" id="work" aria-labelledby="featured-title">
    <div class="section-top">
      <div><p class="eyebrow">BachKhoaTech product suite</p><h2 id="featured-title">Education systems</h2></div>
      <p>School administration, university operations, online learning, digital libraries and assessment.</p>
    </div>
    <div class="featured-grid">{feature_cards}</div>
    <div class="suite-grid">{suite_cards}</div>
    <div class="work-sample-home" id="ba-artifacts">
      <div><p class="eyebrow">Business analysis work samples</p><h2>Requirements, models and tests</h2><p>Open the artifacts that connect a business rule to a screen, contract or testable outcome.</p></div>
      <div class="home-artifact-links">
        <a href="projects/sms360-srs.html">Screen-level SRS →</a>
        <a href="projects/sms360-data-model.html">Database specification and ERD →</a>
        <a href="projects/sms360-api.html">REST API specification →</a>
        <a href="projects/sms360-db-api.html">SMS360 DB &amp; API workbook →</a>
        <a href="projects/sms360.html#uml-sequence">UML sequence diagram →</a>
        <a href="projects/uni360.html#registration-bpmn">BPMN registration flow →</a>
        <a href="projects/sms360.html#traceability">Requirements-to-UAT matrix →</a>
      </div>
    </div>
  </section>
  <section class="section catalog" id="projects" aria-labelledby="catalog-title">
    <div class="wrap">
      <div class="section-top">
        <div><p class="eyebrow">Project portfolio</p><h2 id="catalog-title">Project directory</h2></div>
        <p>Client projects, product prototypes and technical work.</p>
      </div>
      <div class="filter-bar" role="group" aria-label="Filter projects">
        <button type="button" data-filter="all" aria-pressed="true">All</button>
        <button type="button" data-filter="systems" aria-pressed="false">Systems &amp; strategy</button>
        <button type="button" data-filter="client" aria-pressed="false">Client work</button>
        <button type="button" data-filter="product" aria-pressed="false">Product prototypes</button>
        <button type="button" data-filter="engineering" aria-pressed="false">Engineering</button>
      </div>
      <p class="sr-only" id="project-count" aria-live="polite"></p>
      <div class="catalog-grid">{catalog_cards}</div>
      <details class="archive">
        <summary>More development projects <span>View archive</span></summary>
        <ul class="archive-list">{archive_entries()}</ul>
      </details>
      <details class="archive">
        <summary>Visual design and illustration <span>View archive</span></summary>
        <div class="design-grid">{design_entries()}</div>
      </details>
    </div>
  </section>
  <section class="section wrap about-section" id="about" aria-labelledby="about-title">
    <div>
      <p class="eyebrow">About me</p><h2 id="about-title">Jill Nguyen</h2>
      <p class="about-copy">I worked as a business analyst on BachKhoaTech’s school-management products and now support web and communications work at the Vancouver Local Immigration Partnership. I hold the IIBA Entry Certificate in Business Analysis and a BCIT Digital Design and Development diploma. I’m completing my BBA at BCIT with an expected graduation date of September 2027.</p>
    </div>
    <dl class="skills" aria-label="Business analysis skills">
      <div class="skill"><dt>Discovery and delivery</dt><dd>Stakeholder interviews, requirements elicitation, backlog prioritization, Jira and Confluence</dd></div>
      <div class="skill"><dt>Process and systems design</dt><dd>SRS, business rules, BPMN, UML, ERDs, REST API specifications and SQL validation</dd></div>
      <div class="skill"><dt>Figma and design handoff</dt><dd>Role-based navigation, component libraries, wireframes, high-fidelity prototypes and annotated screen specifications</dd></div>
      <div class="skill"><dt>Validation</dt><dd>Acceptance criteria, requirements traceability and UAT planning</dd></div>
    </dl>
  </section>
  <section class="contact-section" id="contact" aria-labelledby="contact-title">
    <div class="wrap contact-inner">
      <div><p class="eyebrow">Contact</p><h2 id="contact-title">Let’s connect.</h2><p>For business analysis opportunities or questions about a case study, send me an email.</p></div>
      <div class="contact-address"><a class="button button-outline" href="{ORIGINAL_SITE}/#contact"{NEW_TAB}>Contact Jill <span aria-hidden="true">↑</span></a></div>
    </div>
  </section>
</main>
"""


def presentation(project, following):
    project_id = project["id"]
    title = escape(project["name"])
    jumps = {
        "sms360": [("Design evidence", "design-evidence"), ("SRS, database and API", "work-samples"), ("Business rules", "business-rules"), ("UAT", "traceability"), ("Homeroom BPMN", "homeroom-flow"), ("UML", "uml-sequence"), ("ERD", "notebook-erd")],
        "uni360": [("BPMN", "registration-bpmn"), ("ERD", "enrollment-erd"), ("UAT", "uat")],
        "elib360": [("Search and access flow", "catalog-flow")],
        "lms360": [("Speaking-practice flow", "speaking-flow")],
        "test360": [("Score sync flow", "score-flow")],
        "whitestone": [("Mockups and prototype", "design-evidence")],
        "heathelp": [("Mockups and prototype", "design-evidence")],
    }.get(project_id, [])
    if project_id in ROLES:
        jumps = [("Users and roles", "project-roles")] + jumps
    if project_id in COMPONENTS and not any(target == "design-evidence" for _, target in jumps):
        jumps += [("Figma and design handoff", "design-evidence")]
    items = "".join(f'<a href="#{target}">{label}</a>' for label, target in jumps)
    jump_nav = f'<nav class="case-jumps" aria-label="On this page">{items}</nav>' if items else ""
    sections = []
    for heading, value in CASES.get(project_id, project["sections"]):
        if isinstance(value, list):
            body = "<ul>" + "".join(f"<li>{escape(item)}</li>" for item in value) + "</ul>"
        else:
            body = f"<p>{escape(value)}</p>"
        sections.append(f'<section class="case-section"><h2>{escape(heading)}</h2>{body}</section>')
    role_section = ""
    if project_id in ROLES:
        intro, rows = ROLES[project_id]
        role_section = section("project-roles", "Who uses this product", f"<p>{escape(intro)}</p>" +
                               table(("Role", "What they do", "What the interface must support"), rows))
    figma_sources = ""
    if project_id in FIGMA_PROJECTS:
        original_case = f"{ORIGINAL_SITE}/projects/{project_id}.html#design-evidence"
        reference = link("Figma references on the original portfolio", original_case)
        figma_sources = f'<div class="figma-links">{reference}</div>'
    sample = ""
    if project.get("sample"):
        heading, description, rows = project["sample"]
        table_rows = "".join(f"<tr><td>{escape(c)}</td><td>{escape(v)}</td></tr>" for c, v in rows)
        sample = f"""
<section class="case-sample">
  <h2>{escape(heading)}</h2><p>{escape(description)}</p>
  <table><thead><tr><th scope="col">Scenario</th><th scope="col">Expected behaviour</th></tr></thead><tbody>{table_rows}</tbody></table>
</section>"""
    evidence = ""
    if project.get("links"):
        sources = "".join(link(label, url) for label, url in project["links"] if "github.com/jillnguyen2311" not in url)
        if sources:
            evidence = f'<section class="evidence"><h2>Project evidence</h2><div class="evidence-links">{sources}</div></section>'
    live = project.get("live")
    live_cta = ""
    if live:
        live_cta = (f'<a class="button button-main case-live" href="{escape(live, quote=True)}"{NEW_TAB}>'
                    f'Open live {title} app <span class="out-arrow" aria-hidden="true">↑</span></a>')
    archive_preview = ""
    if project_id == "westernstains":
        archive_preview = ('<figure class="case-art case-archive-preview"><img src="../assets/westernstains-home.webp" '
                           'alt="Archived WesternStains homepage with wood stain guidance and shopping navigation"></figure>')
    next_link = ""
    if following:
        next_url = following.get("direct") or f'{following["id"]}.html'
        target = NEW_TAB if following.get("direct") else ""
        next_link = (f'<a class="text-link" href="{escape(next_url, quote=True)}"{target}>Next project · '
                     f'{escape(following["name"])} <span aria-hidden="true">→</span></a>')
    return f"""
<main id="main">
  <section class="case-hero" aria-labelledby="case-title">
    <div class="case-wrap">
      <a class="text-link" href="../#work">← Back to projects</a>
      <p class="eyebrow">{escape(project["type"])}</p>
      <h1 id="case-title">{title}</h1>
      <p class="intro">{escape(project["summary"])}</p>
      {live_cta}
    </div>
  </section>
  <article class="case-wrap case-body" aria-labelledby="case-title">
    <dl class="case-meta">
      <div><dt>My role</dt><dd>{escape(project["role"])}</dd></div>
      <div><dt>Period</dt><dd>{escape(project["when"])}</dd></div>
      <div><dt>Project stage</dt><dd>{escape(project["status"])}</dd></div>
    </dl>
    {jump_nav}
    {archive_preview}
    {role_section}
    {"".join(sections)}
    {case_extras(project_id, figma_sources)}
    {sample if project_id != "uni360" else ""}
    {evidence}
    <nav class="case-nav" aria-label="Case study navigation">
      <a class="text-link" href="../#work">← Back to projects</a>{next_link}
    </nav>
  </article>
</main>
"""


def sample_page(slug, title, overview, sections):
    return f"""
<main id="main">
  <section class="case-hero"><div class="case-wrap">
    <a class="text-link" href="sms360.html#work-samples">← Back to SMS360 work samples</a>
    <p class="eyebrow">SMS360 · Portfolio work sample</p>
    <h1>{escape(title)}</h1><p class="intro">{escape(overview)}</p>
  </div></section>
  <article class="case-wrap case-body sample-body">
    <p class="sample-note">Adapted from work on SMS360. Examples use fictional records and representative implementation names.</p>
    {sections}
    <a class="button button-outline print-sample" href="../assets/{slug}.pdf" download>Download PDF ↓</a>
  </article>
</main>"""


def spec_page():
    data = json.loads((DIST.parent / "sms360_public_spec.json").read_text())
    feature_ids = {detail["id"] for detail in data["details"]}
    groups = []
    for group in data["groups"]:
        items = []
        for ident, title in group["features"]:
            label = f"<code>{escape(ident)}</code> {escape(title)}"
            item = f'<a href="#{ident}">{label}</a>' if ident in feature_ids else label
            items.append(f"<li>{item}</li>")
        groups.append(f'<details class="spec-module"><summary>{escape(group["module"])} '
                      f'<span>{len(items)} features</span></summary><ul>{"".join(items)}</ul></details>')
    examples = []
    headings = ("Field", "Type", "Key", "Note")
    for detail in data["details"]:
        body = f'<p>{escape(detail["rule"])}</p>'
        for database in detail["database"]:
            body += f'<h3>Database · {escape(database["title"])}</h3>' + table(headings, database["fields"])
        for api in detail["api"]:
            label = f'{api["method"]} · {api["title"]} · HTTP {api["status"]}'
            body += f'<h3>Proposed API · {escape(label)}</h3>' + table(headings, api["fields"])
        examples.append(section(detail["id"], f'{detail["id"]} · {detail["title"]}', body))
    return f"""
<main id="main">
  <section class="case-hero"><div class="case-wrap">
    <a class="text-link" href="sms360.html#work-samples">← Back to SMS360 work samples</a>
    <p class="eyebrow">SMS360 · School Admin specification</p>
    <h1>Database &amp; API workbook</h1>
    <p class="intro">144 features across 15 School Admin modules, with six examples that connect business rules to database or API fields.</p>
    <a class="button button-main" href="../assets/SMS360_School_Admin_DB_API_Portfolio_Extract.xlsx" download>Download workbook (.xlsx) ↓</a>
  </div></section>
  <article class="case-wrap case-body sample-body">
    <p class="sample-note">Portfolio extract from the combined School Admin specification. Database examples cover notebook identity and reviewer assignment. API fields come from the proposed contracts.</p>
    {section("feature-index", "Feature index", "".join(groups))}
    {"".join(examples)}
  </article>
</main>"""


def design_page(name, description, slug):
    media = f'<figure class="case-art"><img src="../assets/{slug}.webp" alt="{escape(description, quote=True)}"></figure>'
    if slug == "bunny-video":
        media = """
    <figure class="case-art design-video">
      <video controls playsinline preload="none" width="1280" height="720" poster="../assets/bunny-rescue.webp" aria-label="Think Before Getting a Bunny animated short">
        <source src="../assets/think-before-getting-a-bunny.mp4" type="video/mp4">
        <a href="../assets/think-before-getting-a-bunny.mp4">Open the video (.mp4)</a>
      </video>
      <figcaption>Watch the original 1-minute animated short.</figcaption>
    </figure>
    <section class="case-section">
      <h2>Character and scene design</h2>
      <div class="gallery">
        <figure class="artifact-figure"><img src="../assets/bunny-character-study.webp" alt="Two original character poses for a white rabbit" loading="lazy">
          <figcaption><strong>Rabbit character study</strong><p>Two poses used to develop the character’s appearance.</p></figcaption>
        </figure>
        <figure class="artifact-figure"><img src="../assets/bunny-early-days.webp" alt="The child sits with the rabbit in an early scene" loading="lazy">
          <figcaption><strong>Early storyboard scene</strong><p>The owner and rabbit get to know each other.</p></figcaption>
        </figure>
      </div>
    </section>
"""
    return f"""
<main id="main">
  <section class="case-hero"><div class="case-wrap">
    <a class="text-link" href="../#projects">← Back to projects</a>
    <p class="eyebrow">Visual design</p>
    <h1>{escape(name)}</h1><p class="intro">{escape(description)}</p>
  </div></section>
  <article class="case-wrap case-body">
    <p>{escape(DESIGN_DETAILS[slug])}</p>
    {media}
  </article>
</main>"""


def external_project_page(title, url, slug):
    dest = escape(url, quote=True)
    content = f"""
<main id="main"><section class="case-hero"><div class="case-wrap">
  <a class="text-link" href="../#work">← Back to projects</a>
  <h1>{escape(title)}</h1>
  <a class="button button-main case-live" href="{dest}"{NEW_TAB}>Visit website <span class="out-arrow" aria-hidden="true">↑</span></a>
</div></section></main>"""
    return shell(f"{title} | Jill Nguyen", f"Visit the {title} website.", content, case=slug)


def main():
    cases = DIST / "projects"
    cases.mkdir(parents=True, exist_ok=True)
    description = "Jill Nguyen’s business analysis portfolio featuring school operations, system design, stakeholder discovery and product prototyping."
    (DIST / "index.html").write_text(shell("Jill Nguyen | Business Analyst Portfolio", description, home_page()))
    for index, project in enumerate(PROJECTS):
        following = PROJECTS[index + 1] if index + 1 < len(PROJECTS) else None
        slug = project["id"]
        if project.get("direct"):
            (cases / f"{slug}.html").write_text(external_project_page(project["name"], project["direct"], slug))
            continue
        title = f'{project["name"]} | Jill Nguyen'
        page = shell(title, project["summary"], presentation(project, following), case=project["id"])
        (cases / f'{project["id"]}.html').write_text(page)
    for slug, (title, overview, body) in DOCS.items():
        (cases / f"{slug}.html").write_text(
            shell(f"{title} | SMS360", overview, sample_page(slug, title, overview, body()), case=slug)
        )
    slug = "sms360-db-api"
    (cases / f"{slug}.html").write_text(shell(
        "Database & API workbook | SMS360", "Field-level School Admin requirements, data and API examples.",
        spec_page(), case=slug
    ))
    for name, description, slug in DESIGN:
        content = design_page(name, description, slug)
        (cases / f"{slug}.html").write_text(shell(f"{name} | Jill Nguyen", description, content, case=slug))

    for path in DIST.rglob("*.html"):
        html = path.read_text()
        path.write_text("\n".join(line.rstrip() for line in html.splitlines()) + "\n")


if __name__ == "__main__":
    main()
