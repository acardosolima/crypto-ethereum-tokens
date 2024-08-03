# Expose airflow ui
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow

# get postgres user password
kubectl get secret postgresql -n postgresql -o jsonpath="{.data.postgres-password}" | base64 --decode

# Expose postgresql endpoint
kubectl port-forward service/postgresql 5432:5432 -n postgresql

# Setup postgresql connection in airflow and paste key.json
{
  "type": "service_account",
  "project_id": "crypto-ethereum-bigquery",
  "private_key_id": "0ed75d8cdc715e649a7d2bbc6eaaed22158ab9e4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDVW8BgxkQkYeP+\nu2D5yGj/W9Gg3jfbwNdWVaojBe5oAjYixZjHC9iPgUu9LD7mDjTv/eVqTuk6FAZx\nmmAf/8vFdYX8KOJidOeddEWBopmvX1IeZXNGt7d3APAQ/kjdjSNgBpEwCGRy51GW\niIknWOUCTxDcmnRGvlsA7bHGq8z/8qcJ6Dl22AQn7Kz16v2UTYPUVBCW748W1KRx\nbCFLrZ4BQw6vclTORuRu46JNpgWAoMzsu712FaWJW2FNIoXygRLc8mNuDh9kOCPe\nW5pfb9KQFXL+364iV1AGPTVHoMEOWU2yj2jgK7eJ7OPe1IHi+Ss2ngzTQzsJ59VO\nbMZ3T6NJAgMBAAECggEAJ8IfwMjhhNgbCOp5AULn0gIVt8EBLrmqRwPSnxEpYoda\n+DLTK/BYrDE/YGKg2/T0x24MNLm8u15k7wGB/SSJH+QtEha6TPeU+6Hhm+0lb2k3\nX8Ou7hQpI4twsPH5uRNmbqv6nTVLJqBVc1RBHqxxjHMYZMuBdHdfdPZWRPvZyS3i\nwPKgo3WUvCc+nDFugpajjuf/LVF4LN+nTx1ZjSzYh29a/uo/8tx/lUEsItwy3YPi\nFNwrDiuN8Ako+ZdFQzEa+5WUxgi0e2ZQnLbgd42HI13G+8TllnMHdM3mHyqYikJm\nCo3v07VJi6C7UYBHjhcO85+7cJTI9Ia39EFe3+uVKQKBgQD69f5Iva9Nu+PZaOzd\nHdyJxzB5/tnkWBl1+7Lk7HByZJgf2A0p/NlOHYcEebRoc1j7/EUs0Vk2eC9Khs2k\nDVA/vxuMHQ36evk4F1pDdYZWUpJaraXdVHYE9uiuTqW8nuMvDVk1BmpwVnd1B9C7\nbFSPEVsDUqE6m0/vZPcjcIEzhQKBgQDZpHieA+/T6SsYC7qVIy/lkgRM7+GmSzvC\nZPtjigu3ZwyLaY8YKNH/N62FqxpBG4TjJnoxd+VRd3ciFsogbRSbIhqKj6glE51Q\nL3MDaZ0K++8QRv+zfe2UOKDs3j0gp0jrR1VSxEbiqx1/epyT17dcFNrquTci0Fi6\nqDqi3P+R9QKBgQD0oJNFPrlCEbOReojhJTmTh/nGAVlOD16KNlZ0ddFKgKoU6Fo0\noocEcR3qi+QCqOWFg6u+ezb2NIMMp4iOsHeYG+ZzVuMIVZTXS1QuS8IuJQEKqRf0\nPl9oiXHYb0t5KHwVonJhkKZyaKa7Cmo6N+fZKbbI72PAKCLsHUQWZJVcrQKBgC05\nYd7jzofoIY5Dkae/wgogB0i9Z9QYOfiw5xPN8ZVQkmi9rIBGqywvM51c6n2w7DIP\nIsD4uuvsuRKaTbHjOK7rrTwxkazyoHOzCGEjJwDLTOfC+QshFacBBV9y5pzMZfiN\nwAsMwfYDvINqxPJrlqxJoRu5FN3lESroHhcNeQWpAoGBALS4mwCcDknlPEkYazPz\n+2pCgfevDhZYPzGqaB/frqng7JgSfucGBiWLivxjvW3P1iiqNgeagWseGvqoRWW/\neK2LQKerA9FDTKBR5xYLZRqQTjD7d0u6YRypW7Wn9k6oTscLAieVmWRqlUQl3vSf\ndOcMkGmeBVHl1PMVbqF5wFI9\n-----END PRIVATE KEY-----\n",
  "client_email": "python-bigquery-sa@crypto-ethereum-bigquery.iam.gserviceaccount.com",
  "client_id": "102015867971665818220",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/python-bigquery-sa%40crypto-ethereum-bigquery.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
