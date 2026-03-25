# Python Learning Project

A Python test automation project using **Playwright** and **Pytest** for learning web UI and API testing with async/await patterns.

## 🎯 What This Project Covers

- ✅ Async/await patterns in Python with Playwright
- ✅ Page Object Model (POM) design pattern
- ✅ Data-driven testing with JSON files
- ✅ Pytest fixtures and conftest configuration
- ✅ API testing and mocking
- ✅ UI validation and assertions
- ✅ Window/popup handling
- ✅ Authentication state management
- ✅ Test markers for selective execution

## 📁 Project Structure

```
python-LearningProject/
├── src/
│   ├── data/
│   │   ├── credentials.json          # Your credentials (gitignored)
│   │   ├── credentials.json.example  # Template file
│   │   └── pagePractice.json         # Test data for parameterization
│   ├── pageObjects/
│   │   ├── __init__.py
│   │   ├── CartPage.py               # Cart page object
│   │   ├── DashboardPage.py          # Dashboard page object
│   │   └── LoginPage.py              # Login page object
│   └── utils/
│       ├── __init__.py
│       ├── apiBase.py                # API testing utilities
│       └── getCredentialsDetails.py  # Credential management
├── tests/
│   ├── test_api_call_framework.py    # API framework demos
│   ├── test_api_mock_response.py     # API mocking examples
│   ├── test_automationPractice.py    # General automation practice
│   ├── test_login_verification.py    # Login with fixtures
│   ├── test_pageObject_usage.py      # POM pattern usage
│   ├── test_playwrightBasics.py      # Core Playwright concepts
│   └── test_UIValidation.py          # UI validation & popup handling
├── conftest.py                        # Pytest fixtures & configuration
├── pytest.ini                         # Pytest settings & markers
├── requirements.txt                   # Python dependencies
├── auth_state.json                    # Saved authentication state
└── README.md
```

## 🚀 Setup Instructions

### 1. Create Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
.\.venv\Scripts\pip.exe install -r requirements.txt
```

### 3. Install Playwright Browsers

```powershell
playwright install
```

### 4. Configure Credentials

Create a `credentials.json` file in the `src/data/` folder:

```powershell
Copy-Item src\data\credentials.json.example src\data\credentials.json
```

Then edit `src\data\credentials.json` with your actual credentials:

```json
{
  "user_credentials": [
    {
      "userEmail": "your-email@example.com",
      "userPassword": "your-password-here"
    }
  ]
}
```

**Note:** The `credentials.json` file is gitignored for security.

## 🧪 Running Tests

### Run All Tests

```powershell
pytest
```

### Run Specific Test File

```powershell
pytest tests/test_UIValidation.py
```

### Run with Verbose Output

```powershell
pytest -v
```

### Run with Playwright in Headed Mode (visible browser)

```powershell
pytest --headed
```

### Run Specific Test by Name

```powershell
pytest -k "test_childWindowHandle"
```

### Run Smoke Tests Only

```powershell
pytest -m smoke
```

### Run Tests with Live Output

```powershell
pytest -s
```

## 🎬 Automatic Test Tracing

This project includes **automatic Playwright tracing** for all tests. Every test automatically records screenshots, snapshots, and network activity without any manual configuration.

### How It Works

The `page` fixture in `conftest.py` automatically:
- ✅ Starts tracing with `screenshots=True, snapshots=True, sources=True`
- ✅ Saves trace files to `test-results/{test_name}/trace.zip`
- ✅ Cleans up after each test

### What Gets Traced

Every test that uses the `page` fixture automatically captures:
- 📸 Screenshots at each step
- 🌐 Network requests and responses
- 📝 Console logs
- 🎯 DOM snapshots
- 📂 Source code

### Viewing Traces

After running tests, view the trace files with Playwright's trace viewer:

```powershell
playwright show-trace test-results/test_childWindowHandle/trace.zip
```

Or open the trace viewer in your browser:

```powershell
playwright show-trace test-results/test_UIValidation[user_credentials0]/trace.zip
```

### Trace Viewer Features

The trace viewer provides:
- **Timeline** - See every action in chronological order
- **Screenshots** - Visual snapshot at each step
- **Network** - All HTTP requests/responses
- **Console** - Browser console messages
- **Source** - Test code that triggered each action
- **Metadata** - Test duration, browser info, etc.

### Usage in Tests

Simply use the `page` fixture - tracing happens automatically:

```python
@pytest.mark.asyncio
async def test_example(page):
    await page.goto("https://example.com")
    await page.click(".button")
    # Trace automatically saved to test-results/test_example/trace.zip
```

For authenticated tests, use `authenticated_page` (also includes automatic tracing):

```python
@pytest.mark.asyncio
async def test_with_auth(authenticated_page):
    dashboardPage = authenticated_page
    # Tracing automatically enabled
```

### Trace File Location

```
test-results/
├── test_UIValidation[user_credentials0]/
│   └── trace.zip
├── test_childWindowHandle/
│   └── trace.zip
├── test_thirdCheck/
│   └── trace.zip
└── ...
```

**Note:** The `test-results/` directory is gitignored to avoid committing large trace files.

### Why This Matters

- 🐛 **Debug failures faster** - See exactly what happened step-by-step
- 📊 **Visual proof** - Screenshots show UI state at each action
- 🔍 **Network analysis** - Inspect API calls and responses
- ⏱️ **Performance insights** - See timing of each operation

## 🔑 Key Concepts

### Async/Await in Playwright

This project uses Playwright's **async API**, which requires understanding when to use `await`:

#### ✅ **DO await** - Actions that interact with the browser:
```python
await page.goto('url')              # Navigate
await page.click('.button')         # Click
await page.fill('input', 'text')    # Type
await page.check('#checkbox')       # Check
await asyncio.sleep(5)              # Async sleep
await expect(locator).to_be_visible() # Assertions
```

#### ❌ **DON'T await** - Locators (they're just selectors):
```python
locator = page.locator('.button')           # No await
filtered = locator.filter(has_text='text')  # No await
first_item = locator.first                  # No await
```

**Rule:** If it's *finding* something → no `await`. If it's *doing* something → use `await`.

### The `with` Statement

Use `with` for automatic resource cleanup:

```python
# File handling
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closes

