# Kubernetes variables
variable "kubeconfig" {
  description = "Path to the kubeconfig file"
  type        = string
  default     = "~/.kube/config"
}

# PostgreSQL variables
variable "postgres_version" {
  description = "The version of the PostgreSQL Helm chart"
  type        = string
  default     = "15.5.20"
}

variable "postgresql_namespace" {
  description = "The namespace to deploy Postgres"
  type        = string
  default     = "postgresql"
}

variable "db_name" {
  description = "Name of default database to be used"
  type        = string
  default     = "crypto_ethereum"
}