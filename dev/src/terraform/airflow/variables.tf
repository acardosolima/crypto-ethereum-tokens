variable "kubeconfig" {
  description = "Path to the kubeconfig file"
  type        = string
  default     = "~/.kube/config"
}

variable "airflow_version" {
  description = "The version of the Airflow Helm chart"
  type        = string
  default     = "1.15.0"
}

variable "airflow_namespace" {
  description = "The namespace to deploy Airflow"
  type        = string
  default     = "airflow"
}