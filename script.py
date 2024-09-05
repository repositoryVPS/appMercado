import streamlit as st
import pandas as pd
from datetime import datetime 

from pathlib import Path


pasta_atual = Path(__name__).parent
local = pasta_atual / 'controle.xlsx'

#setando a pagina
st.set_page_config(
    layout="wide",
    page_title="CENTRO DE CUSTO"
)

st.write('ONLINE')


df_data = pd.read_excel(local, index_col=6,sheet_name="bd-centro-custo")
st.session_state["data"] = df_data
    
st.dataframe(df_data)
acougue = df_data['SETOR']
st.dataframe(acougue)


