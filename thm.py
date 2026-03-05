from playwright.sync_api import sync_playwright

EMAIL = "gayleen3@ptct.net"
PASSWORD = "gayleen3@ptct.netV"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://tryhackme.com/login")

    page.fill('input[type="email"]', EMAIL)
    page.fill('input[type="password"]', PASSWORD)

    page.click('button[type="submit"]')

    page.wait_for_timeout(5000)

    page.goto("https://tryhackme.com/room/tutorial")

    page.wait_for_timeout(5000)

    try:
        page.click("text=Complete")
    except:
        pass

    browser.close()
