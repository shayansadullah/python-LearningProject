import pytest

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_first_authenticated_access(authenticated_page):
    """Verify first test has authenticated access"""
    dashBoardPage = authenticated_page
    # Check current URL and page state
    current_url = dashBoardPage.page.url
    print(f"\n✅ Test 1: Current URL = {current_url}")
    print(f"   - Should be on dashboard: {'/dashboard/dash' in current_url}")
    assert '/dashboard/dash' in current_url, "Should be on dashboard page"


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_second_authenticated_access(authenticated_page):
    """Verify second test reuses authentication without login"""
    dashBoardPage = authenticated_page
    # Check we're immediately on dashboard (no login needed)
    current_url = dashBoardPage.page.url
    print(f"\n✅ Test 2: Current URL = {current_url}")
    print(f"   - Already on dashboard: {'/dashboard/dash' in current_url}")
    assert '/dashboard/dash' in current_url, "Should already be on dashboard page"
