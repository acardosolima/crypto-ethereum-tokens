import pandas as pd
from google.cloud import bigquery
from google.auth import load_credentials_from_file
from google.auth.exceptions import DefaultCredentialsError

class BigQueryConnector:
    
    def __read_credentials_file__(self, path: str) -> tuple:
        try:
            res = load_credentials_from_file(path)
            return res

        except TypeError as t:
            print(f"{type(t).__name__:} {t}")

    def __init__(self, credentials_path: str =None) -> None:

        cred, projectId = self.__read_credentials_file__(credentials_path)
        self.client = bigquery.Client(project=projectId, credentials=cred)


    def query_dataframe_data(self, query: str) -> pd.DataFrame:

        try:
            results = self.client.query_and_wait(query)
            return results.to_dataframe()
        
        except Exception as e:
            print(f"{type(e).__name__:} {e}")


def main():
    credentials_path = "dev/src/crypto-ethereum-bigquery-key.json"
    connector = BigQueryConnector(credentials_path=credentials_path)

    query = """
        SELECT * FROM
            bigquery-public-data.crypto_ethereum.tokens
        LIMIT 20;
        """

    df = connector.query_dataframe_data(query)

    print(df)

if __name__ == "__main__":
    main()