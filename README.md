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
