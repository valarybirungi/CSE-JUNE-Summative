# FCA Refugee Support Program

A responsive beneficiary registration app built from the FCA assessment brief using Django.

## Run locally

Python 3 is required. From this folder, activate the virtual environment and run:

```text
venv\Scripts\activate
python manage.py migrate
python manage.py runserver
```

Open http://localhost:8000/ or http://localhost:8000/register/ in a browser.

Registrations are stored in SQLite through the `POST /api/beneficiaries/` endpoint. The `GET /api/beneficiaries/` endpoint returns saved records.

## Included requirements

- FCA landing page and beneficiary registration form
- Frontend validation for required fields, minimum text lengths, and date ordering
- Female selected by default for gender
- Fixed nationality, marital status, and settlement camp options
- Success alert and full form reset after registration or alert close
- Backend HTTP routes and JSON persistence
- Responsive layout for smaller screens
