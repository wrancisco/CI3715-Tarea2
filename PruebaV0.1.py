# AUTHORES:
#   Francisco Marcos    11-10569
#   Julio Perez         14-10820

import unittest
from ChequeoIVSS import *

class FunctionTester(unittest.TestCase):

    # Prueba inicial con la que se espera el programa arroje una respuesta positiva.
    def testFirstPositiveMan(self):
        # Se ingresa un hombre con 75 años, 840 semas cotizadas y ningun trabajo insalubre
        self.assertTrue(chequeo_IVSS("03 07 1943", 'M', 840, 0), "Deberia Estar habilitado")
        
