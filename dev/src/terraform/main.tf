module "postgresql" {
  source = "./modules/postgres"
}

#get clusterIP ip address
output "postgresql_cluster_ip" {
  value = module.postgresql.postgresql_cluster_ip
}

module "airflow" {
  source = "./modules/airflow"
}