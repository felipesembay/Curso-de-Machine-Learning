# Curso Machine Learnig

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


# Descrição do Problema de Negócio
## Contexto

Somos cientista de dados de um banco a nível mundial. No banco de dados temos informações sobre pedidos de empréstimo, categorizados em aprovados (0) e negados (1). A tarefa é utilizar esse conjunto de dados para criar um modelo preditivo que determine a probabilidade de um pedido de empréstimo ser aprovado ou negado com base nas características dos solicitantes e nas regras de negócio estabelecidas.

## Regras de Negócio
* Limite de Empréstimo: O valor máximo do empréstimo que pode ser concedido é até 4 vezes a renda anual do solicitante.
* Taxa de Juros: A taxa de juros aplicada é de 1% por parcela do empréstimo.
* Prazo de Pagamento: O prazo máximo para pagamento do empréstimo é de 48 meses (4 anos).

## Objetivo
* O objetivo principal é desenvolver um modelo de machine learning capaz de prever com precisão se um pedido de empréstimo será aprovado ou negado com base nas informações disponíveis. Este modelo ajudará a automatizar e agilizar o processo de decisão de crédito, garantindo que as decisões sejam consistentes com as regras de negócio e reduzindo o risco de inadimplência.

## Abordagem

* **Análise Exploratória de Dados (EDA):** Realizar uma análise inicial dos dados para entender as características dos solicitantes, identificar padrões e detectar possíveis problemas como dados faltantes ou outliers.

* **Pré-processamento de Dados:** Limpar e preparar os dados para o modelo, incluindo a transformação de variáveis categóricas, normalização de variáveis numéricas e tratamento de desbalanceamento de classes.

* **Divisão dos Dados:** Separar os dados em conjuntos de treino e teste para avaliar a performance do modelo de forma justa.

* **Construção do Modelo:** Desenvolver diversos modelos de machine learning utilizando pipelines para facilitar a experimentação com diferentes técnicas de pré-processamento e algoritmos.

* **Avaliação do Modelo:**  Comparar os modelos utilizando métricas de desempenho adequadas, como acurácia, precisão, recall e F1-score, selecionando o melhor modelo baseado na acurácia média.

* **Interpretação do Modelo:** Analisar a importância das features e utilizar técnicas como SHAP values para interpretar as previsões do modelo, garantindo transparência nas decisões.

* **Implementação:** Integrar o modelo preditivo no sistema de concessão de empréstimos, automatizando o processo de decisão.

## Benefícios
* Eficiência: Reduz o tempo e os custos associados à análise manual de pedidos de empréstimo.
* Consistência: Garante que todas as decisões de crédito sejam tomadas de acordo com as regras de negócio estabelecidas.
* Redução de Risco: Melhora a acurácia das decisões de crédito, reduzindo o risco de inadimplência.
* Transparência: Fornece uma base clara e interpretável para as decisões tomadas, aumentando a confiança dos solicitantes e dos stakeholders.

Essa abordagem estruturada permitirá a criação de um modelo robusto e eficiente, alinhado com os objetivos de negócio e as regras estabelecidas, contribuindo significativamente para a otimização do processo de concessão de empréstimos.


## RESULTADOS DO MODELO: 

![Resultado Geral](imagens_resultado/Captura%20de%20tela%20de%202024-05-27%2023-25-44.png)

* Ao todo foram utilizados **5 Scalers** e mais 1 com os dados normais (**None**). Nesse primeiro teste, o que obteve o melhor resultado foi o **Modelo Random Forest**. Os melhores **Scalers foram:  RobustScaler e StandardScaler**. 
* Após analisar o gráfico de **ROC AUC**, foi escolhido o scaler **StandardScaler** com um **ROC AUC** de **0.9330**, contra um ROC AUC de **0.5260**. 


![Resultado StandardScaler](imagens_resultado/Captura%20de%20tela%20de%202024-05-27%2023-28-10.png)


![Resultado StandardScaler](imagens_resultado/Captura%20de%20tela%20de%202024-05-27%2023-28-29.png)


## TRADE OFF THRESHOLD
* O próxima análise que fizemos foi a Análise Precision-Recall vs Threshold. Essa análise é importante para verificarmos aonde ocorre o cruzamento das linhas **Precision e Recall**. 


