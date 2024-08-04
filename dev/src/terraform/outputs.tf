# PostgreSQL ip address for access within kubernetes
output "postgresql_ip" {
  value = module.postgresql.postgresql_cluster_ip
}

output "secret_keys" {
  value = module.postgresql.secret_keys
  sensitive = true
}