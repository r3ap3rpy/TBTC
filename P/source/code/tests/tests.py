import unittest 

class TestDemo(unittest.TestCase):
    def test_sum(self):
        """ This tests sum failure """
        self.assertNotEqual(sum([1,2,3,4,5]),10)
    def test_another(self):
        """ This tests sum equality """
        self.assertEqual(sum([1,2,3]),6)

if __name__ == '__main__':
    unittest.main(verbosity=3)
