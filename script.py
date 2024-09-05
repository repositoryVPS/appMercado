import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime 


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


