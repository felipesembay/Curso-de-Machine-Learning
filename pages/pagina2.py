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
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}/{database}')


def pagina2():
    st.title("PROJETO MACHINE LEARNING END TO END - DASHBOARD METRICAS")
    #st.markdown("Dashboard da tela referente aos clientes")

    query = '''
    SELECT * 
    FROM metrics_model
    '''
    df = pd.read_sql(query, engine)
    #--------------------------------------------------------

    query2 = '''
    SELECT * 
    FROM classification_report
    '''
    df2 = pd.read_sql(query2, engine)

    #--------------------------------------------------------
    query3 = '''
    SELECT * 
    FROM confusion_matrix
    '''
    df3 = pd.read_sql(query3, engine)
    #---------------------------------------------------------

    # Filtrar as métricas necessárias
    metrics = df[['Model', 'Accuracy', 'Recall', 'Precision', 'F1 Score', 'ROC AUC', 'Date', 'Model']]

    # Convertendo a coluna Date para o formato desejado
    metrics['Date'] = pd.to_datetime(metrics['Date']).dt.date

    # Selecionar o dia mais recente
    latest_date = metrics['Date'].max()

    # Filtrar os dados para a data mais recente
    latest_metrics = metrics[metrics['Date'] == latest_date]

    # Selecionar os maiores valores para cada métrica
    best_metrics = latest_metrics.loc[latest_metrics[['Accuracy', 'Recall', 'Precision', 'F1 Score', 'ROC AUC']].idxmax()]


    # Layout com 5 colunas para as métricas
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(label="Accuracy", value=f"{best_metrics['Accuracy'].values[0]:.4f}")

    with col2:
        st.metric(label="Recall", value=f"{best_metrics['Recall'].values[0]:.4f}")

    with col3:
        st.metric(label="Precision", value=f"{best_metrics['Precision'].values[0]:.4f}")

    with col4:
        st.metric(label="F1 Score", value=f"{best_metrics['F1 Score'].values[0]:.4f}")

    with col5:
        st.metric(label="ROC AUC", value=f"{best_metrics['ROC AUC'].values[0]:.4f}")

    # Gráfico de linha interativo usando Plotly para visualizar a variação das métricas ao longo do tempo
    fig_accuracy = px.line(best_metrics, x='Date', y='Accuracy',
                  title='Accuracy Metrics Over Time', markers=True)
    fig_accuracy.update_layout(xaxis_title='Date', yaxis_title='Metrics')
    st.plotly_chart(fig_accuracy)

    fig_recall = px.line(best_metrics, x='Date', y='Recall',
                  title='Recall Metrics Over Time', markers=True)
    fig_recall.update_layout(xaxis_title='Date', yaxis_title='Metrics')
    st.plotly_chart(fig_recall)

    fig_precision = px.line(best_metrics, x='Date', y='Precision',
                  title='Precision Metrics Over Time', markers=True)
    fig_precision.update_layout(xaxis_title='Date', yaxis_title='Metrics')
    st.plotly_chart(fig_precision)

    fig_f1 = px.line(best_metrics, x='Date', y='F1 Score',
                  title='F1 Score Metrics Over Time', markers=True)
    fig_f1.update_layout(xaxis_title='Date', yaxis_title='Metrics')
    st.plotly_chart(fig_f1)

    fig_roc = px.line(best_metrics, x='Date', y='ROC AUC',
                  title='Roc Auc Metrics Over Time', markers=True)
    fig_roc.update_layout(xaxis_title='Date', yaxis_title='Metrics')
    st.plotly_chart(fig_roc)

    st.markdown("Relatório de classificação")

    # Convertendo a coluna Date para o formato desejado

    df2['Date'] = pd.to_datetime(df2['Date']).dt.date
    df2['support'] = pd.to_numeric(df2['support']).astype(int)
    df3['Date'] = pd.to_datetime(df3['Date']).dt.date

    # Selecionar a data desejada
    selected_date = st.date_input("Select a date", value=pd.to_datetime('2024-05-27'))

    # Filtrar os dados para a data selecionada
    filtered_df = df2[df2['Date'] == selected_date]
    filtered_df = df3[df3['Date'] == selected_date]

    if filtered_df.empty:
        st.write("No data available for the selected date.")
    else:
        # Filtrar as métricas necessárias
        metrics2 = df2[['precision', 'recall', 'f1-score', 'support']]

        # Filtrar as métricas necessárias
        metrics = df2[['precision', 'recall', 'f1-score', 'support']]

        # Plotly heatmap
        fig = go.Figure()

        # Adicionar as métricas de precisão, recall e f1-score
        fig.add_trace(go.Heatmap(
            z=metrics[['precision', 'recall', 'f1-score']].values,
            x=metrics[['precision', 'recall', 'f1-score']].columns,
            y=['Liberado', 'Não liberado'],
            colorscale='GnBu',
            showscale=True,
            text=metrics[['precision', 'recall', 'f1-score']].values,
            texttemplate="%{text:.4f}",
            hoverinfo="x+y+z"
        ))

        # Adicionar a métrica de suporte como uma segunda heatmap
        fig.add_trace(go.Heatmap(
            z=metrics[['support']].values,
            x=['support'],
            y=['Liberado', 'Não liberado'],
            colorscale='RdYlBu',
            showscale=False,
            text=metrics[['support']].values,
            texttemplate="%{text}",
            hoverinfo="x+y+z"
        ))

        fig.update_layout(
            title='Classification Report',
            xaxis_title='Metrics',
            yaxis_title='Classes',
            xaxis=dict(tickmode='array', tickvals=[0, 1, 2, 3], ticktext=['precision', 'recall', 'f1-score', 'support']),
            yaxis=dict(tickmode='array', tickvals=[0, 1], ticktext=['Liberado', 'Não liberado'])
        )

        st.plotly_chart(fig)


        st.title("Confusion Matrix Dashboard")
        st.table(df3[['Predicted_0', 'Predicted_1', 'Model']])
