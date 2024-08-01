# REQUIREMENTS
- Projeto: “bigquery-public-data”
- Dataset: “crypto_ethereum”
- Tabela: “tokens”

- Subir um Airflow utilizando helm em um cluster kubernetes local;
- Subir um banco Postgres local no mesmo cluster kubernetes para receber os dados;
- Construir uma DAG no Airflow capaz de integrar-se com o BigQuery e com o
Postgres para migração diária;
- Versionar todo o código dos deployments do cluster kubernetes local (arquivos yaml) e
do Airflow em um repositório git;
- Executar a DAG manualmente e verificar os dados chegando no banco Postgres;
- Executar um backfill de 7 dias para popular um histórico dos dados e verificar os dados
chegando no banco Postgres

# STEP BY STEP
## DEV
### Gerar json de autenticação, ou via cli ou baixando o arquivo via interface web
1. Ter o gcloud cli instalado
1. Checar se está autenticado 
    gcloud auth list
1. Checar se o projeto é reconhecido
    gcloud config list project
1. Habilitar a Api do BigQuery
    gcloud services enable bigquery.googleapis.com
1. Criar variável de ambiente com o id do projeto 
    export PROJECT_ID=$(gcloud config get-value core/project)
1. Criar service account que será utilizada na conexão
    gcloud iam service-accounts create python-bigquery-sa --display-name "bigquery sa for crypto-ethereum project"
1. Criar json key da service account
    gcloud iam service-accounts keys create ~/key.json --iam-account python-bigquery-sa@${PROJECT_ID}.iam.gserviceaccount.com
1. Criar variável de ambiente com a localizacão da key
    export GOOGLE_APPLICATION_CREDENTIALS=~/key.json
1. Adicionar as roles no IAM para acesso aos dados no Bigquery
    gcloud projects add-iam-policy-binding ${PROJECT_ID} --member "serviceAccount:python-bigquery-sa@${PROJECT_ID}.iam.gserviceaccount.com" --role "roles/bigquery.user"

### Criar instância postgres no Docker usando terraform
1. Executar terraform apply no ambiente de dev, pasta terraform. *** dados de autenticação salvos no próprio arquivo de variables ***

### Criar tabela no postgres
1. Utilizar psycopg2 para conexão no postgres 
1. Utilizar dll gerado pela query ao "bigquery-public-data.crypto_ethereum.INFORMATION_SCHEMA.TABLES" para criar a tabela

### Lendo dados do bigquery
1. Usar load_credentials_from_file da lib google.auth para se autenticar
1. Lib google.cloud.bigquery tem função assíncrona para realizar a query e permite salvar em dataframe *** precisa do pandas e db-dtypes ***