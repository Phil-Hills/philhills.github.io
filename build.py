import json
import os

def generate_html(page_data, schema_person, schema_website, site_info):
    title = page_data.get("title", "")
    meta_title = page_data.get("seo", {}).get("metaTitle", "")
    meta_description = page_data.get("seo", {}).get("metaDescription", "")
    keywords = ", ".join(page_data.get("seo", {}).get("keywords", []))
    slug = page_data.get("slug", "")

    # Determine the correct canonical URL
    if slug == "/":
        canonical_url = site_info['primaryDomain']
    else:
        canonical_url = f"{site_info['primaryDomain']}{slug}.html"


    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="title" content="{meta_title}">
    <meta name="description" content="{meta_description}">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="canonical" href="{canonical_url}">
    <script type="application/ld+json">
        {json.dumps(schema_person, indent=4)}
    </script>
    <script type="application/ld+json">
        {json.dumps(schema_website, indent=4)}
    </script>
"""
    if page_data.get('type') in ['article', 'flagshipArticle']:
        article_schema = site_info['schema']['articleTemplate']
        article_schema['headline'] = title
        article_schema['mainEntityOfPage'] = f"{site_info['primaryDomain']}{page_data['slug']}"
        html += f"""    <script type="application/ld+json">
        {json.dumps(article_schema, indent=4)}
    </script>"""

    html += """
</head>
<body>
"""

    # Add header
    html += f"""    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about-phil-hills.html">About</a>
            <a href="/projects-phil-hills.html">Projects</a>
            <a href="/cube-protocol.html">Cube Protocol</a>
            <a href="/press.html">Press</a>
            <a href="/worklog.html">Worklog</a>
        </nav>
        <h1>{page_data.get('title', '')}</h1>
    </header>"""

    # Add main content
    html += """    <main>"""

    if "content" in page_data:
        content = page_data["content"]
        if "heroHeading" in content:
            html += f"""        <section class="hero">
            <h2>{content["heroHeading"]}</h2>
            {''.join([f'<p>{p}</p>' for p in content.get("heroBody", [])])}
        </section>"""

        if "summary" in content:
             html += f"""        <p><em>{content["summary"]}</em></p>"""

        if "body" in content:
            html += ''.join([f'<p>{p}</p>' for p in content["body"]])

        if "sections" in content:
            for section in content["sections"]:
                html += f"""        <section>
            <h2>{section["heading"]}</h2>
"""
                if "bullets" in section:
                    html += "            <ul>"
                    for bullet in section["bullets"]:
                        html += f"                <li>{bullet}</li>"
                    html += "            </ul>"
                if "body" in section:
                    html += ''.join([f'<p>{p}</p>' for p in section["body"]])
                if "ctaText" in section:
                    cta_href = section["ctaHref"]
                    if not cta_href.endswith(".html") and cta_href != "/":
                        cta_href = cta_href.strip("/") + ".html"
                    elif cta_href == "/":
                        cta_href = "index.html"

                    html += f"""            <a href="{cta_href}">{section["ctaText"]}</a>
"""
                html += "        </section>"
    html += """    </main>"""

    # Add footer
    html += """    <footer>
        <p>&copy; 2025 Phil Hills</p>
        <nav>
            <a href="/about-phil-hills.html">About Phil Hills</a>
            <a href="/about-bruce-phillip-hills.html">About Bruce Phillip Hills</a>
            <a href="/projects-phil-hills.html">Projects</a>
            <a href="/cube-protocol.html">Cube Protocol</a>
            <a href="/press.html">Press</a>
            <a href="/worklog.html">Worklog</a>
        </nav>
    </footer>
</body>
</html>"""
    return html


def main():
    with open("content.json", "r") as f:
        data = json.load(f)

    schema_person = data["schema"]["person"]
    schema_website = data["schema"]["website"]
    site_info = data["site"]
    site_info['schema'] = data['schema']


    for page_data in data["site"]["pages"]:
        slug = page_data["slug"]
        if slug == "/":
            filename = "index.html"
        else:
            filename = f"{slug.strip('/')}.html"

        html_content = generate_html(page_data, schema_person, schema_website, site_info)

        with open(filename, "w") as f:
            f.write(html_content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
