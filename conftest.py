"""Pytest configuration and fixtures for Playwright test automation.

Provides fixtures for browser automation, authentication state management,
and test tracing capabilities.
"""

import os

import pytest
import pytest_asyncio
from playwright.async_api import async_playwright


@pytest.fixture(scope="session")
def user_credentials(request):
    """Provide user credentials from parametrized test data.

    Args:
        request: Pytest request object containing parametrized credentials.

    Returns:
        dict: User credentials dictionary with userEmail and userPassword.

    """
    return request.param


@pytest_asyncio.fixture(scope="session")
async def authentication_state(browser_type_launch_args, browser_name):
    """Login once per session and save authentication state to file."""
    from playwright.async_api import async_playwright

    from src.pageObjects.LoginPage import LoginPage
    from src.utils.getCredentialsDetails import CredentialsReader

    # Get credentials
    test_data = CredentialsReader()
    credentials = test_data.get_cretdetials_details()[0]  # Use first credential

    state_file = "auth_state.json"

    # Perform login once and save state
    # Use async_playwright().start() to avoid event loop conflict
    playwright = await async_playwright().start()

    if browser_name == "chromium":
        browser = await playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = await playwright.firefox.launch(headless=True)
    elif browser_name == "webkit":
        browser = await playwright.webkit.launch(headless=True)
    else:
        browser = await playwright.chromium.launch(headless=True)

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
    await playwright.stop()

    yield state_file

    # Cleanup (commented out to keep auth_state.json for inspection)
    if os.path.exists(state_file):
        os.remove(state_file)


@pytest_asyncio.fixture(scope="function")
async def authenticated_page(authentication_state, browser_name, request):
    """Provide a browser page with pre-loaded authentication state."""
    from playwright.async_api import async_playwright

    from src.pageObjects.DashboardPage import DashboardPage

    # Use async_playwright().start() to avoid event loop conflict
    playwright = await async_playwright().start()

    if browser_name == "chromium":
        browser = await playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = await playwright.firefox.launch(headless=True)
    elif browser_name == "webkit":
        browser = await playwright.webkit.launch(headless=True)
    else:
        browser = await playwright.chromium.launch(headless=True)

    # Create context with saved authentication state
    context = await browser.new_context(storage_state=authentication_state)

    # Start tracing
    await context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = await context.new_page()

    # Navigate directly to dashboard (already authenticated)
    await page.goto(
        "https://rahulshettyacademy.com/client/#/dashboard/dash",
        wait_until="networkidle",
    )

    # Return DashboardPage object
    dashboardPage = DashboardPage(page)
    yield dashboardPage

    # Stop tracing and save
    test_name = request.node.name
    trace_dir = f"test-results/{test_name}"
    os.makedirs(trace_dir, exist_ok=True)
    await context.tracing.stop(path=f"{trace_dir}/trace.zip")

    await context.close()
    await browser.close()
    await playwright.stop()


@pytest_asyncio.fixture(scope="function")
async def page(request):
    """Provide a page with automatic tracing."""
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()

    # Start tracing
    await context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = await context.new_page()
    yield page

    # Stop tracing and save
    test_name = request.node.name
    trace_dir = f"test-results/{test_name}"
    os.makedirs(trace_dir, exist_ok=True)
    await context.tracing.stop(path=f"{trace_dir}/trace.zip")

    await page.close()
    await context.close()
    await browser.close()
    await playwright.stop()
