# Python Learning Project

A Python learning project covering **Playwright/Pytest** test automation, **pandas** data manipulation, and **async/await** patterns.

## 📁 Project Structure

```
python-LearningProject/
├── data/
│   ├── credentials.json.example      # Credentials template
│   ├── example_lookup.xlsx           # Lookup table for Excel pandas practice
│   ├── example-1.json                # Sample JSON data for pandas practice
│   ├── example-2.csv                 # Sample CSV data for pandas practice
│   ├── example-3.csv                 # Additional CSV data for pandas practice
│   ├── example-4.json                # Additional JSON data for pandas practice
│   ├── mobile-phone-data.csv         # Mobile phone dataset for pandas practice
│   └── pagePractice.json.example     # Page practice data template
├── notebook/
│   └── pandas.ipynb                  # Jupyter notebook for pandas learning
├── src/
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
│   ├── test_database_mock.py         # Database mocking examples
│   ├── test_login_verification.py    # Login with fixtures
│   ├── test_pageObject_usage.py      # POM pattern usage
│   ├── test_pandas_excel.py          # Pandas Excel/DataFrame testing
│   ├── test_pandas_json.py           # JSON to DataFrame conversions
│   ├── test_pandas_new_data_columns.py  # Pandas data manipulation
│   ├── test_pandas_phone_prices.py   # Mobile phone price data analysis
│   ├── test_pandas_with_realistic_data.py  # Realistic pandas scenarios
│   ├── test_playwrightBasics.py      # Core Playwright concepts
│   └── test_UIValidation.py          # UI validation & popup handling
├── .pre-commit-config.yaml            # Pre-commit hook configuration
├── conftest.py                        # Pytest fixtures & configuration
├── pytest.ini                         # Pytest settings & markers
├── requirements.txt                   # Python dependencies
├── requirements-dev.txt               # Development dependencies
├── ruff.toml                          # Ruff linter configuration
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

# Install pre-commit hooks into git (required once per clone)
python pre-commit-4.5.1.pyz install

# Run all hooks against all files to fix existing issues before your first commit
# Hooks auto-fix what they can (line endings, formatting); re-run until all pass
python pre-commit-4.5.1.pyz run --all-files

# Configure credentials (copy example and edit with your credentials)
Copy-Item data\credentials.json.example data\credentials.json
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

**Database:** `test_database_mock.py`

**Pandas:** `test_pandas_excel.py`, `test_pandas_json.py`, `test_pandas_new_data_columns.py`, `test_pandas_phone_prices.py`, `test_pandas_with_realistic_data.py`

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
