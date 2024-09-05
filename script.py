import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime 
from babel.numbers import format_currency

# Função para formatar os valores em Reais usando Babel
def formatar_valores_em_reais(valor):
    if isinstance(valor, (int, float)):  # Verifica se o valor é numérico
        return format_currency(valor, 'BRL', locale='pt_BR')
    return valor

#setando a pagina
st.set_page_config(
    layout="wide",
    page_title="CENTRO DE CUSTO"
)

st.write('ONLINE')


df_data = pd.read_excel("controle.xlsx", index_col=6,sheet_name="bd-centro-custo")
st.session_state["data"] = df_data
    
    
st.dataframe(df_data)

acougue = df_data['SETOR']

st.dataframe(acougue)


