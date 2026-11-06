"""Indicadores derivados; só calcula quando os inputs comparáveis existem."""
from __future__ import annotations

from typing import Any

from financials import annual_observations


def build_indicators(payload: dict[str, Any]) -> list[dict[str, Any]]:
    metrics = ["Receita", "Resultado operacional", "Resultado líquido",
               "Fluxo de caixa operacional", "Investimento em ativos (CapEx)",
               "Ativos", "Passivos", "Capital próprio"]
    by_period: dict[str, dict[str, float]] = {}
    for metric in metrics:
        for row in annual_observations(payload, metric):
            if row.get("valor") is None:
                continue
            by_period.setdefault(row["periodo"], {})[metric] = float(row["valor"])

    periods = sorted(by_period)
    output = []
    previous = None
    for period in periods:
        values = by_period[period]
        revenue = values.get("Receita")
        operating_income = values.get("Resultado operacional")
        net_income = values.get("Resultado líquido")
        cfo = values.get("Fluxo de caixa operacional")
        capex = values.get("Investimento em ativos (CapEx)")
        equity = values.get("Capital próprio")
        assets = values.get("Ativos")
        liabilities = values.get("Passivos")

        row: dict[str, Any] = {"Período": period}
        if revenue not in (None, 0):
            row["Margem operacional (%)"] = operating_income / revenue * 100 if operating_income is not None else None
            row["Margem líquida (%)"] = net_income / revenue * 100 if net_income is not None else None
            if previous and previous.get("Receita") not in (None, 0):
                row["Crescimento da receita (%)"] = (revenue / previous["Receita"] - 1) * 100
        if cfo is not None and capex is not None:
            row["Fluxo de caixa livre (USD)"] = cfo - abs(capex)
        if liabilities is not None and equity not in (None, 0):
            row["Passivos / capital próprio (x)"] = liabilities / equity
        if assets is not None and liabilities is not None:
            row["Ativos - passivos (USD)"] = assets - liabilities
        if net_income is not None and equity is not None and previous and previous.get("Capital próprio") is not None:
            average_equity = (equity + previous["Capital próprio"]) / 2
            if average_equity:
                row["ROE aproximado (%)"] = net_income / average_equity * 100
        output.append(row)
        previous = values
    return output
