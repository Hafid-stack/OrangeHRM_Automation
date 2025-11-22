import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_valid_admin_login(page: Page):
    # 1. Initialize the Page Object
    # We hand the 'page' fixture to our class so it can control the browser
    login_page = LoginPage(page)
    
    # 2. Perform Actions
    # Notice how readable this is? We don't see "page.locator(...).click()" here.
    login_page.navigate()
    login_page.login("Admin", "admin123")
    
    # 3. Assertions (Verification)
    # We check if the Dashboard header is visible to confirm login success
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()