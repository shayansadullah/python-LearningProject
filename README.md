# Python Learning Project

A Python test automation project using Playwright and Pytest for learning purposes.

## Project Structure

```
python-LearningProject/
├── src/
│   ├── data/
│   │   ├── credentials.json          # Your credentials (gitignored)
│   │   └── credentials.json.example  # Template file
│   ├── pageObjects/
│   │   ├── __init__.py
│   │   ├── CartPage.py
│   │   ├── DashboardPage.py
│   │   └── LoginPage.py
│   └── utils/
│       ├── __init__.py
│       ├── apiBase.py
│       └── getCredentialsDetails.py
├── tests/
│   ├── test_api_call_framework.py
│   ├── test_api_call.py
│   ├── test_api_mock_response.py
│   ├── test_automationPractice.py
│   ├── test_login_verification.py
│   ├── test_pageObject_usage.py
│   ├── test_playwrightBasics.py
│   └── test_UIValidation.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Create Virtual Environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Install Playwright Browsers

```powershell
playwright install
```

### 4. Configure Credentials

Create a `credentials.json` file in the `src/data/` folder:

```powershell
Copy-Item src/data/credentials.json.example src/data/credentials.json
```

Then edit `src/data/credentials.json` with your actual credentials:

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

## Running Tests

### Run All Tests

```powershell
pytest
```

### Run Specific Test File

```powershell
pytest tests/test_login_verification.py
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
pytest -k "test_name"
```

## Test Categories

- **UI Tests**: Login verification, automation practice, page object patterns
- **API Tests**: Basic API calls, framework usage, mock responses
- **Playwright Basics**: Core Playwright functionality demonstrations

## How Fixtures Work: conftest.py Explained

Understanding how `test_login_verification.py` interacts with `conftest.py` fixtures (in simple terms):

### 1. The Test is the Customer

```python
async def test_first_authenticated_access(authenticated_page):
```

Your test says: **"I need an `authenticated_page` to do my work"** - just like ordering "I need a burger"

### 2. conftest.py is the Kitchen

Pytest looks at the parameter name `authenticated_page` and searches for a "recipe" (fixture) with that exact name in `conftest.py`:

```python
@pytest_asyncio.fixture(scope='function')
async def authenticated_page(authentication_state, browser_name):
```

**Found it!** This fixture is the recipe for making an `authenticated_page`.

### 3. But Wait - The Recipe Needs Ingredients!

The `authenticated_page` fixture says: **"I need `authentication_state` first"**

So pytest looks for THAT recipe:

```python
@pytest_asyncio.fixture(scope='session')
async def authentication_state(browser_type_launch_args, browser_name):
```

### 4. The Chain of Preparation

Here's the order things happen:

```
Test asks for: authenticated_page
    ↓
authenticated_page asks for: authentication_state
    ↓
authentication_state runs ONCE per session:
    - Opens browser
    - Logs in
    - Saves login cookies to file
    - Returns the filename
    ↓
authenticated_page runs for EACH test:
    - Takes the saved cookie file
    - Opens new browser with those cookies
    - Goes to dashboard (already logged in!)
    - Gives the DashboardPage to your test
    ↓
Your test runs:
    - Gets ready-to-use authenticated page
    - Checks URL
    - Does assertions
```

### 5. The Magic: Pytest Does All The Wiring

You **never** call these fixtures yourself. Just by writing:

```python
async def test_first_authenticated_access(authenticated_page):
                                          ^^^^^^^^^^^^^^^^^^
                                          This name is the key!
```

Pytest automatically:
1. Sees the parameter name
2. Finds the matching fixture in conftest.py
3. Runs all dependencies in the right order
4. Passes you the final result

### 6. Scope = How Often It's Made

- **`scope='session'`** - Make it ONCE and reuse (like brewing a pot of coffee at the start of the day)
- **`scope='function'`** - Make it fresh for EACH test (like making a fresh sandwich for each customer)

**That's why login happens once, but you get a fresh browser page for each test!**
