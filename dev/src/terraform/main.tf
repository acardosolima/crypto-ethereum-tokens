module "postgresql" {
  source = "./modules/postgres"
}

# --------get clusterIP ip address
#module.postgresql.postgresql_cluster_ip
# ----------get postgres user password
#module.postgresql.postgresql_user_password
# ---------create connection in airflow type postgres

module "airflow" {
  source = "./modules/airflow"
}