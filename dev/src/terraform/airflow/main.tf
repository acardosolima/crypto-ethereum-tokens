resource "kubernetes_namespace" "airflow" {
  metadata {
    name = var.namespace
  }
}
resource "helm_release" "airflow" {
  name       = "airflow"
  namespace  = kubernetes_namespace.airflow.metadata[0].name
  repository = "https://airflow.apache.org"
  chart      = "airflow"
  version    = var.airflow_version
  values     = [file("${path.module}/airflow-values.yaml")]
  depends_on = [kubernetes_namespace.airflow]
}
