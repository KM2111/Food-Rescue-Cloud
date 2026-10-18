import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "foodrescue-demo-key-change-before-production")

database_url = os.environ.get("DATABASE_URL", "sqlite:///foodrescue.db")
# Render PostgreSQL URLs may use postgres://; SQLAlchemy expects postgresql://.
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(160), nullable=False)
    contact = db.Column(db.String(120), nullable=False)
    notes = db.Column(db.String(300), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    donations = Donation.query.order_by(Donation.created_at.desc()).limit(20).all()
    total = Donation.query.count()
    return render_template("index.html", donations=donations, total=total)

@app.route("/donate", methods=["POST"])
def donate():
    food_name = request.form.get("food_name", "").strip()
    quantity = request.form.get("quantity", "").strip()
    location = request.form.get("location", "").strip()
    contact = request.form.get("contact", "").strip()
    notes = request.form.get("notes", "").strip()

    if not all([food_name, quantity, location, contact]):
        flash("Please complete all required fields.", "error")
        return redirect(url_for("index"))

    donation = Donation(
        food_name=food_name[:120],
        quantity=quantity[:80],
        location=location[:160],
        contact=contact[:120],
        notes=notes[:300] or None
    )
    db.session.add(donation)
    db.session.commit()
    flash("Donation added successfully. Thank you for reducing food waste!", "success")
    return redirect(url_for("index"))

@app.route("/health")
def health():
    try:
        db.session.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}, 200
    except Exception as exc:
        return {"status": "error", "message": str(exc)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
