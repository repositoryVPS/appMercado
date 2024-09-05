# import streamlit as st
# import pandas as pd
# from datetime import datetime 

# # from pathlib import Path


# # pasta_atual = Path(__name__).parent
# # local = pasta_atual / 'controle.xlsx'

# #setando a pagina
# st.set_page_config(
#     layout="wide",
#     page_title="CENTRO DE CUSTO"
# )

# st.write('ONLINE')


# df_data = pd.read_excel('controle.xlsx', index_col=6,sheet_name="bd-centro-custo")
# st.session_state["data"] = df_data
    
# st.dataframe(df_data)
# acougue = df_data['SETOR']
# st.dataframe(acougue)

# df_filtrado = df_data[df_data['SETOR'] == 'ACOUGUE']
        
# for index, row in df_filtrado.iterrows():
#     print(f"Nome: {row['faturamento']}, Idade: {row['Lucro Bruto']}, Cidade: {row['MES']}")
    
# st.dataframe(df_filtrado)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para calcular a variação percentual mês a mês
def calcular_variacao(data):
    data['Variacao Faturamento'] = data['Faturamento'].pct_change() * 100
    data['Variacao Lucro Liquido'] = data['LUCRO LIQUIDO'].pct_change() * 100
    data['Variacao Despesas'] = data['DESPESAS'].pct_change() * 100
    return data

# Função para formatar valores em reais
def formatar_valor(valor):
    return f'R$ {valor:,.2f}'

# Carregar os dados (substitua pelo caminho correto ou carregue de uma fonte online)
df = pd.read_excel('controle.xlsx', sheet_name='bd-centro-custo')

# Agrupar por 'SETOR' e 'MES' e calcular as somas
grouped_df = df.groupby(['SETOR', 'MES']).agg({
    'Faturamento': 'sum',
    'LUCRO LIQUIDO': 'sum',
    'DESPESAS': 'sum'
}).reset_index()

# Sidebar para selecionar o setor
setores = grouped_df['SETOR'].unique()
setor_selecionado = st.sidebar.selectbox('Selecione o setor', setores)

# Filtrar dados do setor selecionado
setor_data = grouped_df[grouped_df['SETOR'] == setor_selecionado].sort_values(by='MES')

# Calcular variação percentual mês a mês
setor_data = calcular_variacao(setor_data)

# Aplicar formatação de reais
setor_data['Faturamento'] = setor_data['Faturamento'].apply(formatar_valor)
setor_data['LUCRO LIQUIDO'] = setor_data['LUCRO LIQUIDO'].apply(formatar_valor)
setor_data['DESPESAS'] = setor_data['DESPESAS'].apply(formatar_valor)

# # Exibir tabela de variação percentual com formatação em um tamanho maior
# st.write(f"Variação Mês a Mês - Setor: {setor_selecionado}")
# st.dataframe(setor_data[['MES', 'Faturamento', 'LUCRO LIQUIDO', 'DESPESAS', 'Variacao Faturamento', 'Variacao Lucro Liquido', 'Variacao Despesas']], height=500)


# Exibir tabela de variação percentual sem o índice
st.write(f"Variação Mês a Mês - Setor: {setor_selecionado}")
# Redefine o índice para remover o índice padrão do DataFrame
setor_data_sem_indice = setor_data.reset_index(drop=True)
# Exibe o DataFrame sem o índice
st.dataframe(setor_data_sem_indice[['MES', 'Faturamento', 'LUCRO LIQUIDO', 'DESPESAS', 'Variacao Faturamento', 'Variacao Lucro Liquido', 'Variacao Despesas']], height=500)

# Melhorar o gráfico de variação percentual
fig, ax = plt.subplots(figsize=(12, 8))

# Aplicar estilo Seaborn
sns.set(style="whitegrid")

# Plotar as variações
ax.plot(setor_data['MES'], setor_data['Variacao Faturamento'], label='Variação Faturamento', marker='o', linestyle='-', color='b')
ax.plot(setor_data['MES'], setor_data['Variacao Lucro Liquido'], label='Variação Lucro Líquido', marker='o', linestyle='--', color='g')
ax.plot(setor_data['MES'], setor_data['Variacao Despesas'], label='Variação Despesas', marker='o', linestyle='-.', color='r')

# Adicionar título e rótulos
ax.set_title(f'Variação Percentual Mês a Mês - {setor_selecionado}', fontsize=16)
ax.set_xlabel('Mês', fontsize=14)
ax.set_ylabel('Variação (%)', fontsize=14)

# Melhorar a formatação dos rótulos dos eixos
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Adicionar grid para facilitar a leitura
ax.grid(True, linestyle='--', alpha=0.6)

# Adicionar uma legenda
ax.legend(loc='upper left', fontsize=12)

# Exibir gráfico com melhoria visual
st.pyplot(fig)
