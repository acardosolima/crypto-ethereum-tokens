module "postgres" {
  source    = "./modules/postgres"
}

# get clusterIP ip address
# get postgres user password
# create connection in airflow type postgres

module "airflow" {
  source    = "./modules/airflow"
}