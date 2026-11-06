from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
import streamlit as st

from sec_data import APPLE_CIK, COMPANY_FACTS_URL, fetch_sec_json, latest_company_facts, save_company_facts

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "teste1.sqlite3"

st.set_page_config(page_title="TESTE 1 | Apple Financial History", layout="wide")
st.title("TESTE 1 — Pesquisa Fundamentalista")
st.caption("Protótipo local · Piloto Apple Inc. · Dados oficiais SEC EDGAR")

with st.sidebar:
    st.subheader("Empresa-piloto")
    st.write("**Apple Inc.**")
    st.code(f"CIK: {APPLE_CIK}")
    st.caption("Os dados recolhidos ficam guardados apenas neste computador.")
    st.divider()
    user_agent = st.text_input(
        "Contacto para a SEC (User-Agent)",
        value=os.getenv("SEC_USER_AGENT", ""),
        help="Indique nome e email de contacto; a SEC pede identificação nas chamadas automatizadas.",
    )
    refresh = st.button("Atualizar dados oficiais", type="primary", use_container_width=True)

if refresh:
    try:
        with st.spinner("A obter Company Facts diretamente da SEC..."):
            payload = fetch_sec_json(COMPANY_FACTS_URL, user_agent)
            collected_at = save_company_facts(payload, DB_PATH)
        st.success(f"Dados originais guardados localmente. Recolha: {collected_at}")
    except Exception as exc:
        st.error(f"Não foi possível atualizar os dados: {exc}")

payload = latest_company_facts(DB_PATH)
if payload is None:
    st.info("Ainda não existem dados guardados. Introduza o contacto SEC na barra lateral e selecione «Atualizar dados oficiais».")
    st.markdown(f"**Fonte:** [SEC Company Facts — Apple]({COMPANY_FACTS_URL})")
else:
    entity_name = payload.get("entityName", "Apple Inc.")
    facts = payload.get("facts", {})
    us_gaap_tags = list(facts.get("us-gaap", {}).keys())

    c1, c2, c3 = st.columns(3)
    c1.metric("Empresa", entity_name)
    c2.metric("Tags US-GAAP", f"{len(us_gaap_tags):,}")
    c3.metric("CIK", APPLE_CIK)

    st.subheader("Explorar dados disponíveis")
    search = st.text_input("Pesquisar métrica/tag XBRL", placeholder="Ex.: Revenue, Assets, NetIncome")
    filtered = sorted(tag for tag in us_gaap_tags if search.lower() in tag.lower())
    st.dataframe(pd.DataFrame({"Tag SEC (US-GAAP)": filtered}), use_container_width=True, hide_index=True, height=360)

    st.subheader("Proveniência")
    st.write(f"Fonte original: {COMPANY_FACTS_URL}")
    st.write("O payload JSON original é preservado na base de dados SQLite local.")
    st.warning("A lista de tags é apenas exploratória. Ainda não representa métricas normalizadas nem garante comparabilidade entre períodos.")

st.divider()
st.caption("TESTE 1 · Execução local em 127.0.0.1 · Não é aconselhamento financeiro.")
