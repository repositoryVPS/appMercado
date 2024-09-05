import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime 

st.write('ONLINE')


if "data" not in st.session_state:
    df_data = pd.read_csv("CONTROLE AÇOUGUE.xlsx", index_col=0)
    st.session_state["data"] = df_data
    
    
df_data