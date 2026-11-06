"""Relatório fundamentalista Markdown reproduzível para o piloto Apple."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from app.indicators import build_indicators
from app.financials import METRICS, annual_observations
from app.sec_data import COMPANY_FACTS_URL, SUBMISSIONS_URL


def build_markdown_report(payload: dict[str, Any], submissions: dict[str, Any] | None = None) -> str:
    entity = payload.get("entityName", "Empresa sem nome")
    lines = [
        f"# Relatório financeiro — {entity}",
        "",
        f"- Gerado em: {datetime.now(timezone.utc).isoformat()}",
        "- Âmbito: observações anuais 10-K disponíveis no payload SEC guardado localmente",
        "- Moeda de apresentação: USD, salvo indicação diferente",
        "",
        "## Séries financeiras",
        "",
        "| Métrica | Período | Valor | Unidade | Tag | Submetido |",
        "|---|---:|---:|---|---|---|",
    ]
    for metric in METRICS:
        for item in annual_observations(payload, metric):
            lines.append(
                f"| {metric} | {item['periodo']} | {item['valor']} | {item['unidade']} | "
                f"{item['tag']} | {item.get('submetido') or '—'} |"
            )
    lines.extend(["", "## Indicadores derivados", ""])
    indicators = build_indicators(payload)
    if indicators:
        headers = list(dict.fromkeys(key for row in indicators for key in row))
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
        for row in indicators:
            lines.append("| " + " | ".join(str(row.get(key, "—")) for key in headers) + " |")
    else:
        lines.append("Não existem dados suficientes para calcular indicadores.")
    lines.extend([
        "",
        "## Filings recentes",
        "",
    ])
    if submissions:
        recent = submissions.get("filings", {}).get("recent", {})
        forms = recent.get("form", [])
        dates = recent.get("filingDate", [])
        reports = recent.get("reportDate", [])
        for index, form in enumerate(forms):
            if form in {"10-K", "10-Q", "8-K"}:
                filed = dates[index] if index < len(dates) else "—"
                report_date = reports[index] if index < len(reports) else "—"
                lines.append(f"- {form}: submetido em {filed}; período reportado {report_date}")
                if sum(1 for line in lines if line.startswith("- 10-") or line.startswith("- 8-K")) >= 20:
                    break
    else:
        lines.append("Submissions SEC ainda não disponíveis na base local.")
    lines.extend([
        "",
        "## Fontes",
        f"- SEC Company Facts: {COMPANY_FACTS_URL}",
        f"- SEC Submissions: {SUBMISSIONS_URL}",
        "- Documentos originais: https://www.sec.gov/edgar/browse/?CIK=320193&owner=exclude",
        "",
        "## Limitações",
        "- Os valores dependem das tags US-GAAP selecionadas e podem não cobrir extensões específicas da empresa.",
        "- As séries ainda requerem reconciliação com os relatórios anuais originais e revisão de reapresentações.",
        "- Fluxo de caixa livre e ROE são aproximações com as fórmulas documentadas no projeto.",
        "- Este relatório não constitui recomendação nem aconselhamento de investimento.",
    ])
    return "\n".join(lines)
