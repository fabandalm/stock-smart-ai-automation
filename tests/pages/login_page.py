from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.close_button = page.locator("button:has-text('Close modal')")
        self.logout_link = page.get_by_role("link", name="Logout")

    def goto(self):
        self.page.goto("http://localhost")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.page.wait_for_timeout(1000)
        self.login_button.click()
        self.page.wait_for_timeout(1000)
        self.close_button.click()
        self.page.wait_for_timeout(1000)

    def get_error_message(self):
        return self.error_message.text_content()

