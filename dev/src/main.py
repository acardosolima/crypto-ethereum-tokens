import psycopg2
from google.cloud import bigquery
from google.auth import load_credentials_from_file


def read_bigquery():
    cred, projectId = load_credentials_from_file("dev/src/crypto-ethereum-bigquery-key.json")

    client = bigquery.Client(project=projectId, credentials=cred)

    query = """
        SELECT
            *
        FROM
            bigquery-public-data.crypto_ethereum.tokens
        LIMIT 20;
    """

    results = client.query_and_wait(query).to_dataframe()

    return results

def access_postgres():
    db_host = "localhost"
    db_database = "crypto_ethereum"
    db_user = "root"
    db_password = "password"

    try:
        with psycopg2.connect(host=db_host, database=db_database, user=db_user, password=db_password) as conn:
            print("Connected to the postgres server")
            return conn
        
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def query_postgres():

    with access_postgres() as conn:

        cur = conn.cursor()

        cur.execute("SELECT datname FROM pg_database;")
        print(cur.fetchall())

        cur.close()

def main():
    res = read_bigquery()
    print(res)

if __name__ == "__main__":
    main()
    # query_postgres()