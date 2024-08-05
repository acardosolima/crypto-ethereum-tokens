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
    - [Configure airflow connections](#configure-airflow-connections)
      - [BigQuery](#bigquery)
      - [PostgreSQL](#postgresql)
    - [Validation process](#validation-process)
        - [Pre processing](#pre-processing)
        - [Single execution](#single-execution)
        - [Backfill](#backfill)
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
<a id="json_key"></a>
6. Create JSON access key for the service account 
```
gcloud iam service-accounts keys create ~/key.json --iam-account python-bigquery-sa@${PROJECT_ID}.iam.gserviceaccount.com
```
<!-- 7. Create environment variable with key location
```
export GOOGLE_APPLICATION_CREDENTIALS=~/key.json
``` -->
7. Add IAM roles to access Bigquery datasets
```
gcloud projects add-iam-policy-binding ${PROJECT_ID} --member "serviceAccount:python-bigquery-sa@${PROJECT_ID}.iam.gserviceaccount.com" --role "roles/bigquery.user"
```


### Install required programs
1. Install [Docker Engine](https://docs.docker.com/engine/install/) and check if it is running
```
docker --version
```
2. Install [Minikube](https://k8s-docs.netlify.app/en/docs/tasks/tools/install-minikube/) and check if it's working
```
minikube status
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
2. Execute setup.sh to initialize both postgres and airflow deployment.
```
source setup.sh
```

### Configure airflow connections
In the UI interface, go to **Admin > Connections > +** and add two connections configs, one for Bigquery and another for Postgres

#### BigQuery
Connection Id = 'bigquery_credentials'
Connection Type  = Google Bigquery
Keyfile JSON = Paste the content of json secret key generated in [step 1.6](#json_key)

#### PostgreSQL
Connection Id = postgres_credentials
Connection Type = Postgres
Host: Paste IP address printed in the end of *setup.sh* script
Database: crypto_ethereum
Login: postgres
Password: Paste the output of $POSTGRES_PASSWORD environment variable
Port: 5432


### Validation process

##### Pre processing
Table had no rows
![1](https://github.com/user-attachments/assets/26a0576b-eddf-4035-a10d-46f18e141d76)

##### Single execution
Inserted data for a single day
![2](https://github.com/user-attachments/assets/f0ec01e8-df14-4827-afae-47846a8b5776)
![3](https://github.com/user-attachments/assets/876e4479-4244-448d-86b1-745463a5ff48)

##### Backfill
Executed backfill process considering the last 7 days
![4](https://github.com/user-attachments/assets/860f866f-fcc4-4e53-8966-d65ac7441dab)
![6](https://github.com/user-attachments/assets/84f1744c-8552-43a0-b9df-8b98252b58dd)


## Contributors
- [Adriano C. Lima](mailto:adrianocardoso1991@gmail.com)