* O Threshold padrão é em **0.5**. Conforme podemos ver na imagem, o nosso ponto de cruzamento ou seja equilibrio entre Precision e Recall se encontra em **0.44**. Porém queremos um modelo mais conservador na liberação dos empréstimos. Ou seja queremos um **Recall** mais elevado. Por esse motivo o Threshold que trazia o melhor **trade-off** era no ponto **0.40**

![Resultado StandardScaler](imagens_resultado/Captura%20de%20tela%20de%202024-05-27%2023-30-42.png)

* Observe que com essa mudança o modelo ficou muito mais equilibrado. E a métrica de **F1 Score** teve uma melhora também. 

* O próximo gráfico é uma **Análise de Trade Off** entre Precision e Recall. Com base nesse gráfico seria possível chegar num **Recall** de quase **100%** e ter uma **Precision** de cerca de **80%** de acertos. Porém isso iria gerar um grande desquilibrio. Então, mantivemos um threshold mais conservador. Apenas os 40% com menos riscos terão seus empréstimos aprovados. 

![Resultado StandardScaler](imagens_resultado/Captura%20de%20tela%20de%202024-05-27%2023-30-56.png)

## FEATURE IMPORTANCE
![Resultado StandardScaler](imagens_resultado/Captura%20de%20tela%20de%202024-05-27%2023-31-12.png)

### Importâncias das Features:

* **income:** É a feature mais importante, com uma importância média de aproximadamente 0.27.
* **Profession:** Também é uma feature muito importante, com uma importância média de aproximadamente 0.20.
* **Age:** Tem uma importância média significativa de aproximadamente 0.20.
* **Experience:** Contribui com uma importância média de aproximadamente 0.11.
* **CURRENT_JOB_YRS e CURRENT_HOUSE_YRS:** Ambas têm importâncias médias por volta de 0.09 e 0.08, respectivamente.
* **Car_Ownership, Married/Single, e House_Ownership:** Têm importâncias menores, todas abaixo de 0.03.

### Interpretação
Relação com a Predição: As features com maiores valores de importância são as que mais influenciam as predições do modelo.

* **income** sendo a feature mais influente sugere que o modelo considera a renda do indivíduo como um fator crucial para a predição (por exemplo, aprovação de empréstimo).
* **Profession** e Age também são fatores significativos, indicando que o tipo de profissão e a idade dos indivíduos são relevantes para a predição do modelo.

### Diminuição da Importância:

* **Features como Car_Ownership, Married/Single, e House_Ownership**  têm menor influência comparativamente. Isso pode indicar que esses fatores têm menor impacto nas predições do modelo.
Equilíbrio das Importâncias:

É importante notar que a soma das importâncias das features deve corresponder à capacidade do modelo de fazer predições precisas. 

**Features com baixa importância**  podem ser consideradas para remoção em futuros modelos, especialmente se simplificar o modelo sem reduzir significativamente a precisão.


## SHAP VALUE
![Resultado StandardScaler](imagens_resultado/Captura%20de%20tela%20de%202024-05-27%2023-37-55.png)

### Contribuição das Features para Cada Classe

* **Experience:** Tem uma alta importância para ambas as classes, com valores SHAP significativos para Class 0 e Class 1. Isso indica que a experiência é uma feature crítica na predição do modelo para ambas as classes.

* **Age:** Similarmente à experiência, a idade tem uma alta importância para ambas as classes, com valores SHAP significativos para Class 0 e Class 1.

* **Profession:** Tem uma alta importância para Class 1 e uma menor importância para Class 0. Isso sugere que a profissão pode ser mais relevante na predição para Class 1.

* **Car_Ownership:** Contribui de forma significativa para ambas as classes, com uma importância ligeiramente maior para Class 0.

* **CURRENT_JOB_YRS e CURRENT_HOUSE_YRS:**
Ambas têm importâncias moderadas, contribuindo mais para Class 0 do que para Class 1.

* **Income:** Embora tenha menor importância comparativamente, ainda contribui de maneira relevante, especialmente para Class 0.

* **Married/Single e House_Ownership:** Estas têm menor importância, mas ainda assim contribuem de forma diferenciada para cada classe.


