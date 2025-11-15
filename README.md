# 🧠 Backend-Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge"/>
  <img src="https://img.shields.io/badge/TypeScript-3178c6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript Badge"/>
  <img src="https://img.shields.io/badge/HTML5-e34f26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5 Badge"/>
  <img src="https://img.shields.io/badge/JavaScript-f7df1e?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript Badge"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge"/>
  <img src="https://img.shields.io/badge/License-Educational-informational?style=for-the-badge" alt="License Badge"/>
</p>

Welcome to my **Backend Development Learning Repository** — a hands-on journey from client–server fundamentals to building full Flask REST APIs.

This repo documents my **daily learning notes, code snippets, and mini-projects** as I progress through major backend engineering topics.

---

## 📚 Repository Structure

| Folder / File                     | Description                                                                        |
|------------------------------------|------------------------------------------------------------------------------------|
| **Day1_notes.md → Day5_notes.md**  | Detailed daily notes covering backend concepts, syntax refreshers, and DSA drills. |
| **FLASK/**                        | Flask environment setup, routes, CRUD API for a Todo app (comments, error handling).|
| **REST_API/**                     | REST API practice using `requests`, `curl`, and Postman.                           |
| **HTML+JS/**                      | HTML forms and JS fetch examples for API interaction.                              |
| **README.md**                     | This file — quick reference & setup guide for the repository.                      |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Rishilshajan/Backend-learning.git
cd Backend-learning
```

### 2. (Optional) Create a Virtual Environment

Recommended for Flask and Python API development.

```bash
python3 -m venv venv
# Activate the virtual environment:
source venv/bin/activate     # For Linux/Mac
venv\Scripts\activate        # For Windows
```

### 3. Install Dependencies

```bash
pip install flask requests
```

---

## 🚀 Running the Flask Todo API

- **Location:** `FLASK/app.py`

**Run the app:**

```bash
cd FLASK
python app.py
```

**Open in your browser:**

[http://127.0.0.1:5000](http://127.0.0.1:5000)

#### 📌 Example API Endpoints

| Method | Endpoint         | Description               |
|--------|------------------|--------------------------|
| GET    | `/todos`         | List all todos           |
| GET    | `/todos/<id>`    | Get a specific todo      |
| POST   | `/todos`         | Create a new todo        |
| PUT    | `/todos/<id>`    | Replace an existing todo |
| PATCH  | `/todos/<id>`    | Partially update a todo  |
| DELETE | `/todos/<id>`    | Delete a todo            |

- All routes support **JSON request/response**.
- Proper status codes: `200, 201, 400, 404`.
- Inline comments provided for clarity.

---

## 🧰 Tools & Technologies

| Category              | Tools Used                             |
|-----------------------|----------------------------------------|
| Languages             | Python, JavaScript, HTML, TypeScript   |
| Frameworks/Libraries  | Flask, Requests                        |
| Version Control       | Git & GitHub                           |
| Testing Tools         | Postman, curl                          |

---

## 💡 Learning Focus Areas

- ✅ REST vs GraphQL
- ✅ HTTP Methods & Status Codes
- ✅ Git & Version Control
- ✅ JSON Parsing in Python
- ✅ Flask CRUD API Development
- ✅ DSA Practice (Stacks, Queues, etc.)
- ✅ HTML + JS Fetch Requests
- ✅ TypeScript Object & Interface Concepts

---

## 🧮 Future Plans

- Integrate SQLite / SQLAlchemy for Todo persistence
- Add authentication (Flask-Login / JWT)
- Deploy Flask API using Render or Railway
- Build a front-end (React or plain JS) that consumes the Flask API

---

## 🧑‍💻 Author

**Rishil Shajan**  
📧 [rishilshajan1@gmail.com](mailto:rishilshajan1@gmail.com)  
🎓 B.Tech (Hons) – Computer Science & Engineering (Machine Learning)  
📍 Amal Jyothi College of Engineering, Kerala

---

## 🏷️ License

This repository is for educational purposes.  
Feel free to fork, study, or reuse the material **with proper credit**.

⭐ _If you find this helpful, consider giving the repo a star!_

---
