# Crypto Ethereum Tokens Pipeline
This project aims to create a data pipeline using Airflow to ingest dataset from Google Bigquery to a PostgreSQL database. This stack will run in a local environment using Kubernetes.

Project: bigquery-public-data

Dataset: crypto_ethereum

Table: tokens

## Table of contents

- [Crypto Ethereum Tokens Pipeline](#crypto-ethereum-tokens-pipeline)
  - [Table of contents](#table-of-contents)
  - [Setting up](#setting-up)
    - [Google Cloud setup](#google-cloud-setup)
    - [Install required programs](#install-required-programs)
    - [Local environment setup](#local-environment-setup)
    - [access database](#access-database)
  - [Contributors](#contributors)


## Setting up
### Google Cloud setup
1. Install [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) and configure the authentication method
2. Check if CLI is authenticated and project is listed 
```
gcloud auth list
gcloudconfig list project
```
3. Enable Bigquery API
```
gcloud services enable bigquery.googleapis.com
```
4. Create environment variable with project id
```
export PROJECT_ID=$(gcloud config get-value core/project)
```
5. Create service account in GCP
```
gcloud iam service-accounts create python-bigquery-sa --display-name "bigquery sa for crypto-ethereum project"
```
6. Create JSON access key for the service account
```
gcloud iam service-accounts keys create ~/key.json --iam-account python-bigquery-sa@${PROJECT_ID}.iam.gserviceaccount.com
```
7. Create environment variable with key location
```
export GOOGLE_APPLICATION_CREDENTIALS=~/key.json
```
8. Add IAM roles to access Bigquery datasets
```
gcloud projects add-iam-policy-binding ${PROJECT_ID} --member "serviceAccount:python-bigquery-sa@${PROJECT_ID}.iam.gserviceaccount.com" --role "roles/bigquery.user"
```


### Install required programs
1. Install [Docker Engine](https://docs.docker.com/engine/install/) and check if it is running
```
docker --version
```
2. Install [Minikube](https://k8s-docs.netlify.app/en/docs/tasks/tools/install-minikube/) and start local cluster
```
minikube start
```
3. Install [Terraform](https://developer.hashicorp.com/terraform/install) and check if it's available
```
terraform -version
```

### Local environment setup
1. Clone repo and install python dependencies within virtual environment
```
git clone https://github.com/acardosolima/crypto-ethereum-tokens.git
cd crypto-ethereum-tokens/
python -m venv .env
source .env/Scripts\activate
pip install -r requirements.txt
```
1. Execute setup.sh to initialize both postgres and airflow deployment
```
source setup.sh
```


### access database
export POSTGRES_PASSWORD=$(kubectl get secret --namespace postgresql postgresql-0 -o jsonpath="{.data.postgres-password}" | base64 -d)
kubectl port-forward --namespace teste svc/postgresql-1722793652 5432:5432 & PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432

kubectl run postgresql-1722793652-client --rm --tty -i --restart='Never' --namespace teste --image docker.io/bitnami/postgresql:16.3.0-debian-12-r23 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
  --command -- psql --host postgresql -U postgres -d postgres -p 5432

## Contributors
- [Adriano C. Lima](mailto:adrianocardoso1991@gmail.com)
