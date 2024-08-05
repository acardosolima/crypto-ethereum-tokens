#! /bin/bash

TERRAFORM_DIR="prod/src/terraform/"
DESTROY_FLAG=$1

# Check if minikube is running and if not, start the cluster
minikube_status=$(minikube status --format='{{.Host}}')

if [ "$minikube_status" != "Running" ]; then
    minikube start

    if [ $? -ne 0 ]; then
        exit 1
    fi
fi

# If parameter 'destroy' was provided, deallocates the whole environment
if [ "$DESTROY_FLAG" == "destroy" ]; then
    terraform -chdir=$TERRAFORM_DIR destroy
fi

# Executes commands required to deploy all pods and services
terraform -chdir=$TERRAFORM_DIR init 
terraform -chdir=$TERRAFORM_DIR validate 
terraform -chdir=$TERRAFORM_DIR apply -auto-approve

# Add the 'postgres' user password to an environment variable (mainly to connect to database from outside Kubernetes)
export POSTGRES_PASSWORD=$(kubectl get secret --namespace postgresql postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)

# Exposes airflow webserver on host:8080 (can be eliminated creating an ingress nginx)
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow