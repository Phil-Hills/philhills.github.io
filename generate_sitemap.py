import json
from datetime import datetime

def generate_sitemap(data):
    sitemap_template = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>"""
    url_template = """  <url>
    <loc>{loc}</loc>
    <lastmod>{lastmod}</lastmod>
  </url>"""

    urls = []
    current_date = datetime.now().strftime("%Y-%m-%d")
    primary_domain = data["site"]["primaryDomain"]

    for page in data["site"]["pages"]:
        slug = page["slug"]
        if slug == "/":
            loc = primary_domain
        else:
            loc = f"{primary_domain}/{slug.strip('/')}.html"
        urls.append(url_template.format(loc=loc, lastmod=current_date))

    return sitemap_template.format(urls="\\n".join(urls)).replace('\\n', '\n')

def main():
    with open("content.json", "r") as f:
        data = json.load(f)

    sitemap_xml = generate_sitemap(data)

    with open("sitemap.xml", "w") as f:
        f.write(sitemap_xml)
    print("Generated sitemap.xml")


if __name__ == "__main__":
    main()
