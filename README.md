# Testr (prototype)

The first prototype of **Testr**, an exam question-bank platform for storing past-paper questions and answers. This version is a plain Django project that defines the core data model and uses the Django admin to enter data.

It was later replaced by a separate API and front end:
- [Testr_Backend](https://github.com/Gladiathor1/Testr_Backend) — Django REST API
- [Testr_Frontend](https://github.com/Gladiathor1/Testr_Frontend) — web UI

## Data model

All models live in the `store` app (`store/models/`):

| Model | Description |
| --- | --- |
| `Discipline` | Exam board / qualification level |
| `Subject` | Subject within a discipline |
| `Topic` | Topic within a subject |
| `Tags` | Links a subject to a topic for tagging questions |
| `Papers_type` | Kind of paper (e.g. multiple choice, theory) |
| `Paper` | A past paper: number, date, type, subject, discipline and the uploaded PDF |
| `Question` | A question with difficulty, type, linked paper, image, answer, tag and discipline |
| `Answer` | Answer text with an optional image |
| `Image` | Uploaded image for questions/answers |

Uploaded files are stored under `uploads/` (`uploads/papers/` contains sample past papers).

## Tech stack

- Python 3, Django 3.2
- MySQL

## Getting started

```bash
pip install django mysqlclient pillow
```

Create a MySQL database named `Testr` and update the `DATABASES` settings (user, password, host) in `Testr/settings.py`. Then:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- `http://127.0.0.1:8000/admin/` — manage disciplines, subjects, papers and questions
- `http://127.0.0.1:8000/` — placeholder landing page
