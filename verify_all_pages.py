
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    # Ensure the verification directory exists
    output_dir = "/home/jules/verification"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get the absolute path to the repository
    repo_root = os.path.abspath(os.getcwd())

    # List of all HTML files to verify
    html_files = [
        "index.html",
        "about.html",
        "automation.html",
        "deep-dive.html",
        "identity.html",
        "phil-hills-seattle.html",
        "contact.html",
        "neighborhoods/ballard.html",
        "neighborhoods/capitol-hill.html",
        "neighborhoods/west-seattle.html",
        "neighborhoods/queen-anne.html",
        "neighborhoods/index.html",
        "insights/index.html",
    ]

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for file_path in html_files:
            # Construct the full, absolute path to the HTML file
            absolute_file_path = os.path.join(repo_root, file_path)

            # Use file:// protocol for local files
            await page.goto(f"file://{absolute_file_path}")

            # Inject a <base> tag to fix root-relative CSS paths
            await page.evaluate(f"""
                const base = document.createElement('base');
                base.href = 'file://{repo_root}/';
                document.head.prepend(base);
            """)

            # Wait for the page to re-evaluate with the new base href
            await page.wait_for_timeout(100)

            # Create a unique filename by replacing slashes with underscores
            unique_filename = file_path.replace('/', '_')
            screenshot_path = os.path.join(output_dir, f"final-{unique_filename}.png")
            await page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved to {screenshot_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
