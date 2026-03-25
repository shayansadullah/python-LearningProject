# Python Learning Project

A Python learning project covering **Playwright/Pytest** test automation, **pandas** data manipulation, and **async/await** patterns.

## 📁 Project Structure

```
python-LearningProject/
├── data/
│   ├── example-1.json                # Sample JSON data for pandas practice
│   └── example-2.csv                 # Sample CSV data for pandas practice
├── notebook/
│   └── pandas.ipynb                  # Jupyter notebook for pandas learning
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
│       ├── getCredentialsDetails.py  # Credential management
│       └── pandasHelper.py           # Pandas utility functions
├── tests/
│   ├── test_api_call_framework.py    # API framework demos
│   ├── test_api_mock_response.py     # API mocking examples
│   ├── test_automationPractice.py    # General automation practice
│   ├── test_excel_pandas.py          # Pandas Excel/DataFrame testing
│   ├── test_login_verification.py    # Login with fixtures
│   ├── test_new_data_pandas.py       # Pandas data manipulation
│   ├── test_new_json_pandas.py       # JSON to DataFrame conversions
│   ├── test_new_pandas_with_realistic_data.py  # Realistic pandas scenarios
│   ├── test_pageObject_usage.py      # POM pattern usage
│   ├── test_playwrightBasics.py      # Core Playwright concepts
│   └── test_UIValidation.py          # UI validation & popup handling
├── conftest.py                        # Pytest fixtures & configuration
├── pytest.ini                         # Pytest settings & markers
├── requirements.txt                   # Python dependencies
├── auth_state.json                    # Saved authentication state
└── README.md
```

## 🚀 Setup

```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
.\.venv\Scripts\pip.exe install -r requirements.txt
playwright install

# Configure credentials (copy example and edit with your credentials)
Copy-Item src\data\credentials.json.example src\data\credentials.json
```

## 🧪 Running Tests

```powershell
pytest                              # Run all tests
pytest tests/test_UIValidation.py   # Run specific file
pytest -v                           # Verbose output
pytest --headed                     # Show browser
pytest -k "test_name"               # Run by name
pytest -m smoke                     # Run smoke tests only
```

## 🎬 Test Tracing

Tests automatically record traces (screenshots, network, console logs). View them with:

```powershell
playwright show-trace test-results/test_name/trace.zip
```

## 🔑 Key Concepts

**Async/Await:** Await actions (`await page.click()`), not locators (`page.locator()`)

**Context Managers:** Use `with` for file handling, `async with` for popups:
```python
async with page.expect_popup() as popup_info:
    await page.click('.link')
childpage = await popup_info.value
```

**Data-Driven Tests:** Use `@pytest.mark.parametrize` with JSON data

**Fixtures:** Tests use fixtures from `conftest.py` (e.g., `authenticated_page`, `page`)

## 📋 Tests

**Playwright/UI:** `test_UIValidation.py`, `test_login_verification.py`, `test_pageObject_usage.py`, `test_playwrightBasics.py`, `test_automationPractice.py`

**API:** `test_api_call_framework.py`, `test_api_mock_response.py`

**Pandas:** `test_excel_pandas.py`, `test_new_data_pandas.py`, `test_new_json_pandas.py`, `test_new_pandas_with_realistic_data.py`

**Markers:** Use `@pytest.mark.smoke` for quick validation tests

## 📚 Libraries

`playwright`, `pytest`, `pytest-asyncio`, `asyncio`, `requests`, `pandas`

## 🐛 Common Issues

- Don't `await` locators: `page.locator()` ✓, not `await page.locator()` ✗
- Use `await asyncio.sleep()`, not `await time.sleep()`
- Use `async with` for context managers: `async with page.expect_popup()`

## 📖 Resources

- [Playwright Python Docs](https://playwright.dev/python/docs/intro)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
