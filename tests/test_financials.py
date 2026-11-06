from app.financials import annual_observations


def test_annual_observations_excludes_quarterly_and_wrong_unit():
    payload = {"facts": {"us-gaap": {"Revenues": {"units": {
        "USD": [
            {"form": "10-K", "fy": 2024, "start": "2023-10-01", "end": "2024-09-28", "val": 100, "filed": "2024-11-01"},
            {"form": "10-Q", "fy": 2024, "start": "2024-01-01", "end": "2024-03-30", "val": 20, "filed": "2024-05-01"},
        ],
        "EUR": [
            {"form": "10-K", "fy": 2024, "start": "2023-10-01", "end": "2024-09-28", "val": 90, "filed": "2024-11-01"}
        ]
    }}}}}
    rows = annual_observations(payload, "Receita")
    assert len(rows) == 1
    assert rows[0]["valor"] == 100
    assert rows[0]["unidade"] == "USD"


def test_instant_metric_requires_no_start_date():
    payload = {"facts": {"us-gaap": {"Assets": {"units": {"USD": [
        {"form": "10-K", "fy": 2024, "end": "2024-09-28", "val": 300},
        {"form": "10-K", "fy": 2023, "start": "2023-01-01", "end": "2023-09-30", "val": 200},
    ]}}}}}
    rows = annual_observations(payload, "Ativos")
    assert len(rows) == 1
    assert rows[0]["valor"] == 300


def test_unknown_metric_fails_explicitly():
    import pytest
    with pytest.raises(ValueError):
        annual_observations({}, "Métrica inventada")
