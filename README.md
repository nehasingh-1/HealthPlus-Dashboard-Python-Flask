# HealthPlus Dashboard

## Description
A responsive health monitoring dashboard built with Python Flask. Displays real-time patient health data using Chart.js.

## Setup
1. Install dependencies:
```
pip install -r requirements.txt
```

2. Initialize database:
```
sqlite3 healthplus.db < schema.sql
```

3. Run the server:
```
python app.py
```

## Deployment
- Gunicorn + Nginx on Ubuntu with systemd service.