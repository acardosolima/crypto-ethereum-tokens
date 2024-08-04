# Kubernetes variables
variable "kubeconfig" {
  description = "Path to the kubeconfig file"
  type        = string
  default     = "~/.kube/config"
}

# PostgreSQL variables
variable "postgres_version" {
  description = "PostgreSQL Helm chart version"
  type        = string
  default     = "15.5.20"
}

variable "postgresql_namespace" {
  description = "Namespace to deploy Postgres"
  type        = string
  default     = "postgresql"
}

variable "db_name" {
  description = "Name of default database to be used"
  type        = string
  default     = "crypto_ethereum"
}

variable "num_replicas" {
  description = "Number of postgresql replicas"
  type        = number
  default     = 3
}