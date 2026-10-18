# FoodRescue Cloud

A beginner-friendly cloud computing project built with Flask and PostgreSQL. Users can submit surplus food donation records and view recent entries.

## Features
- Responsive web interface
- Create and list food donations
- PostgreSQL database on Render (SQLite fallback for local testing)
- `/health` endpoint to verify app and database connectivity
- Gunicorn production server
- Render Blueprint configuration in `render.yaml`

## Run locally
1. Install Python 3.10 or newer.
2. Create a virtual environment (optional but recommended).
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python app.py`
5. Open `http://127.0.0.1:5000`

Local mode uses SQLite automatically unless `DATABASE_URL` is configured.

## Deploy to Render
1. Upload this project to a GitHub repository.
2. Sign in to Render and choose **New + → Blueprint**.
3. Connect the repository containing `render.yaml`.
4. Review the web service and PostgreSQL database resources, then deploy.
5. Wait for deployment to finish. Open the generated `https://...onrender.com` URL.
6. Test by adding a sample donation and refreshing the page.
7. Open `/health` on the same domain. Expected result: `{"database":"connected","status":"ok"}`.
8. Take a screenshot of the running app with the URL visible and insert it in the report.

## Cloud concepts demonstrated
- **Compute / application hosting:** Render web service runs the Flask application.
- **Managed database / storage:** Render PostgreSQL stores donation records.
- **Internet accessibility:** the deployed HTTPS URL is accessible online.
- **Resource configuration:** `render.yaml` describes the web service and database.
- **Monitoring / health check:** `/health` checks the database connection.

## Suggested test data
Food item: Fresh vegetables
Quantity: 5 meal boxes
Pickup location: Bhavnagar
Contact details: demo@example.com
Additional notes: Sample record for assignment demonstration

Use fictional test contact details only. Do not enter private personal data into a public student demo.
