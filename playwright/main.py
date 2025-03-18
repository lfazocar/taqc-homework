import random
from playwright.sync_api import sync_playwright
from utils.auth import Authentication

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(URL, wait_until="domcontentloaded")

    auth = Authentication(page, USERNAME, PASSWORD)
    auth.login()

    page.wait_for_selector("#inventory_container")
    inventory = page.locator(".inventory_item")

    rng = random.randint(0, inventory.count() - 1)
    random_item = inventory.nth(rng)

    add_to_cart = random_item.get_by_role("button", name="Add to cart")
    add_to_cart.click()

    cart = page.locator("#shopping_cart_container")
    cart.click()
    page.wait_for_selector("#cart_contents_container")

    auth.logout()
    browser.close()
