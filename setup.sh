#! /bin/bash

minikube start

terraform -chdir=dev/src/terraform/ init 
terraform -chdir=dev/src/terraform/ validate 
terraform -chdir=dev/src/terraform/ apply -auto-approve