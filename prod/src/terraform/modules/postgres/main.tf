# Defines PostgreSQL namespace
resource "kubernetes_namespace" "postgresql" {
  metadata {
    name = var.postgresql_namespace
  }
}

# Installs PostgreSQL via helm
resource "helm_release" "postgresql" {
  name       = "postgresql"
  namespace  = kubernetes_namespace.postgresql.metadata[0].name
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "postgresql"
  version    = var.postgres_version

  values = [file("${path.module}/postgres-values.yaml")]

  set {
    name  = "replicaCount"
    value = var.num_replicas
  }

  depends_on = [kubernetes_namespace.postgresql]
}

# Remembers info regarding created service
data "kubernetes_service" "postgresql" {
  metadata {
    name      = helm_release.postgresql.name
    namespace = helm_release.postgresql.namespace
  }

  depends_on = [helm_release.postgresql]
}

# 
data "kubernetes_secret" "postgresql" {
  metadata {
    name      = "postgresql"
    namespace = kubernetes_namespace.postgresql.metadata[0].name
  }
}
