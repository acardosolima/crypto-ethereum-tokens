resource "kubernetes_namespace" "airflow" {
  metadata {
    name = var.airflow_namespace
  }
}
resource "random_password" "webserver_generated_secret" {
  length  = 8
  special = true
  upper   = true
  lower   = true
}
resource "kubernetes_secret" "webserver_secret_key" {
  metadata {
    name      = "webserver-secret-key"
    namespace = kubernetes_namespace.airflow.metadata[0].name
  }

  data = {
    "secret-key" = base64encode(random_password.webserver_generated_secret.result)
  }

  type = "Opaque"
}

resource "helm_release" "airflow" {
  name       = "airflow"
  namespace  = kubernetes_namespace.airflow.metadata[0].name
  repository = "https://airflow.apache.org"
  chart      = "airflow"
  version    = var.airflow_version

  values = [file("${path.module}/airflow-values.yaml")]

  depends_on = [kubernetes_namespace.airflow]
}