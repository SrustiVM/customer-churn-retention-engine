from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
from pathlib import Path
import logging

from src.prediction.predictor import ChurnPredictor
from src.config import load_config


# --------------------------------------------------
# Logging
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# FastAPI application
# --------------------------------------------------

app = FastAPI(title="Customer Churn Prediction API")


# --------------------------------------------------
# Project paths and model
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

config = load_config()

model_path = BASE_DIR / "models" / "churn_model.joblib"

predictor = ChurnPredictor(str(model_path))

logger.info("Churn prediction model loaded successfully.")


# --------------------------------------------------
# Input schema
# --------------------------------------------------

class CustomerInput(BaseModel):
    customerID: str
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int = Field(ge=0)
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float = Field(ge=0)
    TotalCharges: float = Field(ge=0)


# --------------------------------------------------
# Output schema
# --------------------------------------------------

class PredictionResponse(BaseModel):
    churn_probability: float
    risk_level: str
    recommended_action: str
    business_priority: str


# --------------------------------------------------
# Endpoints
# --------------------------------------------------

@app.get("/")
def home():

    logger.info("Root endpoint accessed.")

    return {
        "message": "Customer Churn API is running"
    }


@app.get("/health")
def health():

    logger.info("Health check requested.")

    return {
        "status": "healthy"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict_customer(customer: CustomerInput):

    logger.info(
        "Prediction request received for customer: %s",
        customer.customerID
    )

    try:

        customer_df = pd.DataFrame([customer.model_dump()])

        result = predictor.predict(
            customer_df,
            threshold=config["business"]["threshold"]
        )

        logger.info(
            "Prediction completed for customer: %s | Risk: %s",
            customer.customerID,
            result["risk_level"]
        )

        return result

    except ValueError as e:

        logger.warning(
            "Validation error for customer %s: %s",
            customer.customerID,
            str(e)
        )

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        logger.exception(
            "Unexpected prediction error for customer %s",
            customer.customerID
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )