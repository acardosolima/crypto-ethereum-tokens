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
    - [Local environment setup](#local-environment-setup)
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


### Local environment setup
1. Install [Docker Engine](https://docs.docker.com/engine/install/) and check if it is running
```
docker --version
```
2. Install [Minikube](https://k8s-docs.netlify.app/en/docs/tasks/tools/install-minikube/) and start local cluster
```
minikube start
```
3. Execute installAll.sh to initialize both postgres and airflow deployment **use terragrunt maybe?**
```
bash installAll.sh    # If using Windows
source installAll.sh  # if using Linux
```


## Contributors
- [Adriano C. Lima](mailto:adrianocardoso1991@gmail.com)
