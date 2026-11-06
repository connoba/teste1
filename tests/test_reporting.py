from app.reporting import build_markdown_report


def test_report_contains_source_methodology_and_financial_data():
    payload = {"entityName": "Apple Inc.", "facts": {"us-gaap": {
        "Assets": {"units": {"USD": [{"form": "10-K", "fy": 2024, "end": "2024-09-28", "val": 1000}]}}
    }}}
    report = build_markdown_report(payload)
    assert "# Relatório financeiro — Apple Inc." in report
    assert "SEC Company Facts" in report
    assert "Ativos" in report
    assert "reconciliação" in report.lower()
