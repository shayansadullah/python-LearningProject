"""Page Object Model for the dashboard page."""

from src.pageObjects.CartPage import CartPage


class DashboardPage:
    """Represents the dashboard page with methods to interact with products."""

    def __init__(self, page):
        """Initialize DashboardPage with a Playwright page instance.

        Args:
            page: Playwright page object for browser automation.

        """
        self.page = page

    async def add_to_cart(self, product_name):
        """Add a product to cart by product name.

        Args:
            product_name: Name of the product to add to cart.

        Returns:
            CartPage: CartPage instance for further interactions.

        """
        await (
            self.page.locator(".col-lg-4")
            .filter(has_text=product_name)
            .get_by_role("button", name="Add To Cart")
            .click()
        )
        cartPage = CartPage(self.page)
        return cartPage
