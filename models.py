from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, timedelta

db = SQLAlchemy()

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    dob = db.Column(db.String(20))
    content = db.Column(db.Text)

    word_count = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_edited = db.Column(db.DateTime, default=datetime.utcnow)

    download_count = db.Column(db.Integer, default=0)
    expiry_time = db.Column(
    db.DateTime,
    default=lambda: datetime.now(timezone.utc) + timedelta(hours=24)
)


class ShareHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume_id = db.Column(db.String(50))
    method = db.Column(db.String(20))
    recipient = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(100))
    resume_id = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class FeatureToggle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    download_enabled = db.Column(db.Boolean, default=True)
    email_enabled = db.Column(db.Boolean, default=True)
    whatsapp_enabled = db.Column(db.Boolean, default=True)