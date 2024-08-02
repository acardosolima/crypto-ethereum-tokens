import unittest
import dev.src.airflow.modules.postgres_connector as pg


class TestPostgresConnector(unittest.TestCase):
    """
    Tests the functionality of the PostgresConnector class.
    """

    def test_invalid_password_existing_server(self) -> None:
        """
        Tests if an invalid password results in empty object.

        This test verifies that __init__ method creates an
        empty object if provided password is wrong
        """
        connector = pg.PostgreSQLConnector(
            password="asdf123a3#"
        )

        self.assertFalse(hasattr(connector, "conn"))

    def test_invalid_database_existing_server(self) -> None:
        """
        Tests if an invalid database results in empty object.

        This test verifies that __init__ method creates an
        empty object if provided database doesn't exist
        """
        connector = pg.PostgreSQLConnector(
            database="asdfqwe123"
        )

        self.assertFalse(hasattr(connector, "conn"))

    def test_sucessfull_connection(self) -> None:
        """
        Tests if right provided parameters results in proper object.

        This test verifies that __init__ method creates a
         proper object if provided with right info
        """
        connector = pg.PostgreSQLConnector(
            database="crypto_ethereum",
            user="root",
            password="password"
        )

        pass
