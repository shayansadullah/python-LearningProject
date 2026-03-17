"""Page Object Model for the login page."""

from src.pageObjects.DashboardPage import DashboardPage


class LoginPage:
    """Represents the login page with methods for authentication."""

    def __init__(self, page):
        """Initialize LoginPage with a Playwright page instance.

        Args:
            page: Playwright page object for browser automation.

        """
        self.page = page

    async def navigate(self):
        """Navigate to the login page."""
        await self.page.goto("https://rahulshettyacademy.com/client")

    async def login(self, user_credentials: dict):
        """Perform login with provided credentials.

        Args:
            user_credentials: Dictionary containing userEmail and userPassword.

        Returns:
            DashboardPage: DashboardPage instance after successful login.

        """
        await self.page.get_by_placeholder("email@example.com").fill(
            user_credentials["userEmail"]
        )
        await self.page.get_by_placeholder("enter your passsword").fill(
            user_credentials["userPassword"]
        )
        await self.page.get_by_role("button", name="Login").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage
