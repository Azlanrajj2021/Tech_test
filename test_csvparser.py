import unittest
from unittest.mock import Mock
import csvparser

class TestMethods(unittest.TestCase):
    def test_read_row(self):
        file = Mock()
        file.configure_mock(**{'readline.return_value': "First,Second"})
        actual = csvparser.read_row(file)
        expected = 'First - Second'
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
