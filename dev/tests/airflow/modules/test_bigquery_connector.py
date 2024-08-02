import unittest
import dev.src.airflow.modules.bigquery_connector as bq
from google.auth.exceptions import DefaultCredentialsError


class TestBigQueryConnector(unittest.TestCase):
    """
    Tests the functionality of the HTTPConector class.
    """

    def test_blank_path(self) -> None:
        """
        Tests if an invalid path results an error.

        This test verifies that __init__ method raises error
        for an empty path.
        """
        with self.assertRaises(TypeError):
            bq.BigQueryConnector()

    def test_invalid_path(self) -> None:
        """
        Tests if an invalid path results an error.

        This test verifies that __init__ method raises error
        for an invalid path for credentials file.
        """
        with self.assertRaises(DefaultCredentialsError):
            path = "/dev/test/blank_test"
            bq.BigQueryConnector(path)

    def test_valid_path(self) -> None:
        """
        Tests if a valid path results in a sucessfull instantiation.

        This test verifies that __init__ method run normally
        for a provided valid path.
        """
        pass

    def test_query_dataframe(self) -> None:
        pass
