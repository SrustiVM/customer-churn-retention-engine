from src.business.roi import calculate_business_value


def test_business_value():
    result = calculate_business_value(
        tp=100,
        fp=50,
        campaign_cost=50,
        retention_cost=200,
        success_rate=0.30,
        revenue_at_risk=2000
    )

    assert result["customers_targeted"] == 150
    assert result["campaign_expense"] == 7500
    assert result["retention_expense"] == 20000
    assert result["revenue_protected"] == 60000
   