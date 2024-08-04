#! /bin/bash

TERRAFORM_DIR="dev/src/terraform/"
DESTROY_FLAG=$1

#minikube start

if [ "$DESTROY_FLAG" == "destroy" ]; then
    terraform -chdir=$TERRAFORM_DIR destroy --auto-approve
fi

terraform -chdir=$TERRAFORM_DIR init 
terraform -chdir=$TERRAFORM_DIR validate 
terraform -chdir=$TERRAFORM_DIR apply -auto-approve

#export POSTGRES_PASSWORD=$(kubectl get secret --namespace postgresql postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)