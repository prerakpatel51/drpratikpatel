# Dr. Pratik Patel, Django website

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

## Google reviews

After the independent Google Business Profile is verified, add these Railway variables:

- `GOOGLE_REVIEW_URL`: the public Google profile or reviews link
- `GOOGLE_REVIEW_WRITE_URL`: the direct link for writing a Google review

The Google Reviews section remains hidden until at least one of these links is configured. The website does not display a rating or review count that cannot be verified.
