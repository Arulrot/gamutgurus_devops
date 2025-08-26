# 🚀 CI/CD for Python Flask App

## 📌 Project Overview
This project demonstrates a complete CI/CD pipeline for a **Python Flask web application** using industry-standard tools and cloud deployment.  
The goal is to automate **building, testing, linting, containerization, and deployment** to **AWS EC2 (or Kubernetes)** with minimal manual intervention.

---

## 🏗️ Architecture Diagram
```
┌────────┐      ┌──────────────┐        ┌────────┐         ┌──────────┐
│ GitHub │ ─→─ │ GitHub CI/CD │ ─→─ │ Jenkins │ ─→─ │ EC2/K8s │
└────────┘      └──────────────┘        └────────┘         └──────────┘
    ▲                │                   │                      │
    │                │                   │                      │
(code push)     (lint & test)      (build, test, deploy)   (Flask running)
```

---

## ⚙️ Tech Stack
| Layer            | Tools/Tech                  |
|------------------|-----------------------------|
| Source Control   | Git, GitHub                 |
| App Framework    | Python Flask                |
| CI               | GitHub Actions              |
| CD               | Jenkins                     |
| Containerization | Docker                      |
| Deployment       | AWS EC2 or Kubernetes       |
| Testing          | Pytest, Flake8              |

---

## 📂 Folder Structure
```
flask-app/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── .flake8
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

## 🛠️ Setup Instructions

### 1️⃣ Local Setup
Clone the repo:
```bash
git clone https://github.com/yourusername/flask-app.git
cd flask-app
```

Create virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Visit 👉 `http://localhost:5000`

---

### 2️⃣ Docker Setup
Build Docker image:
```bash
docker build -t flask-app .
```

Run Docker container:
```bash
docker run -d -p 80:5000 flask-app
```

---

### 3️⃣ GitHub Actions (CI)
On every **push or pull request**, GitHub Actions will:
- ✅ Lint with **flake8**  
- ✅ Run unit tests with **pytest**

---

### 4️⃣ Jenkins & AWS EC2 Deployment (CD)
Jenkins pipeline (defined in `Jenkinsfile`) will:
1. Clone the repo  
2. Build Docker image  
3. (Optional) Push to Docker Hub  
4. SSH into EC2 and deploy container  

---

## 🔌 API Endpoints

**GET /**  
Response:  
```json
{ "message": "Hello, World!" }
```

**GET /status**  
Response:  
```json
{ "status": "ok", "message": "App is healthy" }
```

---

## 🖥️ Sample API Response
```bash
$ curl http://localhost:5000/
{"message": "Hello, World!"}

$ curl http://localhost:5000/status
{"status": "ok", "message": "App is healthy"}
```

---

## 📸 Pipeline Screenshot Samples
- GitHub Actions CI ✅  
- Jenkins Build Logs 📜  
- Running Flask App 🌐  
- EC2 Terminal Deployment 💻  

---

## 🔄 Pipeline Summary
**CI (GitHub Actions)**  
- Triggered on push or pull requests  
- Steps: Lint (**flake8**), Unit tests (**pytest**)  

**CD (Jenkins)**  
- Triggered on main branch updates  
- Steps:  
  1. Checkout repo  
  2. Build Docker image  
  3. Run tests  
  4. Deploy to **EC2/Kubernetes**  

---

## 🗓️ Timeline
| Week | Tasks |
|------|-------|
| 1 | Build and Dockerize Flask app |
| 2 | Set up GitHub Actions: lint and test |
| 3 | Create Jenkins pipeline, build, (optionally push to DockerHub) |
| 4 | Deploy to EC2, create demo video, finalize project report |

---

## 🎯 Learning Outcomes
- Hands-on **CI/CD automation** for Python apps  
- Using **GitHub Actions** and **Jenkins** for pipelines  
- Creating and deploying **Docker containers**  
- Real-world deployment to **AWS EC2/Kubernetes**  

---
✍️ Maintained by **[Arulmohan P]**