### Impacto nas Predições
* **Classes Balanceadas:** As features como Experience e Age são importantes para ambas as classes, sugerindo que estas são fatores críticos em geral para o modelo.

* **Importância Diferenciada:**
Features como Profession e Car_Ownership mostram uma variação maior na importância entre as classes, indicando que estas podem influenciar de maneira diferente as predições dependendo da classe.

### Gráfico de Cascata
![Resultado StandardScaler](imagens_resultado/Captura%20de%20tela%20de%202024-05-27%2023-38-18.png)

### Fórmula da Função Softmax

A função softmax é definida como:

\[ \sigma(\mathbf{x})_i = \frac{e^{x_i}}{\sum_{j} e^{x_j}} \]

Onde:
- \(\mathbf{x}\) é um vetor de entrada de valores reais.
- \(\sigma(\mathbf{x})_i\) é a probabilidade associada ao elemento \(i\) no vetor de entrada.
- \(e^{x_i}\) é a exponenciação do elemento \(x_i\).
- \(\sum_{j} e^{x_j}\) é a soma das exponenciações de todos os elementos no vetor de entrada.

### Script em Python

```python
import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)
```
### Interpretação

 **Contribuição das Features para a Predição** 
 
**Experience (Experiência):**
* Valor: 6
* Contribuição: -0.08
* Impacto: Reduz a predição final em 0.08, sugerindo que, neste exemplo, maior experiência diminui a probabilidade da predição.


**Age (Idade):**
* Valor: 65
* Contribuição: -0.07
* Impacto: Reduz a predição final em 0.07, indicando que uma idade mais alta diminui a probabilidade da predição.

**Profession (Profissão):**
* Valor: 10
* Contribuição: -0.03
* Impacto: Reduz a predição final em 0.03, mostrando que a profissão tem um impacto negativo nesta predição.

**Car_Ownership (Propriedade de Carro):**
* Valor: 0
* Contribuição: -0.01
* Impacto: Reduz a predição final em 0.01, indicando que não possuir um carro diminui a probabilidade da predição.

**CURRENT_JOB_YRS (Anos no Trabalho Atual):**
* Valor: 6
* Contribuição: -0.01
* Impacto: Reduz a predição final em 0.01, sugerindo que mais anos no trabalho atual tem um impacto negativo nesta predição.

**CURRENT_HOUSE_YRS (Anos na Casa Atual):**
* Valor: 12
* Contribuição: 0 (negligível)
* Impacto: Não afeta significativamente a predição final.

**Married/Single (Estado Civil):**
* Valor: 1
* Contribuição: 0 (negligível)
* Impacto: Não afeta significativamente a predição final.


**Income (Renda):**
* Valor: 101967.204
* Contribuição: 0 (negligível)
* Impacto: Não afeta significativamente a predição final.


**House_Ownership (Propriedade de Casa):**

* Valor: 2
* Contribuição: 0 (negligível)
* Impacto: Não afeta significativamente a predição final.

**Impacto Total na Predição**
* Valor Base (E[f(x)]):

* Representa a predição média do modelo antes de considerar as contribuições das features.Neste caso, E[f(x)] = 0.499.

* Predição Final (f(x)): Representa a predição final do modelo após somar as contribuições de todas as features. Neste caso, f(x) = 0.296.

**Diferença:**

A diferença entre o valor base e a predição final é devido às contribuições das features listadas no gráfico.


**Features Principais:**

* As features Experience, Age, Profession, Car_Ownership, e CURRENT_JOB_YRS são as que mais contribuem para a predição final neste exemplo específico, todas reduzindo o valor da predição.
Interpretação Contextual:

Este gráfico é específico para um único exemplo. 

![Resultado StandardScaler](imagens_resultado/Captura%20de%20tela%20de%202024-05-27%2023-38-37.png)


# OPTUNA - Tunagem do modelo
## Melhor Hypeparameters
![Resultado StandardScaler](imagens_resultado/Captura%20de%20tela%20de%202024-05-27%2023-39-00.png)


### Curva ROC AUC - Hyper Hypeparameters
![Resultado StandardScaler](imagens_resultado/Captura%20de%20tela%20de%202024-05-27%2023-39-33.png)






