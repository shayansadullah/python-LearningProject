from src.pageObjects.DashboardPage import DashboardPage


class LoginPage:
    def __init__(self, page):
        self.page = page

    async def navigate(self):
        await self.page.goto("https://rahulshettyacademy.com/client")

    async def login(self, user_credentials: dict):
        await self.page.get_by_placeholder("email@example.com").fill(
            user_credentials["userEmail"]
        )
        await self.page.get_by_placeholder("enter your passsword").fill(
            user_credentials["userPassword"]
        )
        await self.page.get_by_role("button", name="Login").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage
