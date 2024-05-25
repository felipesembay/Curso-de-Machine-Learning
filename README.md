# Curso_Machine_Learnig

Este repositório contém os arquivos relacionados ao Curso de Machine Learning.

# Estrutura do Repositório

- **Arquivos Jupyter** -  Contém todos os notebooks utilizados para a Análise Exploratória de Dados (EDA), construção dos modelos de Machine Learning e persistência em disco (testes dos arquivos pickle dos modelos).

- **Arquivos Pickle** - Contém todos os arquivos salvos de cada um dos modelos treinados.

- **Dados** - Inclui o arquivo **JSON** utilizado para criar os dados em **SQL**. Também temos os dados em csv chamado **fake_data.csv** que são os dados fakes criados para testar o modelo. E por último o **profession_mapping.csv** que é o arquivo contendo o dicionário dos dados, referente as profissões. 

- **SQL - Database**- Contém o script utilizado para criar o `banco de dados` e a `tabela`. utilizado é o **PostgresSQL** que se encontra no nosso **Docker**. 

- **STREAMLIT**- Contém os arquivos utilizados para construir o protótipo no **Streamlit**. 

### Fontes utilizadas no Projeto:

- **KAGGLE**: Utilizamos um conjunto de dados no Kaggle para criarmos o nosso modelo. Basta clicar [aqui](https://www.kaggle.com/datasets/rohit265/loan-approval-dataset/data), para ser direcionado na pasta e baixar o arquivo. Importante frisar, que o conjunto de dados está em formato **JSON**. 

- **Render**: É no Render, que vamos criar o nosso `banco de dados` na **CLOUD** gratuitamente, sem precisar adicionar qualquer cartão de crédito. Para criar a sua conta no **render** clique [aqui](https://dashboard.render.com/)


## Sobre o Render
O Render é uma plataforma de cloud que facilita a implementação de aplicativos web, APIs, bancos de dados e outros serviços online. Algumas das vantagens do Render incluem:

* **Facilidade de Uso:** Interface amigável que simplifica a configuração e gerenciamento dos serviços.

* **Gratuito para Iniciantes:** Oferece um plano gratuito que permite criar e hospedar pequenos projetos sem custos.

* **Integração Contínua:** Suporte para integração contínua (CI/CD), facilitando o deployment automático de aplicações a partir de repositórios como GitHub e GitLab.

* **Escalabilidade:** Permite escalar os serviços conforme a necessidade do projeto, desde pequenos aplicativos até grandes sistemas de produção.

* **Segurança:**  Implementa práticas robustas de segurança para proteger os dados e aplicações.

Para utilizar o Render no seu projeto, siga os passos abaixo:

* **Criação de Conta:** Acesse Render e crie uma conta gratuita.

* **Configuração do Banco de Dados:** Após criar a conta, você pode configurar um banco de dados PostgreSQL seguindo os tutoriais disponíveis na plataforma.

* **Deployment:** Faça o deployment dos seus serviços conectando seu repositório Git e configurando os parâmetros necessários.

* **Gerenciamento:**  Utilize o dashboard do Render para gerenciar seus serviços, monitorar o desempenho e ajustar as configurações conforme necessário.

Com o Render, você pode facilmente gerenciar a infraestrutura do seu projeto de Machine Learning na cloud, garantindo disponibilidade, segurança e escalabilidade.


### Comandos GITHUB

**echo "# Curso-Machine-Learning" >> README.md**

`git init`

`git add README.md`

`git add .`

`git commit -m "first commit"`

`git branch -M main`

`git remote add origin https://github.com/felipesembay/Curso-Machine-Learning.git`

`git push -u origin main`


### or push an existing repository from the command line

`git remote add origin https://github.com/felipesembay/Curso-Machine-Learning.git`

`git branch -M main`

`git push -u origin main`







