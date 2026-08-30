from src.validation.input_validator import validate_input
import joblib


class ChurnPredictor:

    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)

    def predict(self, customer_data, threshold: float):

        validate_input(customer_data)

        probability = self.model.predict_proba(
            customer_data
        )[:, 1][0]

        if probability >= threshold:
            risk_level = "High"
            recommended_action = "Retention intervention"
            business_priority = "High"

        elif probability >= 0.3:
            risk_level = "Medium"
            recommended_action = "Targeted retention offer"
            business_priority = "Medium"

        else:
            risk_level = "Low"
            recommended_action = "Normal engagement"
            business_priority = "Low"

        return {
            "churn_probability": float(probability),
            "risk_level": risk_level,
            "recommended_action": recommended_action,
            "business_priority": business_priority
        }