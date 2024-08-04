# PostgreSQL ip address for access within kubernetes
output "postgresql_cluster_ip" {
  value = data.kubernetes_service.postgresql.spec[0].cluster_ip
}

output "secret_keys" {
  value = data.kubernetes_secret.postgresql.data
  sensitive = true
}
