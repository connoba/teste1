"""Conversão conservadora de tags SEC XBRL em observações anuais."""
from __future__ import annotations

from datetime import date
from typing import Any

# Tags específicas/padrão usadas no piloto Apple. A unidade é sempre validada.
METRICS = {
    "Receita": ("RevenueFromContractWithCustomerExcludingAssessedTax", "duration", "USD"),
    "Resultado operacional": ("OperatingIncomeLoss", "duration", "USD"),
    "Resultado líquido": ("NetIncomeLoss", "duration", "USD"),
    "Fluxo de caixa operacional": ("NetCashProvidedByUsedInOperatingActivities", "duration", "USD"),
    "Investimento em ativos (CapEx)": ("PaymentsToAcquirePropertyPlantAndEquipment", "duration", "USD"),
    "Ativos": ("Assets", "instant", "USD"),
    "Passivos": ("Liabilities", "instant", "USD"),
    "Capital próprio": ("StockholdersEquity", "instant", "USD"),
    "Caixa e equivalentes": ("CashAndCashEquivalentsAtCarryingValue", "instant", "USD"),
}


def annual_observations(payload: dict[str, Any], metric_name: str) -> list[dict[str, Any]]:
    """Extrai observações 10-K anuais; não agrega trimestres nem mistura unidades."""
    if metric_name not in METRICS:
        raise ValueError(f"Métrica não suportada: {metric_name}")
    tag, kind, unit = METRICS[metric_name]
    concept = payload.get("facts", {}).get("us-gaap", {}).get(tag)
    if not concept:
        return []
    observations = []
    for unit_name, rows in concept.get("units", {}).items():
        if unit_name != unit:
            continue
        for row in rows:
            if row.get("form") != "10-K" or not row.get("end"):
                continue
            if kind == "duration":
                if not row.get("start"):
                    continue
                try:
                    days = (date.fromisoformat(row["end"]) - date.fromisoformat(row["start"])).days
                except (TypeError, ValueError):
                    continue
                if not 330 <= days <= 380:
                    continue
            elif row.get("start"):
                continue
            observations.append({
                "periodo": row["end"],
                "ano_fiscal": row.get("fy"),
                "valor": row.get("val"),
                "unidade": unit_name,
                "ficheiro": row.get("accn"),
                "submetido": row.get("filed"),
                "formulario": row.get("form"),
                "tag": tag,
            })
    # Se a SEC reportar mais do que uma versão para o mesmo período,
    # manter a submissão mais recente, preservando a data e accession.
    chosen: dict[tuple[Any, str], dict[str, Any]] = {}
    for item in sorted(observations, key=lambda x: x.get("submetido") or ""):
        chosen[(item["ano_fiscal"], item["periodo"])] = item
    return sorted(chosen.values(), key=lambda x: x["periodo"])


def metric_label(metric_name: str) -> str:
    return METRICS[metric_name][0]
