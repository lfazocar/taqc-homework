class Authentication():
    def __init__(self, page, username, password):
        self.page = page
        self.username = username
        self.password = password

    def login(self) -> None:
        login_button = self.page.locator("#login-button")
        username_input = self.page.locator("#user-name")
        password_input = self.page.locator("#password")

        username_input.fill(self.username)
        password_input.fill(self.password)
        login_button.click()

    def logout(self) -> None:
        sidebar_button = self.page.locator("#react-burger-menu-btn")
        sidebar_button.click()

        logout_button = self.page.wait_for_selector("#logout_sidebar_link")
        logout_button.click()
