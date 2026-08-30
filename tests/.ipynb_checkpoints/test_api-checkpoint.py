from fastapi.testclient import TestClient

from api.app import app


client = TestClient(app)


VALID_CUSTOMER = {
    "customerID": "TEST001",
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 80.0,
    "TotalCharges": 960.0
}


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Customer Churn API is running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction():
    response = client.post("/predict", json=VALID_CUSTOMER)

    assert response.status_code == 200

    result = response.json()

    assert "churn_probability" in result
    assert "risk_level" in result
    assert "recommended_action" in result
    assert "business_priority" in result

    assert 0 <= result["churn_probability"] <= 1


def test_invalid_tenure():
    customer = VALID_CUSTOMER.copy()
    customer["tenure"] = -5

    response = client.post("/predict", json=customer)

    assert response.status_code == 422