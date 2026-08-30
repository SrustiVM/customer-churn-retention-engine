def calculate_business_value(
    tp: int,
    fp: int,
    campaign_cost: float,
    retention_cost: float,
    success_rate: float,
    revenue_at_risk: float
) -> dict:
    """
    Calculate the business value of a retention campaign.
    """

    customers_targeted = tp + fp

    campaign_expense = customers_targeted * campaign_cost

    retention_expense = tp * retention_cost

    revenue_protected = (
        tp
        * success_rate
        * revenue_at_risk
    )

    net_benefit = (
        revenue_protected
        - campaign_expense
        - retention_expense
    )

    total_cost = campaign_expense + retention_expense

    roi_percent = (
        (net_benefit / total_cost) * 100
        if total_cost > 0
        else 0
    )

    return {
        "customers_targeted": customers_targeted,
        "campaign_expense": campaign_expense,
        "retention_expense": retention_expense,
        "revenue_protected": revenue_protected,
        "net_benefit": net_benefit,
        "roi_percent": roi_percent
    }