# Infinity Lock — Render deployment

Render settings:
- Service type: Web Service
- Runtime: Python
- Build command: `pip install -r requirements.txt`
- Start command: `python app.py`
- Compute plan: Free

The app binds to `0.0.0.0` and Render's `PORT` environment variable automatically.
