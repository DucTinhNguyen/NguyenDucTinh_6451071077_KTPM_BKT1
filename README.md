# Selenium tests - UTC electronic office login

This project uses Selenium and pytest to check the login page at
`https://vanphongdientu.utc.edu.vn/Login?r=https%3A%2F%2Fvanphongdientu.utc.edu.vn%2F`.

The tests locate elements by their observed `name` and `id` attributes, and check
the login form and its links. They do not submit credentials or attempt to
authenticate against the live service.

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
