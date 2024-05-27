import unittest
from nose2.tools import params

class TestStrings(unittest.TestCase):
    def test_upper(self):
        temp = "demo"
        self.assertEqual(temp.upper(),"DEMO")


@params("Mr. Daniel","Mrs. Gabriella","Mr. Pug")
def test_startswith(value):
    assert value.startswith("Mr")
