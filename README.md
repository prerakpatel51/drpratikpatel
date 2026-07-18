# Dr. Pratik Patel — Django website

A standard Django website using server-rendered HTML templates, plain CSS, and plain JavaScript. It is configured for Railway with Gunicorn and WhiteNoise.

## Run locally

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
DJANGO_DEBUG=true python manage.py runserver
```

Open `http://127.0.0.1:8000`.

## Railway

The included `railway.json` collects static assets, runs Django's deployment checks, starts Gunicorn on Railway's assigned port, and exposes `/health/` for health checks.
