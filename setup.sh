#! /bin/bash

TERRAFORM_DIR="dev/src/terraform/"
DESTROY_FLAG=$1


minikube_status=$(minikube status --format='{{.Host}}')

if [ "$minikube_status" != "Running" ]; then
    minikube start

    if [ $? -ne 0 ]; then
        exit 1
    fi
fi


if [ "$DESTROY_FLAG" == "destroy" ]; then
    terraform -chdir=$TERRAFORM_DIR destroy
fi

terraform -chdir=$TERRAFORM_DIR init 
terraform -chdir=$TERRAFORM_DIR validate 
terraform -chdir=$TERRAFORM_DIR apply -auto-approve


export POSTGRES_PASSWORD=$(kubectl get secret --namespace postgresql postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow