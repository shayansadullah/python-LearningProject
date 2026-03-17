"""Page Object Model for the cart page."""


class CartPage:
    """Represents the shopping cart page with methods to interact with cart items."""

    def __init__(self, page):
        """Initialize CartPage with a Playwright page instance.

        Args:
            page: Playwright page object for browser automation.

        """
        self.page = page

    async def navigate(self):
        """Navigate to the cart page."""
        await self.page.goto("https://rahulshettyacademy.com/client/#/dashboard/cart")

    async def get_cart_item(self, product_name):
        """Retrieve cart item text content by product name.

        Args:
            product_name: Name of the product to find in cart.

        Returns:
            str: Text content of the cart item matching the product name.

        """
        return (
            await self.page.locator("li.items")
            .filter(has_text=product_name)
            .text_content()
        )
