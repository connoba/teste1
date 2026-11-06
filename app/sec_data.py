"""Acesso mínimo à SEC EDGAR e persistência local do ficheiro Company Facts."""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

APPLE_CIK = "0000320193"
COMPANY_FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json"


def fetch_sec_json(url: str, user_agent: str, timeout: int = 30) -> dict[str, Any]:
    """Obtém JSON público da SEC com User-Agent identificável."""
    if not user_agent or "@" not in user_agent:
        raise ValueError("Configure um User-Agent com contacto (ex.: Nome email@dominio.pt).")
    response = requests.get(
        url,
        headers={"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate"},
        timeout=timeout,
    )
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict):
        raise ValueError("A resposta da SEC não contém um objeto JSON.")
    return payload


def save_company_facts(payload: dict[str, Any], db_path: str | Path) -> str:
    """Guarda a resposta original e a data de recolha em SQLite."""
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    collected_at = datetime.now(timezone.utc).isoformat()
    with sqlite3.connect(path) as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS sec_companyfacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cik TEXT NOT NULL,
                source_url TEXT NOT NULL,
                collected_at TEXT NOT NULL,
                payload_json TEXT NOT NULL
            )"""
        )
        connection.execute(
            """INSERT INTO sec_companyfacts
               (cik, source_url, collected_at, payload_json)
               VALUES (?, ?, ?, ?)""",
            (APPLE_CIK, COMPANY_FACTS_URL, collected_at,
             json.dumps(payload, ensure_ascii=False)),
        )
    return collected_at


def latest_company_facts(db_path: str | Path) -> dict[str, Any] | None:
    """Devolve a última resposta SEC guardada, sem alterar o original."""
    path = Path(db_path)
    if not path.exists():
        return None
    with sqlite3.connect(path) as connection:
        row = connection.execute(
            "SELECT payload_json FROM sec_companyfacts ORDER BY id DESC LIMIT 1"
        ).fetchone()
    return json.loads(row[0]) if row else None


def list_fact_names(payload: dict[str, Any]) -> list[str]:
    """Lista tags XBRL disponíveis, sem assumir equivalência contabilística."""
    names: list[str] = []
    for namespace in payload.get("facts", {}).values():
        if isinstance(namespace, dict):
            names.extend(namespace.keys())
    return sorted(set(names))
