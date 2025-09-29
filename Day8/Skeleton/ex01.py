import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Step 1. Create a browser
    # Can use chromium/firefox/webkit
    browser = p.chromium.launch(headless=False)

    # Step 2. Create a new BrowserContext
    context = browser.new_context()
    page = context.new_page()

    # Step 3. Open a page
    page.goto("https://reddit.com")
    # time.sleep(5)
    page.wait_for_selector("main")
    for anchor in page.query_selector_all("a"):
        print(anchor.get_attribute("href"))
    browser.close()

    # print(page.title())
