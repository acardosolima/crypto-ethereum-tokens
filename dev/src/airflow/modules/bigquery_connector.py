import pandas as pd
from google.cloud import bigquery
from google.auth import load_credentials_from_file


def get_bigquery_client_from_file(path: str) -> bigquery.Client:

    try:
        cred, projectId = load_credentials_from_file(path)
        client = bigquery.Client(project=projectId, credentials=cred)

        return client
    
    except Exception as e:
        print(f"Error while trying to read provided path: {e}")

def query_dataframe_data(query: str, bigquery_client: bigquery.Client) -> pd.DataFrame:

    try:
        results = bigquery_client.query_and_wait(query)
        return results.to_dataframe
    except Exception as e:
        print(f"Error while trying to query data from Bigquery: {e}")


def main():
    client = get_bigquery_client_from_file("dev/src/crypto-ethereum-bigquery-key.json")
    
    query = """
        SELECT * FROM
            bigquery-public-data.crypto_ethereum.tokens
        LIMIT 20;
        """

    df = query_dataframe_data(query, client)

    print(df)

if __name__ == "__main__":
    main()
