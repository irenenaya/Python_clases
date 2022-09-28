from unittest import TestCase, main
from libreria import es_mayor_a

class TestMayor(TestCase):
    def test_a_mayor(self):
        self.assertTrue(es_mayor_a(4, 3))
        #self.assertEqual(es_mayor_a(4, 3), True)

    def test_a_menor(self):
        self.assertFalse(es_mayor_a(3,4))

    def test_iguales(self):
        self.assertFalse(es_mayor_a(4,4))

main()