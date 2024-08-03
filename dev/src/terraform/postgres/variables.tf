variable "postgres_image" {
  description = "Docker image for PostgreSQL"
  type        = string
  default     = "postgres:16"
}

variable "container_name" {
  description = "Name of the PostgreSQL container"
  type        = string
  default     = "postgres_db"
}

variable "postgres_user" {
  description = "PostgreSQL user"
  type        = string
  default     = "root"
}

variable "postgres_password" {
  description = "PostgreSQL user password"
  type        = string
  default     = "password"
}

variable "postgres_db" {
  description = "PostgreSQL database name"
  type        = string
  default     = "crypto_ethereum"
}

variable "host_port" {
  description = "Host port for PostgreSQL"
  type        = number
  default     = 5432
}

variable "container_port" {
  description = "Container port for PostgreSQL"
  type        = number
  default     = 5432
}