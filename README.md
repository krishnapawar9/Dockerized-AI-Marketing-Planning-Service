# 📈 Dockerized AI Marketing Planning Service

An AI-powered marketing planning system that generates structured marketing strategies using **LangChain, Streamlit, and MySQL**, packaged with **Docker** and integrated with **GitHub Actions CI**.

This project demonstrates an **agentic AI workflow** combined with **DevOps practices** such as containerization, service orchestration, environment consistency, and continuous integration.

---

## 📝 Problem Statement

Build and deploy a **Dockerized AI Marketing Planning Service** using modern DevOps practices.

The objective is to containerize the application, connect it with a MySQL database, manage multi-service execution using Docker Compose, and automate validation using GitHub Actions CI.

This ensures:
- consistent development and runtime environment
- portability across systems
- easier deployment and maintenance
- improved reliability through CI checks

---

## 🚀 Features

- ✅ AI-based Marketing Plan Generation
- ✅ Goal Decomposition into Structured Tasks
- ✅ Marketing Resource Validation
- ✅ Budget and Keyword Assistance
- ✅ Optimized Campaign Scheduling
- ✅ Interactive Streamlit Interface
- ✅ Dark Mode Toggle
- ✅ MySQL-based Plan History
- ✅ Search / Filter Previous Plans
- ✅ Delete Individual Plans
- ✅ Clear Entire History
- ✅ PDF Export
- ✅ Dockerized Deployment
- ✅ GitHub Actions CI Pipeline

---

## 🧠 Tech Stack

### Application
- Python
- LangChain
- Streamlit
- MySQL
- ReportLab
- Pydantic
- Python Dotenv

### DevOps / Deployment
- Git
- GitHub
- Docker
- Docker Compose
- GitHub Actions

---

## 📂 Project Structure

```text
Dockerized-AI-Marketing-Planning-Service/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tools/
│   ├── ad_library_tool.py
│   ├── budget_tool.py
│   ├── keyword_tool.py
│   └── scheduler_tool.py
├── .dockerignore
├── .env
├── .gitignore
├── Dockerfile
├── README.md
├── __init__.py
├── agent.py
├── config.py
├── database_mysql.py
├── docker-compose.yml
├── init.sql
├── main.py
├── planner.py
├── requirements.txt
└── streamlit_app.py

```
---
## 🖥️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/krishnapawar9/Dockerized-AI-Marketing-Planning-Service.git
cd Dockerized-AI-Marketing-Planning-Service
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file and add:

```env
GOOGLE_API_KEY=your_google_api_key
MODEL_NAME=gemini-2.5-flash
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=marketing_agent
```

> Make sure a local MySQL server is running and the `marketing_agent` database is available before starting the application.

### 4. Run the application

```bash
streamlit run streamlit_app.py
```

---

## 🐳 Run with Docker

### Build and start containers

```bash
docker compose up --build
```

### Access the app

```text
http://localhost:8501
```

---
## ⚙️ How It Works

1. The user enters a marketing goal in the Streamlit interface.
2. The AI agent processes the input and decomposes it into a structured marketing plan.
3. Supporting tools assist with keyword suggestions, budget estimation, ad-related insights, and scheduling.
4. The generated plan is stored in the MySQL database.
5. Users can search, load, delete, refresh, or export generated plans as PDF.
6. Docker Compose runs both the application and database in a consistent multi-container environment.

---

## 🗄️ Database

The application uses **MySQL** for persistent storage of generated marketing plans.

Stored information includes:
- plan ID
- user goal
- generated marketing plan
- creation timestamp

A Docker volume is used to preserve database data across container restarts.

---

## 🔁 CI Pipeline

This project includes a **GitHub Actions CI pipeline** for basic continuous integration.

On every push or pull request, the pipeline:
- checks out the repository
- sets up Python
- installs dependencies
- performs basic Python validation
- builds the Docker image

This helps maintain code quality and deployment readiness.

---

## ☸️ Kubernetes Deployment

Kubernetes manifests are provided in the `k8s/` folder for deploying:
- Streamlit application
- MySQL database
- Kubernetes Secret
- Services for internal and external access

To deploy on a local Kubernetes cluster:

```bash
kubectl apply -f k8s/
```

To verify resources:

```bash
kubectl get pods
kubectl get services
kubectl get deployments
```

The application can be accessed through NodePort after deployment:

```text
http://localhost:30085
```

---

## 📊 Example Use Cases

- Create a marketing plan for a fitness app
- Growth plan for a personal brand
- Marketing strategy for a new e-commerce business
- Campaign planning for a local business

---

## 🎯 Learning Outcomes

This project demonstrates practical experience in:
- Agentic AI workflow design
- Streamlit application development
- MySQL database integration
- Docker containerization
- Docker Compose orchestration
- GitHub Actions CI setup
- Environment variable management
- Persistent storage with Docker volumes
- DevOps-oriented deployment workflow

---

## 👨‍💻 Author

**Krishna Pawar**