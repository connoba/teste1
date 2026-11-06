from app.indicators import build_indicators


def test_build_indicators_uses_matching_periods_and_calculates_growth():
    def annual(tag, vals):
        return {"units": {"USD": [
            {"form": "10-K", "fy": year, "start": f"{year-1}-10-01", "end": end,
             "val": value, "filed": f"{year+1}-01-01"}
            for year, end, value in vals
        ]}}
    payload = {"facts": {"us-gaap": {
        "RevenueFromContractWithCustomerExcludingAssessedTax": annual("Revenue", [(2023, "2023-09-30", 100), (2024, "2024-09-28", 120)]),
        "OperatingIncomeLoss": annual("Operating", [(2023, "2023-09-30", 20), (2024, "2024-09-28", 30)]),
        "NetIncomeLoss": annual("NetIncome", [(2023, "2023-09-30", 10), (2024, "2024-09-28", 18)]),
        "NetCashProvidedByUsedInOperatingActivities": annual("CFO", [(2023, "2023-09-30", 25), (2024, "2024-09-28", 35)]),
        "PaymentsToAcquirePropertyPlantAndEquipment": annual("CapEx", [(2023, "2023-09-30", 5), (2024, "2024-09-28", 7)]),
        "Assets": {"units": {"USD": [{"form": "10-K", "fy": 2023, "end": "2023-09-30", "val": 200}, {"form": "10-K", "fy": 2024, "end": "2024-09-28", "val": 240}]}},
        "Liabilities": {"units": {"USD": [{"form": "10-K", "fy": 2023, "end": "2023-09-30", "val": 100}, {"form": "10-K", "fy": 2024, "end": "2024-09-28", "val": 120}]}},
        "StockholdersEquity": {"units": {"USD": [{"form": "10-K", "fy": 2023, "end": "2023-09-30", "val": 100}, {"form": "10-K", "fy": 2024, "end": "2024-09-28", "val": 120}]}},
    }}}
    rows = build_indicators(payload)
    assert len(rows) == 2
    assert abs(rows[1]["Crescimento da receita (%)"] - 20) < 1e-9
    assert abs(rows[1]["Margem operacional (%)"] - 25) < 1e-9
    assert abs(rows[1]["Fluxo de caixa livre (USD)"] - 28) < 1e-9
    assert rows[1]["ROE aproximado (%)"] == 16.363636363636363


def test_missing_inputs_do_not_create_fabricated_ratios():
    payload = {"facts": {"us-gaap": {"Assets": {"units": {"USD": [
        {"form": "10-K", "fy": 2024, "end": "2024-09-28", "val": 10}
    ]}}}}}
    assert build_indicators(payload) == [{"Período": "2024-09-28"}]


def test_annual_growth_and_roe_are_not_calculated_across_missing_years():
    revenue = {"units": {"USD": [
        {"form": "10-K", "fy": 2021, "start": "2020-10-01", "end": "2021-09-30", "val": 100},
        {"form": "10-K", "fy": 2024, "start": "2023-10-01", "end": "2024-09-28", "val": 160},
    ]}}
    net_income = {"units": {"USD": [
        {"form": "10-K", "fy": 2021, "start": "2020-10-01", "end": "2021-09-30", "val": 10},
        {"form": "10-K", "fy": 2024, "start": "2023-10-01", "end": "2024-09-28", "val": 20},
    ]}}
    equity = {"units": {"USD": [
        {"form": "10-K", "fy": 2021, "end": "2021-09-30", "val": 100},
        {"form": "10-K", "fy": 2024, "end": "2024-09-28", "val": 150},
    ]}}
    payload = {"facts": {"us-gaap": {
        "RevenueFromContractWithCustomerExcludingAssessedTax": revenue,
        "NetIncomeLoss": net_income,
        "StockholdersEquity": equity,
    }}}
    rows = build_indicators(payload)
    assert "Crescimento da receita (%)" not in rows[-1]
    assert "ROE aproximado (%)" not in rows[-1]
