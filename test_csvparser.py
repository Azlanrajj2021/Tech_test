import unittest
from unittest.mock import Mock

import csvparser


class TestMethods(unittest.TestCase):
    def test_read_row(self):
        file = Mock()
        file.configure_mock(**{'readline.return_value': "\"First\",\"Second\""})
        assert csvparser.read_row(file) == ['First','Second']


if __name__ == "__main__":
    unittest.main()
