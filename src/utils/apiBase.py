"""API utility functions for authentication and order management."""

from playwright.async_api import Playwright

orderPayload = {
    "_id": "69ceb9c2f86ba51a6541cc34",
    "product": {
        "_id": "6960eae1c941646b7a8b3ed3",
        "productName": "ADIDAS ORIGINAL",
        "productCategory": "electronics",
        "productSubCategory": "mobiles",
        "productPrice": 11500,
        "productDescription": "Apple phone",
        "productImage": "https://rahulshettyacademy.com/api/ecom/uploads/productImage_1767959265156.jpg",
        "productRating": "0",
        "productTotalOrders": "0",
        "productStatus": "true",
        "productFor": "women",
        "productAddedBy": "admin",
        "__v": 0,
    },
}


class APIUtils:
    """Utility class for API operations including authentication and orders."""

    async def getToken(self, playwright: Playwright, user_credentials: dict):
        """Get authentication token via API login.

        Args:
            playwright: Playwright instance for API requests.
            user_credentials: Dictionary containing userEmail and userPassword.

        Returns:
            str: Authentication token.

        """
        api_request_context = await playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )
        response = await api_request_context.post(
            "/api/ecom/auth/login", data=user_credentials
        )
        assert response.ok
        response_json = await response.json()
        print(response_json)
        token = response_json["token"]
        return token

    async def createOrder(self, playwright: Playwright, user_credentials: dict):
        """Create an order via API.

        Args:
            playwright: Playwright instance for API requests.
            user_credentials: Dictionary containing userEmail and userPassword.

        Returns:
            dict: Dictionary with message and token.

        """
        token = await self.getToken(playwright, user_credentials)
        api_request_context = await playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )
        response = await api_request_context.post(
            "/api/ecom/user/add-to-cart",
            data=orderPayload,
            headers={"Authorization": token},
        )
        response_body = await response.json()
        print(f"add-to-cart status: {response.status}, body: {response_body}")
        return {"message": response_body["message"], "token": token}

    async def getOrderId(self):
        """Get the product ID from order payload.

        Returns:
            str: Product ID from the order payload.

        """
        return orderPayload["product"]["_id"]
