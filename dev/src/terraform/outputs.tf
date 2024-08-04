# PostgreSQL ip address for access within kubernetes
output "postgresql_ip" {
  value = module.postgresql.postgresql_cluster_ip
}
