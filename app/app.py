from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from app.financials import METRICS, annual_observations
from app.indicators import build_indicators
from app.sec_data import APPLE_CIK, COMPANY_FACTS_URL, fetch_sec_json, latest_company_facts, save_company_facts

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "teste1.sqlite3"

st.set_page_config(page_title="TESTE 1 | Apple Financial History", layout="wide")
st.title("TESTE 1 — Pesquisa Fundamentalista")
st.caption("Aplicação local · Piloto Apple Inc. · Dados oficiais SEC EDGAR")

with st.sidebar:
    st.subheader("Empresa-piloto")
    st.write("**Apple Inc.**")
    st.code(f"CIK: {APPLE_CIK}")
    st.caption("A base de dados e os documentos ficam neste computador.")
    st.divider()
    user_agent = st.text_input(
        "Contacto para a SEC (User-Agent)",
        value=os.getenv("SEC_USER_AGENT", ""),
        help="Indique nome e email de contacto. Exemplo: Nome contacto@dominio.pt",
    )
    refresh = st.button("Atualizar dados oficiais", type="primary", use_container_width=True)
    if DB_PATH.exists():
        st.download_button(
            "Descarregar backup da base de dados",
            data=DB_PATH.read_bytes(),
            file_name="teste1_backup.sqlite3",
            mime="application/vnd.sqlite3",
            use_container_width=True,
        )


if refresh:
    try:
        with st.spinner("A obter Company Facts diretamente da SEC..."):
            payload_new = fetch_sec_json(COMPANY_FACTS_URL, user_agent)
            collected_at = save_company_facts(payload_new, DB_PATH)
        st.success(f"Payload original guardado localmente. Recolha: {collected_at}")
    except Exception as exc:
        st.error(f"Atualização falhou: {exc}")

payload = latest_company_facts(DB_PATH)
if payload is None:
    st.info("Ainda não há dados locais. Configure o contacto SEC na barra lateral e atualize os dados.")
    st.markdown(f"**Fonte oficial:** [SEC Company Facts — Apple]({COMPANY_FACTS_URL})")
else:
    tags = payload.get("facts", {}).get("us-gaap", {})
    c1, c2, c3 = st.columns(3)
    c1.metric("Empresa", payload.get("entityName", "Apple Inc."))
    c2.metric("Tags US-GAAP", f"{len(tags):,}")
    c3.metric("CIK", APPLE_CIK)

    tab_table, tab_chart, tab_indicators, tab_dictionary = st.tabs(["Lista financeira", "Gráficos", "Indicadores", "Dicionário de dados"])

    with tab_table:
        st.subheader("Histórico anual — demonstrações selecionadas")
        selected = st.multiselect("Métricas", list(METRICS.keys()), default=["Receita", "Resultado operacional", "Resultado líquido", "Ativos", "Capital próprio"])
        records = []
        for metric in selected:
            for item in annual_observations(payload, metric):
                records.append({"Métrica": metric, "Período": item["periodo"], "Ano fiscal": item["ano_fiscal"], "Valor": item["valor"], "Unidade": item["unidade"], "Submetido": item["submetido"], "Tag": item["tag"]})
        if records:
            frame = pd.DataFrame(records).sort_values(["Métrica", "Período"], ascending=[True, False])
            frame["Valor (milhões USD)"] = frame.apply(lambda row: row["Valor"] / 1_000_000 if row["Unidade"] == "USD" else row["Valor"], axis=1)
            st.dataframe(frame[["Métrica", "Período", "Ano fiscal", "Valor (milhões USD)", "Unidade", "Submetido", "Tag"]], use_container_width=True, hide_index=True)
            st.download_button("Exportar tabela CSV", frame.to_csv(index=False).encode("utf-8-sig"), "apple_financial_history.csv", "text/csv")
        else:
            st.warning("Não foram encontradas observações anuais para as métricas selecionadas. Não são fabricados valores em falta.")

    with tab_chart:
        st.subheader("Evolução histórica")
        metric = st.selectbox("Métrica a representar", list(METRICS.keys()), index=0)
        chart_rows = annual_observations(payload, metric)
        if chart_rows:
            chart = pd.DataFrame(chart_rows)
            chart["valor_milhoes"] = chart["valor"] / 1_000_000 if chart_rows[0]["unidade"] == "USD" else chart["valor"]
            fig = px.line(chart.sort_values("periodo"), x="periodo", y="valor_milhoes", markers=True, title=f"{metric} — milhões de {chart_rows[0]['unidade']}")
            st.plotly_chart(fig, use_container_width=True)
            st.caption("A série usa observações anuais 10-K identificadas pela SEC. Confirme alterações de perímetro, classificação e reapresentações antes de comparar.")
        else:
            st.info("Sem observações anuais compatíveis para esta métrica.")

    with tab_indicators:
        st.subheader("Indicadores derivados")
        indicator_rows = build_indicators(payload)
        if indicator_rows:
            indicator_frame = pd.DataFrame(indicator_rows)
            st.dataframe(indicator_frame, use_container_width=True, hide_index=True)
            st.download_button("Exportar indicadores CSV", indicator_frame.to_csv(index=False).encode("utf-8-sig"), "apple_indicators.csv", "text/csv")
        else:
            st.info("Não existem dados suficientes para calcular indicadores.")

    with tab_dictionary:
        st.subheader("Tags contabilísticas disponíveis")
        query = st.text_input("Pesquisar tag US-GAAP", placeholder="Ex.: Revenue, Assets, NetIncome")
        matches = sorted(tag for tag in tags if query.lower() in tag.lower())
        st.dataframe(pd.DataFrame({"Tag SEC (US-GAAP)": matches}), use_container_width=True, hide_index=True, height=300)

    st.divider()
    st.subheader("Proveniência e limitações")
    st.write(f"Fonte original: {COMPANY_FACTS_URL}")
    st.write("O JSON original da SEC é guardado sem alteração na base SQLite local, com data de recolha.")
    st.warning("A normalização inicial usa apenas tags US-GAAP selecionadas e observações 10-K anuais. Pode haver diferenças de classificação, reapresentações ou métricas sem tag equivalente. Esta versão não é ainda uma análise de investimento validada.")

st.divider()
st.caption("TESTE 1 · Acesso local em 127.0.0.1 · Sem envio dos dados locais para cloud.")
