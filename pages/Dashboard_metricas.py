import streamlit as st
import pandas as pd
import joblib
from sqlalchemy import create_engine
import base64
from io import BytesIO
import toml
import os
import plotly
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns


# Carregar configurações do arquivo config.toml
#config_path = os.path.join(os.path.dirname(__file__), 'config.toml')
#config = toml.load(config_path)

# Carregar variáveis de ambiente
# Obter as configurações do banco de dados
#config = config['database']
#username = config['user']
#password = config['password']
#host = config['host']
#database = config['name']

def init_connection():
    db_secrets = st.secrets["postgres"]
    connection_string = (
        f"postgresql+psycopg2://{db_secrets['user']}:{db_secrets['password']}@"
        f"{db_secrets['host']}:{db_secrets['port']}/{db_secrets['name']}"
    )
    engine = create_engine(connection_string)
    return engine

# Inicializar a conexão
engine = init_connection()

# Criar a engine de conexão
#engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')
#engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}/{database}')

st.title("PROJETO MACHINE LEARNING END TO END - DASHBOARD METRICAS")

# Consultas SQL para obter os dados
query = '''
SELECT "Scaler", "Model", "Accuracy", "Recall", "Precision", "F1 Score", "ROC AUC", "Date"::date as "Date"
FROM metrics_model
'''
df = pd.read_sql(query, engine)

query2 = '''
SELECT precision, recall, "f1-score", support, "Date"::date as "Date", "Model" 
FROM classification_report
'''
df2 = pd.read_sql(query2, engine)

query3 = '''
SELECT "Predicted_0", "Predicted_1", "Model", "Scaler", "Date"::date as "Date"
FROM confusion_matrix
'''
df3 = pd.read_sql(query3, engine)

# Convertendo a coluna Date para o formato desejado
df['Date'] = pd.to_datetime(df['Date']).dt.date

# Selecionar os maiores valores para cada métrica por dia
best_metrics_per_day = df.groupby('Date').apply(lambda x: x.loc[x[['Accuracy', 'Recall', 'Precision', 'F1 Score', 'ROC AUC']].idxmax().values[0]])

# Layout com 5 colunas para as métricas
col1, col2, col3, col4, col5 = st.columns(5)

# Selecionar os melhores valores para a data mais recente
latest_date = best_metrics_per_day['Date'].max()
latest_metrics = best_metrics_per_day[best_metrics_per_day['Date'] == latest_date]

with col1:
    st.metric(label="Accuracy", value=f"{latest_metrics['Accuracy'].values[0]:.4f}")
    
with col2:
    st.metric(label="Recall", value=f"{latest_metrics['Recall'].values[0]:.4f}")
    
with col3:
    st.metric(label="Precision", value=f"{latest_metrics['Precision'].values[0]:.4f}")
    
with col4:
    st.metric(label="F1 Score", value=f"{latest_metrics['F1 Score'].values[0]:.4f}")
    
with col5:
    st.metric(label="ROC AUC", value=f"{latest_metrics['ROC AUC'].values[0]:.4f}")

# Gráfico de linha interativo usando Plotly para visualizar a variação das métricas ao longo do tempo
fig_accuracy = px.line(best_metrics_per_day, x='Date', y='Accuracy',
              title='Accuracy Metrics Over Time', markers=True)
fig_accuracy.update_layout(xaxis_title='Date', yaxis_title='Metrics')
st.plotly_chart(fig_accuracy)

fig_recall = px.line(best_metrics_per_day, x='Date', y='Recall',
              title='Recall Metrics Over Time', markers=True)
fig_recall.update_layout(xaxis_title='Date', yaxis_title='Metrics')
st.plotly_chart(fig_recall)

fig_precision = px.line(best_metrics_per_day, x='Date', y='Precision',
              title='Precision Metrics Over Time', markers=True)
fig_precision.update_layout(xaxis_title='Date', yaxis_title='Metrics')
st.plotly_chart(fig_precision)

fig_f1 = px.line(best_metrics_per_day, x='Date', y='F1 Score',
              title='F1 Score Metrics Over Time', markers=True)
fig_f1.update_layout(xaxis_title='Date', yaxis_title='Metrics')
st.plotly_chart(fig_f1)

fig_roc = px.line(best_metrics_per_day, x='Date', y='ROC AUC',
              title='Roc Auc Metrics Over Time', markers=True)
fig_roc.update_layout(xaxis_title='Date', yaxis_title='Metrics')
st.plotly_chart(fig_roc)

st.markdown("Relatório de classificação")

# Convertendo a coluna Date para o formato desejado

df['Date'] = pd.to_datetime(df['Date']).dt.date
df2['Date'] = pd.to_datetime(df2['Date']).dt.date
df2['support'] = pd.to_numeric(df2['support']).astype(int)
df3['Date'] = pd.to_datetime(df3['Date']).dt.date

# Selecionar a data desejada
selected_date = st.date_input("Select a date", value=pd.to_datetime('2024-05-25').date())

# Filtrar os dados para a data selecionada
filtered_df2 = df2[df2['Date'] == selected_date]
filtered_df3 = df3[df3['Date'] == selected_date]

if filtered_df2.empty or filtered_df3.empty:
    st.write("No data available for the selected date.")
else:
    st.markdown("Relatório de classificação")
    
    # Filtrar as métricas necessárias
    metrics = filtered_df2[['precision', 'recall', 'f1-score', 'support']]
    
    # Plotar os heatmaps utilizando Matplotlib e Seaborn
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    
    sns.heatmap(
        metrics[['precision', 'recall', 'f1-score']],
        annot=True,
        fmt=".4f",
        cmap="GnBu",
        ax=ax[0],
        cbar=True,
        xticklabels=metrics[['precision', 'recall', 'f1-score']].columns,
        yticklabels=['Liberado', 'Não liberado']
    )
    ax[0].set_title('Precision, Recall, F1-Score')
    ax[0].set_xlabel('Metrics')
    ax[0].set_ylabel('Classes')
    
    sns.heatmap(
        metrics[['support']],
        annot=True,
        fmt="d",
        cmap="Blues",
        ax=ax[1],
        cbar=False,
        xticklabels=['support'],
        yticklabels=['Liberado', 'Não liberado']
    )
    ax[1].set_title('Support')
    ax[1].set_xlabel('Metrics')
    ax[1].set_ylabel('Classes')
    st.pyplot(fig)

    st.title("Dashboard Matriz de Confusão")

    # Exibir a matriz de confusão filtrada pela data selecionada
    #st.table(filtered_df3[['Predicted_0', 'Predicted_1', 'Model']])

    # Criar a matriz de confusão com os valores corretos
    cm = [
        [filtered_df3.iloc[0]['Predicted_0'], filtered_df3.iloc[0]['Predicted_1']],
        [filtered_df3.iloc[1]['Predicted_0'], filtered_df3.iloc[1]['Predicted_1']]
    ]

    fig_cm, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=['Predicted_0', 'Predicted_1'], yticklabels=['Actual_0', 'Actual_1'], ax=ax)
    ax.set_title(f'Confusion Matrix for Date: {selected_date}')
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')

    st.pyplot(fig_cm)