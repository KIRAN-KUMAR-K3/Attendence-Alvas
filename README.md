<h1 align="center">📷 Attendance-Alvas</h1>

<p align="center">
  <b>A Smart Face Recognition Attendance System</b><br>
  <i>Built with Deep Learning, Automated CSV Logging & Telegram Notifications</i>
</p>

<p align="center">
<a href="https://github.com/KIRAN-KUMAR-K3/Attendence-Alvas/blob/main/LICENSE">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License">
</a>
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/OpenCV-Face%20Recognition-success?style=for-the-badge&logo=opencv" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
</p>

---

## 📌 Overview

**Attendance-Alvas** is an intelligent, camera-based face recognition attendance system tailored for academic institutions like **ALVA'S Institute of Engineering and Technology**. It enables seamless attendance capture, training, logging, and daily reporting — all from a simple web interface.

> ✅ Train your dataset → 📸 Capture faces → 📊 Mark attendance → 📩 Get daily reports via Telegram.

---

## 🎯 Key Features

| Feature | Description |
|--------|-------------|
| 📸 **Face Capture** | Register student faces using webcam |
| 🧠 **Deep Learning Model** | Uses Haarcascade + LBPH recognizer for face detection & training |
| 💻 **Web Interface** | Register and manage students via simple HTML frontend |
| 🗂️ **CSV Export** | Auto-saves attendance logs in CSV format |
| 📲 **Telegram Bot** | Sends daily attendance report directly to your Telegram group |
| 🔐 **Secure** | Modify token or credentials securely within codebase |

---

## 🧰 Tech Stack

| Stack/Library         | Purpose                         |
|-----------------------|---------------------------------|
| 🐍 Python             | Backend scripting               |
| 📷 OpenCV             | Face detection & recognition    |
| 🧠 LBPH + Haarcascade | Facial recognition algorithms   |
| 🗃️ SQLite             | Local database for metadata     |
| 🧾 CSV Module         | Attendance logging              |
| 🌐 HTML               | Frontend interface              |
| 🤖 Telegram API       | Report notification system       |

---

## 📁 Folder Structure

```bash
Attendence-Alvas/
├── Attendance/               # Saved attendance images
├── ImagesUnknown/            # Unrecognized faces
├── StudentDetails/           # Student profile storage
├── TrainingImage/            # Raw training images
├── TrainingImageLabel/       # Labeled training images
├── templates/                # Web UI HTML files
│   └── signup1.html
├── haarcascade_frontalface_default.xml
├── gendb.db                  # SQLite3 DB
├── crtdb.py                  # DB creation script
├── train.py                  # Model training
├── last12.py                 # 🚀 Main app launcher
├── test_cam12.py             # Camera testing
├── requiremets.txt           # Dependency file
├── setup.py
└── README.md
````

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/KIRAN-KUMAR-K3/Attendence-Alvas.git
cd Attendence-Alvas
```

### 2️⃣ Install Dependencies

```bash
pip install -r requiremets.txt
```

> 💡 Tip: Use a Python virtual environment for clean installs.

---

## 🔐 Telegram Bot Setup

1. Search **BotFather** on Telegram and create your bot.
2. Copy your **bot token** and **chat ID**.
3. In `last12.py`, update the following:

```python
bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
```

---

## ▶️ Workflow

### 👤 Register Students

* Open `signup1.html` in browser
* Capture face and enter student details

### 🧠 Train the Model

```bash
python3 train.py
```

### 📷 Take Attendance

```bash
python3 last12.py
```

* Activates camera and matches faces
* Automatically logs attendance in a CSV
* Sends daily attendance CSV via Telegram

---

## 📊 Sample Output

```text
--- Attendance Marked ---
👨 Name: Ravi Sharma
📅 Date: 2025-08-01
⏱️ Time: 10:18:42
📌 Status: Present
📁 File Saved: Attendance/01-08-2025.csv
📤 Telegram report sent successfully!
```

---

## 🌟 Future Enhancements

* 🔍 Face accuracy boost via Dlib/CNN model
* 📊 Web dashboard for attendance visualization
* 📱 Android App Integration
* ☁️ Cloud-based DB support (e.g., Firebase/MySQL)
* 🧾 Auto-report scheduling via cron jobs

---

## 👨‍💻 Author

**Kiran Kumar K**
📧 [18kirankumar.k03@gmail.com](mailto:18kirankumar.k03@gmail.com)
🔗 [GitHub: @KIRAN-KUMAR-K3](https://github.com/KIRAN-KUMAR-K3)

---

## 📜 License

This project is licensed under the **MIT License** — use it freely with credit.
See the [LICENSE](LICENSE) file for more info.

---

> ⚡ Empowering institutions with smart, automated attendance — one face at a time.


