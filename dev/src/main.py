from google.cloud import bigquery
from google.auth import load_credentials_from_file

cred, projectId = load_credentials_from_file("dev/src/crypto-ethereum-bigquery-key.json")

client = bigquery.Client(project=projectId, credentials=cred)

query = """
    SELECT
        table_name, ddl
    FROM
        `bigquery-public-data`.crypto_ethereum.INFORMATION_SCHEMA.TABLES
    WHERE
        table_name = 'tokens';
"""

results = client.query(query)

for row in results:
    print(row)
