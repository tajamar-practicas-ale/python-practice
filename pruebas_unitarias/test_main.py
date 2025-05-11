import unittest
from main import *

class TestFunciones(unittest.TestCase):
    """
    Clase que agrupa pruebas unitarias para las funciones definidas en el archivo main.py.
    Hereda de unittest.TestCase, lo cual permite usar métodos como assertEqual, assertTrue, etc.
    """

    def test_sumar(self):
        """
        Prueba que la función 'sumar' devuelva el resultado correcto al sumar dos números.
        """
        self.assertEqual(sumar(2, 3), 5)           # 2 + 3 debe dar 5
        self.assertEqual(sumar(-1, 1), 0)          # -1 + 1 debe dar 0
        self.assertNotEqual(sumar(2, 2), 5)        # 2 + 2 no debe dar 5

    def test_eliminar_clave(self):
        """
        Prueba que la función 'eliminar_clave' elimine correctamente una clave de un diccionario.
        """
        dic = {'a': 1, 'b': 2}

        # Verifica que la clave 'a' se elimina correctamente
        self.assertTrue(eliminar_clave(dic, 'a'))
        self.assertNotIn('a', dic)  # 'a' ya no debería estar en el diccionario

        # Verifica que eliminar una clave inexistente retorna False
        self.assertFalse(eliminar_clave(dic, 'c'))

    def test_agregar_elemento_conjunto(self):
        """
        Prueba que la función 'agregar_elemento_conjunto' agregue correctamente un elemento
        a un conjunto si no existe, y que no lo agregue si ya está presente.
        """
        conj = {1, 2, 3}

        # Agrega un nuevo elemento
        self.assertTrue(agregar_elemento_conjunto(conj, 4))
        self.assertIn(4, conj)  # El número 4 debe estar ahora en el conjunto

        # Intenta agregar un elemento existente
        self.assertFalse(agregar_elemento_conjunto(conj, 2))  # Ya existe, debe retornar False

# Punto de entrada para ejecutar las pruebas si se corre directamente este archivo
if __name__ == '__main__':
    unittest.main()
