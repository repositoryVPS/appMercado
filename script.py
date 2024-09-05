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


if "data" not in st.session_state:
    df_data = pd.read_csv("controle.xlsx", index_col=0)
    st.session_state["data"] = df_data
    
    
st.dataframe(df_data)
player_stats = 1

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")