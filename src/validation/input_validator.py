import pandas as pd


REQUIRED_COLUMNS = {
    "customerID",
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges"
}


ALLOWED_VALUES = {
    "gender": {"Male", "Female"},
    "SeniorCitizen": {0, 1},
    "Partner": {"Yes", "No"},
    "Dependents": {"Yes", "No"},
    "PhoneService": {"Yes", "No"},
    "MultipleLines": {"Yes", "No", "No phone service"},
    "InternetService": {"DSL", "Fiber optic", "No"},
    "OnlineSecurity": {"Yes", "No", "No internet service"},
    "OnlineBackup": {"Yes", "No", "No internet service"},
    "DeviceProtection": {"Yes", "No", "No internet service"},
    "TechSupport": {"Yes", "No", "No internet service"},
    "StreamingTV": {"Yes", "No", "No internet service"},
    "StreamingMovies": {"Yes", "No", "No internet service"},
    "Contract": {
        "Month-to-month",
        "One year",
        "Two year"
    },
    "PaperlessBilling": {"Yes", "No"},
    "PaymentMethod": {
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    }
}


def validate_input(customer_data: pd.DataFrame) -> None:
    """Validate one customer before prediction."""

    # 1. Check empty input
    if customer_data.empty:
        raise ValueError("Customer input cannot be empty.")

    # 2. Check exactly one customer
    if len(customer_data) != 1:
        raise ValueError("Expected exactly one customer.")

    # 3. Check required columns
    missing_columns = REQUIRED_COLUMNS - set(customer_data.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # 4. Check numeric columns
    numeric_columns = [
        "SeniorCitizen",
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    for column in numeric_columns:
     print(column, customer_data[column].dtype)

     if not pd.api.types.is_numeric_dtype(customer_data[column]):
        raise ValueError(
            f"{column} must be numeric."
        )

    # 5. Check missing values
    if customer_data[list(REQUIRED_COLUMNS)].isna().any().any():
        raise ValueError(
            "Customer input contains missing values."
        )

    # 6. Check allowed categorical values
    for column, allowed in ALLOWED_VALUES.items():

        invalid_values = (
            set(customer_data[column].unique()) - allowed
        )

        if invalid_values:
            raise ValueError(
                f"Invalid values in {column}: {invalid_values}"
            )

    # 7. Check numerical ranges
    if (customer_data["tenure"] < 0).any():
        raise ValueError("Tenure cannot be negative.")

    if (customer_data["MonthlyCharges"] < 0).any():
        raise ValueError("MonthlyCharges cannot be negative.")

    if (customer_data["TotalCharges"] < 0).any():
        raise ValueError("TotalCharges cannot be negative.")