from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators - We define them once here.
        # If the ID changes later, we only fix it here, not in 50 different tests.
        self.username_input = page.locator("input[name='Admin']")
        self.password_input = page.locator("input[name='admin123']")
        self.login_button = page.locator("button[type='submit']")
    
    def navigate(self):
        """Go to the OrangeHRM login page"""
        self.page.goto("https://opensource-demo.orangehrmlive.com/")
    
    def login(self, username, password):
        """Perform the login action"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        