from app.sec_data import latest_company_facts, list_fact_names, save_company_facts


def test_list_fact_names_returns_sorted_unique_names():
    payload = {
        "facts": {
            "us-gaap": {"Assets": {}, "Revenues": {}},
            "dei": {"EntityCommonStockSharesOutstanding": {}},
        }
    }
    assert list_fact_names(payload) == [
        "Assets", "EntityCommonStockSharesOutstanding", "Revenues"
    ]


def test_save_and_read_company_facts(tmp_path):
    db_path = tmp_path / "local" / "test.sqlite3"
    payload = {"entityName": "Apple Inc.", "facts": {"us-gaap": {"Assets": {}}}}
    collected_at = save_company_facts(payload, db_path)
    assert collected_at
    assert latest_company_facts(db_path) == payload


def test_latest_returns_none_without_database(tmp_path):
    assert latest_company_facts(tmp_path / "missing.sqlite3") is None
