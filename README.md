📁 Project Structure
resume_builder/
│
├── app.py                  # Main entry point (Flask app)
├── config.py               # Database & app configuration
├── requirements.txt        # All dependencies
├── README.md               # Project documentation
│
├── models/                 # Database models
│   ├── __init__.py
│   ├── resume_model.py
│   ├── activity_model.py
│   ├── share_model.py
│
├── routes/                 # API routes
│   ├── __init__.py
│   ├── resume_routes.py
│   ├── admin_routes.py
│
├── services/               # Business logic
│   ├── __init__.py
│   ├── pdf_service.py
│   ├── email_service.py
│   ├── whatsapp_service.py
│
├── utils/                  # Helper functions
│   ├── __init__.py
│   ├── analytics.py
│   ├── validator.py
│   ├── time_control.py
│
├── database/               # DB related files
│   └── db.py
│
├── static/                 # Generated files (PDFs)
│   └── resumes/
│
└── migrations/ (optional)  # For DB migration (if using Flask-Migrate)


# Resume_Builder_Backend
Dynamic Resume Builder with PDF generation, time-controlled access, analytics, and sharing via Email &amp; WhatsApp (Flask Backend).
# 🚀 Dynamic Resume Builder (Backend - Flask)

## 📌 Project Overview
This project is a **Dynamic Resume Builder Web Application Backend** developed using **Python (Flask)**. It allows users to create, manage, and share resumes with advanced features like PDF generation, password protection, analytics, and time-controlled access.

---

## 🎯 Key Features

### 📝 Resume Management
- Create, Read, Update, Delete (CRUD) APIs
- Unique Resume ID generation (RES-2026-XXXX)

### ⏳ Time-Controlled Access
- Resume form access limited to **20 minutes**
- Prevents submissions after expiry

### 📄 PDF Generation
- Generate formatted resume (2–3 pages)
- Download and print support

### 🔐 Password Protected PDF
- PDF secured with password format:

### 📊 Resume Analytics
- Word count
- Character count
- Paragraph count
- Estimated reading time

### ⚠️ Smart Validations
- Duplicate skill detection
- Resume length warning (>700 words)
- Input validation (email, phone, required fields)

### 📤 Sharing Features
- Send resume via **Email**
- Share via **WhatsApp (Twilio API)**
- Password included in sharing

### 📥 Download Tracking
- Track number of downloads per resume

### 🕒 Resume Expiry
- Download link valid for **24 hours only**

### 🧑‍💼 Admin Controls
- Enable/Disable features:
- Download
- Print
- Email
- WhatsApp
- Password protection

### 📜 Activity Logging
- Resume created
- PDF generated
- Downloaded
- Shared (Email/WhatsApp)

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** MySQL / SQLite
- **ORM:** SQLAlchemy
- **PDF Generation:** ReportLab
- **PDF Security:** PyPDF2
- **Email Service:** Flask-Mail
- **WhatsApp Integration:** Twilio API
- **CORS Handling:** Flask-CORS

---

## 📦 Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/resume-builder.git
cd resume-builder
