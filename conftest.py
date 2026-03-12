import pytest
import pytest_asyncio
from playwright.async_api import async_playwright
import os


@pytest.fixture(scope='session')
def user_credentials(request):
    return request.param

@pytest_asyncio.fixture(scope='session')
async def authentication_state(request):
    """Login once per session and save authentication state to file"""
    from src.utils.getCredentialsDetails import CredentialsReader
    from src.pageObjects.LoginPage import LoginPage

    # Get browser type
    try:
        browser_names = request.config.getoption("browser")
        browser_name = browser_names[0] if isinstance(browser_names, list) and browser_names else "chromium"
    except:
        browser_name = "chromium"

    # Get credentials
    test_data = CredentialsReader()
    credentials = test_data.get_cretdetials_details()[0]  # Use first credential

    state_file = "auth_state.json"

    # Perform login once and save state
    async with async_playwright() as playwright:
        if browser_name == "chromium":
            browser = await playwright.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = await playwright.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = await playwright.webkit.launch(headless=False)
        else:
            browser = await playwright.chromium.launch(headless=False)

        context = await browser.new_context()
        page = await context.new_page()

        # Login once
        print("\n🔐 Performing login (once per session)...")
        loginPage = LoginPage(page)
        await loginPage.navigate()
        await loginPage.login(credentials)

        # Wait for navigation to dashboard after login
        await page.wait_for_url("**/dashboard/dash", timeout=10000)
        print(f"   - Navigated to dashboard: {page.url}")

        # Save authentication state
        await context.storage_state(path=state_file)
        print(f"✅ Authentication state saved to {state_file}")

        await context.close()
        await browser.close()

    yield state_file

    # Cleanup (commented out to keep auth_state.json for inspection)
    if os.path.exists(state_file):
         os.remove(state_file)


@pytest_asyncio.fixture(scope='function')
async def authenticated_page(request, authentication_state):
    """Provides a browser page with pre-loaded authentication state"""
    from src.pageObjects.DashboardPage import DashboardPage

    # Get browser type
    try:
        browser_names = request.config.getoption("browser")
        browser_name = browser_names[0] if isinstance(browser_names, list) and browser_names else "chromium"
    except:
        browser_name = "chromium"

    async with async_playwright() as playwright:
        if browser_name == "chromium":
            browser = await playwright.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = await playwright.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = await playwright.webkit.launch(headless=False)
        else:
            browser = await playwright.chromium.launch(headless=False)

        # Create context with saved authentication state
        context = await browser.new_context(storage_state=authentication_state)
        page = await context.new_page()

        # Navigate directly to dashboard (already authenticated)
        await page.goto('https://rahulshettyacademy.com/client/#/dashboard/dash', wait_until='networkidle')

        # Return DashboardPage object
        dashboardPage = DashboardPage(page)
        yield dashboardPage

        await context.close()
        await browser.close()