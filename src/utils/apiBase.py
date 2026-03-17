from playwright.async_api import Playwright

orderPayload = {
    "_id": "63c993f3568c3e9fb1fcd1c2",
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
    async def getToken(self, playwright: Playwright, user_credentials: dict):
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
        token = await self.getToken(playwright, user_credentials)
        api_request_context = await playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )
        response = await api_request_context.post(
            "/api/ecom/user/add-to-cart",
            data=orderPayload,
            headers={"Authorization": token, "Content-Type": "application/json"},
        )
        response_body = await response.json()
        return {"message": response_body["message"], "token": token}

    async def getOrderId(self):
        return orderPayload["product"]["_id"]
