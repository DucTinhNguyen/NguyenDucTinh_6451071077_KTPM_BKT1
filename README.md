# Selenium tests - UTC electronic office login

This project uses Selenium and pytest to check the login page at
`https://vanphongdientu.utc.edu.vn/Login?r=https%3A%2F%2Fvanphongdientu.utc.edu.vn%2F`.

The tests locate elements by their observed `name` and `id` attributes, and check
the login form and its links. They do not submit credentials or attempt to
authenticate against the live service.

## Project structure

```text
base/
  base_test.py       # Shared browser setup
pages/
  base_page.py       # Common wait, click, typing, and read operations
  login_page.py      # Login page locators and page actions
tests/
  test_login.py      # Ten UI/form test cases
conftest.py          # pytest browser and page fixtures
```

The layout follows the slide's separation of shared test setup, page objects,
and test scripts. Locators are private to the page object; assertions remain
in the test cases.

## Setup

```powershell
py -m pip install -r requirements.txt
```

Chrome must be installed. Selenium Manager obtains a compatible driver when the
tests run.

## Run

```powershell
py -m pytest -v
```

To run against an authorized test/staging environment, set `LOGIN_URL` to its
login page URL before running pytest:

```powershell
$env:LOGIN_URL = "https://staging.example.test/Login"
py -m pytest -v
```

The suite contains ten independent UI/form test cases. Authentication success
and failure cases are intentionally not submitted because no test account or
non-production endpoint was provided.

## Intentional failure demonstration

`tests/test_expected_failure.py` contains one deliberately incorrect title
expectation for demonstrating a pytest failure. Run it separately:

```powershell
py -m pytest -v tests/test_expected_failure.py
```

The regular login tests can be run without this demonstration case:

```powershell
py -m pytest -v --ignore=tests/test_expected_failure.py
```
