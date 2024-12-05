# Sistema de Irrigação Inteligente

Este projeto é um sistema de irrigação inteligente que utiliza dados coletados de sensores ESP32 e integrações com algoritmos de aprendizado de máquina para prever a necessidade de irrigação. Além disso, uma interface interativa foi desenvolvida em Streamlit para visualização e monitoramento dos dados.

## Objetivo

O objetivo principal é otimizar o uso de água em sistemas agrícolas, utilizando um modelo preditivo baseado em dados de sensores de umidade, temperatura, pH e outros fatores ambientais.

## Estrutura do Projeto

### 1. Coleta de Dados
Os dados são coletados de sensores conectados ao ESP32 e armazenados em um banco de dados Oracle. Os dados incluem:
- Temperatura
- Umidade
- Nível de pH
- Estado da irrigação (ativo ou inativo)

### 2. Modelo de Machine Learning
Utilizamos o algoritmo **Random Forest** para prever se a irrigação é necessária com base nos dados coletados pelos sensores. As razões para escolher este algoritmo incluem:
- Capacidade de lidar com dados não linearmente separáveis.
- Boa performance com múltiplos atributos.
- Interpretação robusta.

O modelo foi treinado usando **Scikit-learn** e validado com métricas como acurácia, precisão, recall e F1-score.

### 3. Interface Interativa
Uma interface foi construída em **Streamlit**, permitindo:
- Visualização dos dados históricos do banco de dados.
- Previsão de irrigação com base nos valores inseridos manualmente.
- Monitoramento em tempo real.

### 4. Banco de Dados
Os dados dos sensores e históricos meteorológicos foram armazenados em tabelas no Oracle Database, com as seguintes estruturas principais:
- `NutrientHistory`: Registros dos sensores ESP32.
- `WeatherHistoricalData`: Dados históricos de clima (não utilizados no modelo final).

## Requisitos do Sistema

### 1. Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Streamlit**: Criação da interface gráfica.
- **Scikit-learn**: Desenvolvimento do modelo de machine learning.
- **SQLAlchemy**: Integração com o banco de dados.
- **Oracle Database**: Armazenamento de dados.
- **ESP32**: Coleta de dados dos sensores.

### 2. Instalação de Dependências
Crie um ambiente virtual e instale as dependências necessárias:
```bash
python3 -m venv .venv
source .venv/bin/activate  # No Windows, use .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configuração do Banco de Dados
Certifique-se de que o Oracle Database está configurado e populado com os dados das tabelas `NutrientHistory` e `WeatherHistoricalData`.
Execute o script `src/populate_db.py` para criar as tabelas e inserir dados de exemplo.

## Execução do Projeto

### 1. Treinamento do Modelo
Para treinar o modelo de machine learning execute  o jupyter notebook:
[prediction-dados-de-sensores](src/notbooks/prediction-dados-de-sensores.ipynb)

### 2. Executar o Streamlit
Para iniciar o servidor Streamlit e visualizar a interface:
```bash
cd src/web-app/
streamlit app.py
```

Acesse o sistema no navegador, no endereço: `http://localhost:8501`.

## Estrutura do Repositório
- `src/`: Contém os códigos-fonte.
  - `web-app/`: Interface Streamlit.
  - `notebooks/`: Notebooks Jupyter relacionados ao treinamento do modelo.
  - `populate_db.py`: Script para inserir dados no banco de dados.
  - `ml_models/`: Modelos de machine learning.
- `requirements.txt`: Dependências do projeto.
- `embedded/`: Código do ESP32.
- `docs/`: Documentação do projeto.
- `db/`: Scripts SQL para criação do banco de dados.
- `assets/`: Imagens e outros recursos.
- `README.md`: Este documento.

## Justificativas Técnicas

### Escolha do Random Forest
- Lida bem com conjuntos de dados complexos e não linearmente separáveis.
- Robustez contra overfitting, devido ao uso de múltiplas árvores de decisão.
- Simplicidade na explicação dos resultados.

### Uso do Streamlit
- Simplicidade e rapidez no desenvolvimento de interfaces.
- Integração direta com o Python e bibliotecas de visualização.

### Oracle Database
- Capacidade de lidar com grandes volumes de dados.
- Robustez e escalabilidade.

## Resultados
- **Acurácia do modelo**: 68% nos dados de validação.
- **Interface**: Ferramenta intuitiva para monitorar dados e prever a necessidade de irrigação.

## Licença
Este projeto é distribuído sob a licença MIT.
