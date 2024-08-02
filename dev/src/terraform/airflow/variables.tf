variable "kubeconfig" {
  description = "Path to the kubeconfig file"
  type        = string
  default     = "~/.kube/config"
}
variable "airflow_version" {
  description = "Version of the Airflow Helm chart"
  type        = string
  default     = "1.15.0"
}
variable "namespace" {
  description = "Namespace name of deployed Airflow"
  type        = string
  default     = "airflow"
}
