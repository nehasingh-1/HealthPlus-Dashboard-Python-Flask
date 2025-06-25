# 🩺 HealthPlus Dashboard – Python + Flask

A **responsive health monitoring dashboard** built with Flask that visualizes real-time patient health metrics using **Chart.js**. Secure login with session-based authentication, local storage using SQLite, and deployment-ready using Gunicorn + Nginx on Ubuntu with CI/CD support.

---

## 📌 Features

- ✅ Real-time chart visualizations using Chart.js
- ✅ Secure login with session-based authentication
- ✅ Flask backend with modular routing
- ✅ SQLite database for storing patient and health metrics
- ✅ Responsive UI (ready to extend with Bootstrap)
- ✅ Production-ready deployment (Gunicorn + Nginx)
- ✅ Clean and lightweight codebase

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, Chart.js
- **Backend:** Python, Flask
- **Database:** SQLite
- **Server:** Gunicorn + Nginx (Ubuntu)
- **Version Control:** Git & GitHub

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nehasingh-1/HealthPlus-Dashboard-Python-Flask.git
cd HealthPlus-Dashboard-Python-Flask
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Initialize the Database

```bash
sqlite3 healthplus.db < schema.sql
```

### 4️⃣ Run the Flask App

```bash
python app.py
```

Open your browser and visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔐 Login Credentials

```
Username: admin
Password: admin
```

---

## 📊 Dashboard Preview

![Dashboard Screenshot](https://via.placeholder.com/800x400?text=HealthPlus+Dashboard+Preview)

> Replace with your actual screenshot URL if available

---

## 🐧 Deployment (Gunicorn + Nginx on Ubuntu)

1. Setup virtual environment and dependencies
2. Use Gunicorn to serve Flask app:
   ```bash
   gunicorn -w 4 app:app
   ```
3. Configure Nginx as a reverse proxy
4. Setup `systemd` service for auto-restart
5. Integrate CI/CD using GitHub Actions (optional)

---

## 🙋‍♀️ Author

**Neha Singh**  
📍 Chandigarh University  
💼 Aspiring Full Stack Developer  

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐️ Show Your Support

If you like this project, don't forget to **star ⭐** the repo and share your feedback!
