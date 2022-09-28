#import unittest
from unittest import TestCase, main
from libreria import division

class PruebasTest(TestCase):
    # probar division de enteros
    def test_enteros(self):
        self.assertEqual(division(10, 2), 5)

    # probar division de floats
    def test_float(self):
        self.assertEqual(division(7, 2), 3.5)


    # probar division por 0
    def test_divsion_cero(self):
        self.assertRaises(ZeroDivisionError, division, 7, 0)
main()
