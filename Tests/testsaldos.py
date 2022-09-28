from unittest import  TestCase, main
from libreria import calcular_saldo_final

class TestSaldos(TestCase):
    def test_caso_feliz(self):
        self.assertEqual(calcular_saldo_final(0, [100000000, 200000000, 300000000]), 600000000)

    def test_vector_vacío(self):
        self.assertEqual(calcular_saldo_final(20, []), 20)

    def test_saldo_imposible(self):
        self.assertEqual(calcular_saldo_final(10, [10, -30, 40]), -1)

    def test_saldo_inicial_neg(self):
        #self.assertEqual(calcular_saldo_final(-10, [15, 20, 10]), None)
        self.assertIsNone(calcular_saldo_final(-10, [15, 20, 10]))

main()