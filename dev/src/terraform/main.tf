module "postgresql" {
  source = "./modules/postgres"
}

module "airflow" {
  source = "./modules/airflow"
}