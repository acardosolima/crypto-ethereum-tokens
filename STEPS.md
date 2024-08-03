# Expose airflow ui
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow

# get postgres user password
kubectl get secret postgresql -n postgresql -o jsonpath="{.data.postgres-password}" | base64 --decode

# Expose postgresql endpoint
kubectl port-forward service/postgresql 5432:5432 -n postgresql


# Setup gcp connection in airflow and paste key.json

