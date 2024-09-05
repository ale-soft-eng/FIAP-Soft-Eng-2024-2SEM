

# crie uma função busca_em_lista, que recebe 
# um elemento buscado e uma lista
# ela retorna True se o elemento está na lista
# False, caso contrário
def busca_em_lista (buscado, lista):
    if buscado in lista:
        True
    else:
        False


# crie uma função busca_em_lista, que recebe 
# um elemento buscado e uma matriz (uma lista de listas)
# ela retorna True se o elemento está na matriz (dentro de alguma das listas da matriz)
# False, caso contrário
def busca_em_matriz (buscado, matriz):
    for lista in matriz:
        if buscado in lista:
            return True
    return False

matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

busca_em_lista(5, matriz) # True
busca_em_lista(10, matriz)  # False

try:
    from gabarito_cp4 import busca_em_lista, busca_em_matriz
except:
    pass

import unittest

class TestStringMethods(unittest.TestCase):
    def test01_busca_em_lista(self):
        self.assertEqual (busca_em_lista(2,[1,2,3]), True)
        self.assertEqual (busca_em_lista(6,[1,2,3]), False)
        self.assertEqual (busca_em_lista(6,[1,2,6]), True)

    def test02_busca_em_matriz(self):
         
        self.assertEqual (busca_em_matriz(6,[[1,2,3]]),False)
        self.assertEqual (busca_em_matriz(6,[[1,2,3],[6,3,2]]),True)

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()

