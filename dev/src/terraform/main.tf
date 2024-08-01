# Creates local postgres instance to persist ethereum data
resource "docker_image" "postgres" {
  name = var.postgres_image
}

resource "docker_container" "postgres" {
  name  = var.container_name
  image = docker_image.postgres.name
  ports {
    internal = var.container_port
    external = var.host_port
  }
  env = [
    "POSTGRES_USER=${var.postgres_user}",
    "POSTGRES_PASSWORD=${var.postgres_password}",
    "POSTGRES_DB=${var.postgres_db}"
  ]
}