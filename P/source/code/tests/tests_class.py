import unittest
from code.code import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(2,8)
        self.scalculator = Calculator('a','b')
    def test_sum(self):
        """ Test sum from Calculator class! """
        self.assertEqual(self.calculator.sum(),'a + b = 10')

    def test_multiply(self):
        """ Test multiply from Calculator class! """
        self.assertEqual(self.calculator.multiply(),'a * b = 16')

    def test_string_sum(self):
        """ Test sum of two string with Calculator class! """
        self.assertEqual(self.scalculator.sum(),"a + b = ab")

class TestCalculatorAssertions(unittest.TestCase):
    def setUp(self):
        self.c = Calculator(10,20)

    def test_truthyness(self):
        self.assertTrue(self.c.truthyness())
    def test_not_truthyness(self):
        self.assertFalse(not self.c.truthyness())
    def test_isyness(self):
        self.assertIs(self.c, self.c)
    def test_nonness(self):
        self.assertIsNone(self.c.noness())
    def test_inness(self):
        self.assertIn(self.c, [self.c,self.c])
    def test_instanceness(self):
        self.assertIsInstance(self.c, Calculator)

