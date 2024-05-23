import unittest, doctest, hello_world, dundertest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(hello_world))
    tests.addTests(doctest.DocTestSuite(dundertest))
    return tests

if __name__ == '__main__':
    unittest.main()
