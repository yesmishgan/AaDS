import unittest
from hw1 import simple
from hw1 import exponentiation as expon
import time

NUMBER = 1267650600228229401496703205376

class TestSimpleNumber(unittest.TestCase):

    def testWork1(self):
        self.assertEqual(simple.isSimple(7), True)
    
    def testWork2(self):
        self.assertEqual(simple.isSimple(4), False)
    
class TestExpNumber(unittest.TestCase):

    def testWork1(self):
        self.assertEqual(expon.exponentiation(2, 100), NUMBER)

    def testWork2(self):
        self.assertEqual(expon.stupid_exponentiation(2, 100), NUMBER)


if __name__=='__main__':
    unittest.main()