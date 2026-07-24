# 🚗 Car Service Booking System

A full-stack, commercial-grade **Car Service Booking Web Application** built using **Django 5**, **HTML5**, **Bootstrap 5**, and modern CSS design tokens. 

Designed for seamless vehicle maintenance scheduling, customer dashboard management, admin overview analytics, and instant deployment.

---

## 🌟 Key Features

### 👤 Customer Features
- **User Authentication**: Secure registration, login, and editable profile settings.
- **Customer Dashboard**: Overview stat cards for total registered vehicles, active bookings, pending approvals, and completed services.
- **Garage Management (CRUD)**: Add, edit, view, and delete vehicle records with custom registration badges.
- **Service Appointment Booking**: Interactive form with vehicle selector, service type dropdowns, and date/time pickers.
- **Appointments Management**: Filter bookings by status (*Pending, Confirmed, In Progress, Completed, Cancelled*) & search by vehicle registration number.
- **Invoice & Ticket Detail View**: Detailed summary breakdown including estimated labor time and price breakdown.
- **Completed Service History**: Log of all past finished services.

### 🛡️ Admin & Staff Features
- **Admin Dashboard**: System-wide statistics for total registered users, total vehicles, active services, and pending queue counts.
- **Django Admin Customization**: Filter and manage bookings, vehicles, and users with ease.

---

## 🛠️ Technology Stack

- **Backend**: Python 3 / Django 5
- **Frontend**: HTML5, Modern CSS3 (Glassmorphic cards, CSS variables, Google Fonts `Outfit` & `Poppins`, Bootstrap Icons)
- **Database**: SQLite3 (Local) / PostgreSQL compatible
- **Production Server**: Gunicorn & WhiteNoise (Static file management)

---

## 🚀 Local Development Setup

1. **Clone or Navigate to the Project**:
   ```bash
   cd C:\Users\MONIKAINIKA\Desktop\cars
   ```

2. **Activate Virtual Environment**:
   ```bash
   # Windows (PowerShell)
   .\myvenv\Scripts\Activate.ps1
   ```

3. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Run Server**:
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser.

---

## 🌐 Free One-Click Deployment Guide (Render)

This repository includes pre-configured `Procfile`, `render.yaml`, `build.sh`, and `requirements.txt` for deployment on **Render.com**.

### Step 1: Push Code to GitHub
1. Open terminal in project directory (`C:\Users\MONIKAINIKA\Desktop\cars`).
2. Run:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Redesigned UI and Deployment Ready"
   ```
3. Create a new public/private repository on GitHub and push:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/car-service-app.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Render
1. Go to [Render Dashboard](https://dashboard.render.com/) and sign in.
2. Click **New +** → **Web Service**.
3. Select **Build and deploy from a Git repository** and connect your GitHub repo.
4. Set the following settings:
   - **Name**: `car-service-app`
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn config.wsgi:application`
5. Under **Environment Variables**, add:
   - `SECRET_KEY`: `generate-any-random-secret-key-string`
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `.onrender.com`
6. Click **Create Web Service**.

Within 2 minutes, Render will build your application and generate your live public URL (e.g., `https://car-service-app.onrender.com`).

---

## 📝 License
Created as an MCA Final / Portfolio Project.
