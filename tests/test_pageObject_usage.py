import pytest


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_pageObject_usage(authenticated_page):
    """Test using authenticated page - login performed once in session"""
    dashBoardPage = authenticated_page
    cartPage = await dashBoardPage.add_to_cart("ADIDAS ORIGINAL")
    await cartPage.navigate()
    cart_item = await cartPage.get_cart_item("ADIDAS ORIGINAL")
    print(f"This is the {cart_item}")
    assert "ADIDAS ORIGINAL" in cart_item


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_pageObject_usage2(authenticated_page):
    """Test using authenticated page - reuses saved authentication state"""
    dashBoardPage = authenticated_page
    cartPage = await dashBoardPage.add_to_cart("ADIDAS ORIGINAL")
    await cartPage.navigate()
    cart_item = await cartPage.get_cart_item("ADIDAS ORIGINAL")
    print(f"This is the {cart_item}")
    assert "ADIDAS ORIGINAL" in cart_item