# Async context managers
async with async_playwright() as playwright:
    browser = await playwright.chromium.launch()
# Browser automatically closes

# Popup handling
async with page.expect_popup() as popup_info:
    await page.click('.link-that-opens-popup')
childpage = await popup_info.value
```

**Rule:** If something needs `.close()` or cleanup → use `with`.

### Data-Driven Testing

Use `@pytest.mark.parametrize` with JSON data:

```python
import json

with open("src/data/pagePractice.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize('user_credentials', test_data['user_credentials'])
async def test_UIValidation(user_credentials):
    await page.fill('username', user_credentials['userEmail'])
    await page.fill('password', user_credentials['userPassword'])
```

### Popup/Child Window Handling

Pattern for handling popups in async Playwright:

```python
# Set up listener and trigger popup
async with page.expect_popup() as popup_info:
    await page.locator(".link").click()

# Work with popup after the block
childpage = await popup_info.value
text = await childpage.locator(".content").text_content()
```

## 📋 Test Categories

| Test File | Description | Key Concepts |
|-----------|-------------|--------------|
| `test_UIValidation.py` | UI validation with data-driven tests, popup handling | `@pytest.mark.parametrize`, `async with page.expect_popup()` |
| `test_login_verification.py` | Authentication with fixtures | Session-scoped fixtures, auth state management |
| `test_pageObject_usage.py` | Page Object Model pattern | POM design, reusable page classes |
| `test_playwrightBasics.py` | Core Playwright functionality | Locators, selectors, basic interactions |
| `test_automationPractice.py` | General automation exercises | Form filling, dropdowns, checkboxes |
| `test_api_call_framework.py` | API testing with framework | Requests library, API utilities |
| `test_api_mock_response.py` | API mocking and network interception | Mock responses, network control |

### Test Markers

Defined in `pytest.ini`:

- **`@pytest.mark.smoke`** - Quick validation tests for CI/CD pipelines

Run smoke tests: `pytest -m smoke`

## 🔧 How Fixtures Work: conftest.py Explained

Understanding how tests interact with fixtures in `conftest.py`:

### The Flow

```
1. Test declares what it needs:
   async def test_login(authenticated_page):
                       ^^^^^^^^^^^^^^^^^^
                       Parameter name = fixture name

2. Pytest finds the fixture in conftest.py:
   @pytest_asyncio.fixture(scope='function')
   async def authenticated_page(authentication_state):

3. Fixture declares its dependencies:
   This fixture needs 'authentication_state' first

4. Pytest resolves the dependency chain:
   authentication_state (session) → runs once
       ↓
   authenticated_page (function) → runs per test
       ↓
   test receives ready-to-use page object
```

### Fixture Scopes

- **`scope='session'`** - Created once for all tests (e.g., login state)
- **`scope='function'`** - Created fresh for each test (e.g., new page)

### Key Fixtures in This Project

- **`authentication_state`** - Logs in once, saves cookies to `auth_state.json`
- **`authenticated_page`** - Loads saved auth state, returns logged-in page
- **`user_credentials`** - Provides test credentials from JSON

## 📚 Important Libraries

| Library | Purpose | Import Example |
|---------|---------|----------------|
| `playwright` | Browser automation | `from playwright.async_api import async_playwright, expect` |
| `pytest` | Testing framework | `import pytest` |
| `pytest-asyncio` | Async test support | `@pytest.mark.asyncio` |
| `asyncio` | Python async utilities | `import asyncio` / `await asyncio.sleep()` |
| `requests` | HTTP/API testing | `import requests` |

## 🐛 Common Issues & Solutions

### Issue: `TypeError: object Locator can't be used in 'await' expression`
**Solution:** Don't await locators, only await actions:
```python
# ❌ Wrong
locator = await page.locator('.button')

# ✅ Correct
locator = page.locator('.button')
await locator.click()
```

### Issue: `TypeError: object NoneType can't be used in 'await' expression`
**Solution:** Use `asyncio.sleep()` instead of `time.sleep()`:
```python
# ❌ Wrong
await time.sleep(5)

# ✅ Correct
await asyncio.sleep(5)
```

### Issue: `'AsyncEventContextManager' object does not support the context manager protocol`
**Solution:** Use `async with` for async context managers:
```python
# ❌ Wrong
with page.expect_popup() as popup:

# ✅ Correct
async with page.expect_popup() as popup:
```

### Issue: `'coroutine' object has no attribute 'locator'`
**Solution:** Await the popup value:
```python
# ❌ Wrong
childpage = newPage_info.value

# ✅ Correct
childpage = await newPage_info.value
```

## 📖 Learning Resources

- [Playwright Python Docs](https://playwright.dev/python/docs/intro)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python Asyncio Guide](https://docs.python.org/3/library/asyncio.html)
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom)

## 🤝 Contributing

This is a learning project. Feel free to experiment, add new tests, and try different patterns!

## 📝 Notes

- Always activate the virtual environment before running tests
- Credentials are gitignored for security
- Authentication state is cached in `auth_state.json` for performance
- Use `pytest -s` to see print statements during test execution
- Use `--headed` flag to watch tests run in visible browser
