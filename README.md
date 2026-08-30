# Customer Churn & Retention Engine

An end-to-end production-oriented machine learning system for predicting customer churn and converting ML predictions into actionable customer-retention decisions.

The project goes beyond model training by implementing data analysis, preprocessing, model evaluation, business-oriented threshold optimization, ROI analysis, explainability, API serving, Docker containerization, automated testing, and CI/CD.

---

## 🎯 Project Objective

Customer churn prediction is useful only when predictions can support business decisions.

This project answers two questions:

1. Which customers are likely to churn?
2. Which customers should the business prioritize for retention?

The system combines:

Customer Data → Data Processing → ML Prediction → Churn Probability → Risk Level → Retention Decision → Business Value

---

## 📊 Dataset

The project uses the IBM Telco Customer Churn dataset.

The dataset contains customer information including:

- Demographics
- Tenure
- Contract type
- Internet services
- Payment method
- Monthly charges
- Total charges
- Customer churn

Target variable:

`Churn`

---

## 🔍 Machine Learning Workflow

The project follows an end-to-end machine learning workflow:

1. Data loading
2. Data quality checks
3. Exploratory Data Analysis
4. Missing-value handling
5. Duplicate and unusual-value detection
6. Feature analysis
7. Feature engineering
8. Categorical encoding
9. Numerical preprocessing
10. Train/test splitting
11. Model training
12. Model comparison
13. Cross-validation
14. Hyperparameter optimization
15. Imbalanced-class handling
16. Evaluation using multiple metrics
17. Probability threshold analysis
18. Business ROI analysis
19. Model explainability
20. Prediction pipeline
21. API development
22. Unit and API testing
23. Docker containerization
24. CI/CD with GitHub Actions

---

## 🤖 Model Evaluation

Multiple classification approaches were evaluated rather than relying only on accuracy.

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- PR-AUC
- Confusion Matrix

Because churn prediction is a business problem, particular attention is given to:

- Recall
- Precision
- PR-AUC
- False positives and false negatives
- Business impact

---

## 💰 Business & ROI Analysis

A major component of the project is converting model predictions into business decisions.

Different probability thresholds are evaluated to understand the trade-off between:

- True Positives
- False Positives
- True Negatives
- False Negatives
- Customers targeted
- Retention cost
- Revenue at risk
- Revenue protected
- Campaign cost
- Net benefit
- ROI

Instead of blindly using the default `0.5` classification threshold, the system evaluates thresholds according to the business objective.

This allows the business to choose a threshold based on the cost of contacting customers and the potential revenue protected by successful retention.

---

## 🧠 Model Explainability

SHAP-based explainability is used to understand model predictions.

The analysis provides:

- Global feature importance
- Direction of feature influence
- Individual customer prediction explanations
- Features increasing or decreasing churn risk

This makes the model more transparent and useful for business stakeholders.

---

## 🚀 Prediction API

The trained ML pipeline is exposed through a FastAPI application.

### Health Check

```text
GET /health

Used to verify that the API service is running correctly.

Prediction

POST /predict

Accepts customer information and returns a churn prediction and probability.

Example response:

{
  "churn_prediction": 1,
  "churn_probability": 0.73,
  "risk_level": "High"
}

Interactive API documentation is available through FastAPI's Swagger UI:

http://localhost:8000/docs


---

🐳 Docker

The API is containerized using Docker.

The Docker setup provides a reproducible environment containing:

Python

Required dependencies

ML model

Prediction code

FastAPI application


Run the application using Docker:

docker build -t churn-api .

docker run -p 8000:8000 churn-api

The API can then be accessed at:

http://localhost:8000

Swagger documentation:

http://localhost:8000/docs

Health check:

http://localhost:8000/health


---

🧪 Testing

The project includes automated tests for:

Business ROI calculations

Prediction functionality

API endpoints


Tests are written using pytest.

Run the test suite:

pytest

The API tests use FastAPI's TestClient.


---

⚙️ CI/CD

GitHub Actions is used to automatically execute the test suite when changes are pushed to the repository.

The CI pipeline:

1. Checks out the repository


2. Sets up Python


3. Installs dependencies


4. Runs automated tests


5. Reports the result through GitHub Actions



This helps prevent broken code from being merged or deployed.


---

📁 Project Structure

customer-churn-retention-engine/
│
├── api/
│   ├── app.py
│   └── __init__.py
│
├── configs/
│   └── config.yaml
│
├── Data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   └── churn_model.joblib
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── customer_churn_retention_engine.ipynb
│   ├── modeldevelopment.ipynb
│   └── models.ipynb
│
├── src/
│   ├── business/
│   │   └── roi.py
│   │
│   ├── prediction/
│   │   └── predictor.py
│   │
│   ├── validation/
│   │   └── input_validator.py
│   │
│   └── config.py
│
├── tests/
│   ├── test_api.py
│   ├── test_predictor.py
│   └── test_roi.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md


---

🛠️ Technology Stack

Machine Learning

Python

NumPy

Pandas

Scikit-learn

CatBoost

SHAP


Data Analysis

Matplotlib

Seaborn

Jupyter Notebook


Backend

FastAPI

Uvicorn


Testing

Pytest


Deployment & MLOps

Docker

Git

GitHub

GitHub Actions



---

📌 Key Engineering Concepts Demonstrated

This project demonstrates practical knowledge of:

End-to-end ML workflows

Data preprocessing

Feature engineering

Categorical encoding

Imbalanced classification

Model comparison

Cross-validation

Hyperparameter tuning

Classification threshold optimization

Business-oriented ML

ROI-driven decision making

Model explainability

Modular Python code

Input validation

Unit testing

API development

Containerization

CI/CD automation



---

💡 Business Impact

The system is designed to move beyond:

> "Will this customer churn?"



towards:

> "Which customers should we target for retention to maximize business value?"



By combining churn probability with threshold optimization and ROI analysis, the model can support practical customer-retention campaigns.


---

🔮 Future Improvements

Potential future extensions include:

MLflow experiment tracking

Model versioning

Automated model retraining

Data drift monitoring

Model performance monitoring

Cloud deployment

Database integration

Customer-retention dashboard

Automated batch prediction

Production model registry



---

👩‍💻 Author

Srusti VM

Computer Science Engineering


---

⭐ Project Highlights

This project demonstrates the complete journey from:

Raw Customer Data

→ EDA

→ Feature Engineering

→ ML Modeling

→ Model Evaluation

→ Threshold Optimization

→ ROI Analysis

→ Explainability

→ Prediction Pipeline

→ FastAPI

→ Docker

→ Automated Testing

→ GitHub Actions CI/CD


---

📄 License

This project is intended for educational and portfolio purposes.