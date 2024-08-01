from psycopg2 import connect
from psycopg2 import DatabaseError
from psycopg2 import extensions

def get_postgres_connector(
        db_database: str,
        db_user: str,
        db_password: str,
        db_host: str = "localhost") -> extensions.connection:

    try:
        with connect(
            host=db_host,
            database=db_database,
            user=db_user,
            password=db_password
            ) as conn:

            return conn
        
    except DatabaseError as e:
        print(f"Could not connect to database: {e}")

def execute_statement(query: str, postgres_client: extensions.connection) -> bool:

    try:
        cur = postgres_client.cursor()
        cur.execute(query)

        postgres_client.commit()

        cur.close()

        return True

    except Exception as e:
        print(f"Could not perform operation on database: {e}")

        return False

def query_database(query: str, postgres_client: extensions.connection):
    try:
        cur = postgres_client.cursor()
        cur.execute(query)

        res = cur.fetchmany(10)
        cur.close()

        return res

    except Exception as e:
        print(f"Could not perform operation on database: {e}")

def main():
    connector = get_postgres_connector(
        db_database="crypto_ethereum",
        db_user="root",
        db_password="password"
    )

    query = """
        INSERT INTO tokens
        VALUES (
            '0x142362602f1b1ce711a9ea72a8089f49ef6e3021',
            'ETH',
            'ETH...',
            '18',
            '100000000000000000000000000',
            '2024-01-18 22:17:47.000000 UTC',
            '19036676',
            '0x8f28059bebf9a4b55b80307ab34eeda2737a68fd38030c53ea376ee549c70cc0'
        )
    """
    res = execute_statement(query, connector)

    select = """
        SELECT * FROM tokens
        LIMIT 10
    """
    print(query_database(select, connector))

    connector.close()

if __name__ == "__main__":
    main()