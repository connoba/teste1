from app.sec_data import latest_submissions, recent_filings, save_submissions


def test_recent_filings_builds_sec_archive_url_and_filters_forms():
    payload = {"filings": {"recent": {
        "form": ["10-K", "10-Q", "S-8"],
        "filingDate": ["2025-11-01", "2025-02-01", "2025-01-01"],
        "reportDate": ["2025-09-27", "2024-12-28", "2025-01-01"],
        "accessionNumber": ["0000320193-25-000001", "0000320193-25-000002", "0000320193-25-000003"],
        "primaryDocument": ["aapl-20250927.htm", "aapl-20241228.htm", "s8.htm"],
    }}}
    rows = recent_filings(payload)
    assert len(rows) == 2
    assert rows[0]["form"] == "10-K"
    assert rows[0]["url"].endswith("/000032019325000001/aapl-20250927.htm")


def test_submissions_are_saved_and_read_from_sqlite(tmp_path):
    path = tmp_path / "sec.sqlite3"
    payload = {"filings": {"recent": {"form": ["10-K"]}}}
    save_submissions(payload, path)
    assert latest_submissions(path) == payload


def test_missing_submissions_table_returns_none(tmp_path):
    from app.sec_data import save_company_facts
    path = tmp_path / "legacy.sqlite3"
    save_company_facts({"facts": {}}, path)
    assert latest_submissions(path) is None
