# AUTHORES:
#   Francisco Marcos    11-10569
#   Julio Perez         14-10820

import unittest
from Chequeo_IVSS import *

class FunctionTester(inittest.Testcase):

    # Prueba inicial con la que se espera el programa arroje una respuesta positiva.
    def testFirstPositiveMan(self):
        # Se ingresa un hombre con 75 años, 840 semas cotizadas y ningun trabajo insalubre
        self.assertTrue(chequeoIVSS("03 07 1943", 'M', 840, 0), "Deberia Estar habilitado")
        
