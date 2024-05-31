import streamlit as st
import pandas as pd
import joblib
from sqlalchemy import create_engine
import base64
from io import BytesIO
import toml
import os

# Configurar a string de conexão
#username = 'postgres'
#password = 'airflow'
#host = '172.17.0.3'
#database = 'model_bank'

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

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded"""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV file</a>'


# Carregar modelo
with open('model3_hiperparameters.pkl', 'rb') as arquivo:
    model = joblib.load(arquivo)

def pagina1():
    st.title("PROJETO MACHINE LEARNING END TO END")
    st.markdown("Simulação de Classificação de Crédito, é um projeto para aprendizado no curso Machine Learning End to End - Youtube")

    # Dicionários para mapeamento de variáveis categóricas
    married_single_mapping = {"Não": 0, "Sim": 1}
    house_ownership_mapping = {"Sem ser alugada e sem ser casa própria": 0, "Em casa própria": 1, "Em casa alugada": 2}
    car_ownership_mapping = {"Não": 0, "Sim": 1}
    profession_mapping = {
        "Physician": 37,
        "Statistician": 44,
        "Web_designer": 50,
        "Psychologist": 40,
        "Computer_hardware_engineer": 13,
        "Drafter": 19,
        "Magistrate": 32,
        "Fashion_Designer": 22,
        "Air_traffic_controller": 0,
        "Comedian": 12,
        "Industrial_Engineer": 29,
        "Mechanical_engineer": 33,
        "Chemical_engineer": 9,
        "Technical_writer": 47,
        "Hotel_Manager": 28,
        "Financial_Analyst": 23,
        "Graphic_Designer": 27,
        "Flight_attendant": 25,
        "Biomedical_Engineer": 6,
        "Secretary": 42,
        "Software_Developer": 43,
        "Petroleum_Engineer": 36,
        "Police_officer": 38,
        "Computer_operator": 14,
        "Politician": 39,
        "Microbiologist": 34,
        "Technician": 48,
        "Artist": 4,
        "Lawyer": 30,
        "Consultant": 15,
        "Dentist": 16,
        "Scientist": 41,
        "Surgeon": 45,
        "Aviator": 5,
        "Technology_specialist": 49,
        "Design_Engineer": 17,
        "Surveyor": 46,
        "Geologist": 26,
        "Analyst": 1,
        "Army_officer": 3,
        "Architect": 2,
        "Chef": 8,
        "Librarian": 31,
        "Civil_engineer": 10,
        "Designer": 18,
        "Economist": 20,
        "Firefighter": 24,
        "Chartered_Accountant": 7,
        "Civil_servant": 11,
        "Official": 35,
        "Engineer": 21
    }

    selected_option = st.radio("Selecione uma opção:", ["Lançar manulamente", "Subir via CSV"], key='radio_option', horizontal=True)
    if selected_option == "Lançar manulamente":

        # Receber dados para o modelo processar
        with st.form(key="Include_cliente"):
            name = st.text_input(label="Insira o seu nome")
            Age = st.number_input(label="Insira a idade", min_value=0, step=1)
            st.markdown("Marca a caixa abaixo:")
            if st.checkbox('É casado?'):
                estado_civil = 0
            else:
                estado_civil = 1
            experience = st.number_input(label="Insira quantos anos de experiência no trabalho você tem?", min_value=1, step=1)
            profession = st.selectbox(label="Profissão", options=list(profession_mapping.keys()))
            current_jobs_yrs = st.number_input(label="Insira quantos anos você está no atual trabalho?", min_value=1, step=1)
            house_ownership = st.selectbox(label="Você mora em casa?", options=["Sem ser alugada e sem ser casa própria", "Em casa própria", "Em casa alugada"])
            car_ownership = st.selectbox(label="Seu carro é próprio", options=["Não", "Sim"])
            current_house_yrs = st.number_input(label="Quantos anos você mora na sua atual residência?", min_value=1, step=1)
            income = st.number_input(label="Qual a sua atual renda no ano (em dólar)?", min_value=1, step=1)
            city = st.text_input(label="Qual é a atual cidade em que você mora?")
            state = st.text_input(label="Fica no Estado/Provincía?")

            prediction_state = st.markdown('calculando...')

            # Mapear variáveis categóricas para valores numéricos
            house_ownership_mapped = house_ownership_mapping[house_ownership]
            car_ownership_mapped = car_ownership_mapping[car_ownership]
            profession_mapped = profession_mapping[profession]

            input_data = pd.DataFrame([[Age, estado_civil, experience, profession_mapped, current_jobs_yrs, 
                                        house_ownership_mapped, car_ownership_mapped, current_house_yrs, income]], 
                                      columns=['Age', 'Married/Single', 'Experience', 'Profession', 'CURRENT_JOB_YRS', 
                                               'House_Ownership', 'Car_Ownership', 'CURRENT_HOUSE_YRS', 'income'])

            submit_button = st.form_submit_button(label="Enviar")
            if submit_button:
                y_pred = model.predict(input_data)
                y_pred_proba = model.predict_proba(input_data)[0][1]

                if y_pred[0] == 1:
                    msg = '**Empréstimo Negado**'
                else:
                    msg = '**Empréstimo Liberado**'

                prediction_state.markdown(msg)
                st.success(y_pred_proba)

            #Salvar os dados no banco de dados
            # Salvar os resultados no banco de dados
                result_data = {
                    'Name': name,
                    'Age': Age,
                    'Married/Single': estado_civil,
                    'Experience': experience,
                    'Profession': profession_mapped,
                    'CURRENT_JOB_YRS': current_jobs_yrs,
                    'House_Ownership': house_ownership_mapped,
                    'Car_Ownership': car_ownership_mapped,
                    'CURRENT_HOUSE_YRS': current_house_yrs,
                    'income': income,
                    'City': city,
                    'State': state,
                    'Prediction': y_pred[0],
                    'Prediction_Probability': y_pred_proba
                }

                df_result = pd.DataFrame([result_data])

                # Inserir dados no banco
                #df_result.to_sql('bank_model', engine, schema='public', index=False, if_exists='append')
                df_result.to_sql('bank_model', engine, schema='public', index=False, if_exists='append')
                st.success("Resultado salvo no banco de dados com sucesso!")

    elif selected_option == "Subir via CSV":
        uploaded_file = st.file_uploader("Selecione um arquivo", type=['xlsx', 'csv'])

        if uploaded_file is not None:
            # Verificar o tipo do arquivo e lê-lo como um DataFrame
            try:
                if uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                    data = pd.read_excel(uploaded_file, engine='openpyxl')
                elif uploaded_file.type == 'text/csv':
                    data = pd.read_csv(uploaded_file)

                # Verificar se todas as colunas necessárias estão presentes
                required_columns = ['Name', 'Age', 'Married/Single', 'Experience', 'Profession', 'CURRENT_JOB_YRS', 
                                    'House_Ownership', 'Car_Ownership', 'CURRENT_HOUSE_YRS', 'income', 'City', 'State']
                if all(column in data.columns for column in required_columns):
                    # Mapear variáveis categóricas para valores numéricos
                    #data['House_Ownership'] = data['House_Ownership'].map(house_ownership_mapping)
                    #data['Car_Ownership'] = data['Car_Ownership'].map(car_ownership_mapping)
                    #data['Profession'] = data['Profession'].map(profession_mapping)

                    input_data = data.drop(columns=['City', 'State', 'Name'])  # Excluir 'City', 'State' e 'Name'

                    # Gerar previsões
                    data['Prediction'] = model.predict(input_data)
                    data['Prediction_Probability'] = model.predict_proba(input_data)[:, 1]

                    st.write(data)

                    # Botão para download dos resultados
                    csv = data.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Baixar resultados como CSV",
                        data=csv,
                        file_name='predictions.csv',
                        mime='text/csv',
                    )

                    # Inserir dados no banco de dados
                    #data.to_sql('bank_model', con=engine, if_exists='append', index=False)
                    data.to_sql('bank_model', engine, schema='public', index=False, if_exists='append')
                    st.success("Resultados salvos no banco de dados com sucesso!")
                else:
                    st.error("O arquivo CSV deve conter as colunas necessárias: " + ", ".join(required_columns))
            except pd.errors.EmptyDataError:
                st.error("O arquivo CSV está vazio.")
            except Exception as e:
                st.error(f"Erro ao processar o arquivo: {e}")
