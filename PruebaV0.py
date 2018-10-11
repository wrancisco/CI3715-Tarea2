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
        
     # separamos las que deberian dar respuesta negativa de las que deberian dar respuestas positivas
    
    # Respuestas negativas
    
    # Fronteras
    
    # 59 anos
    def testAgeNegativeMan(self):
        self.assertFalse(chequeo_IVSS("06 07 1959", 'M', 760, 0), "No deberia estar habilitado")
    # 54 anos
    
    def testAgeNegativeWoman(self):
        self.assertFalse(chequeo_IVSS("06 07 1964", 'F', 760, 0), "No deberia estar habilitado")
    
    # 61 anos
        
    def testHoursNegativeMan(self):
        self.assertFalse(chequeo_IVSS("06 07 1957", 'M', 749, 0), "No deberia estar habilitado")
        
    # 56 anos
    
    def testHoursNegativeWoman(self):
        self.assertFalse(chequeo_IVSS("06 07 1962", 'F', 749, 0), "No deberia estar habilitado")
    
    # 49 anos
        
    def testRiskYearsNegativeMan(self):
        self.assertFalse(chequeo_IVSS("06 07 1969", 'F', 760, 20), "No deberia estar habilitado")
    
    # 54 anos
    
    def testRiskYearsNegativeWoman(self):
        self.assertFalse(chequeo_IVSS("06 07 1974", 'F', 760, 20), "No deberia estar habilitado")
        
    # Esquina
    # 59 anos
        
    def testEveryEdgeNegativeMan(self):
        self.assertFalse(chequeo_IVSS("06 07 1959", 'M', 749, 3), "No deberia estar habilitado")
    
    # 59 anos
        
    def testEveryEdgeNegativeWoman(self):
        self.assertFalse(chequeo_IVSS("06 07 1959", 'F', 749, 3), "No deberia estar habilitado")
        
    # Respuestas positivas
    
    # Fronteras
    
    # 60 anos
    def testAgePositiveMan(self):
        self.assertTrue(chequeo_IVSS("06 07 1958", 'M', 760, 0), "Deberia estar habilitado")
        
    # 55 anos
    
    def testAgePositiveWoman(self):
        self.assertTrue(chequeo_IVSS("06 07 1963", 'F', 760, 0), "Deberia estar habilitado")
    
    # 61 anos
        
    def testHoursPositiveMan(self):
        self.assertTrue(chequeo_IVSS("06 07 1957", 'M', 750, 0), "Deberia estar habilitado")
        
    # 56 anos
    
    def testHoursPositiveWoman(self):
        self.assertTrue(chequeo_IVSS("06 07 1962", 'F', 750, 0), "Deberia estar habilitado")
        
    # 55 anos
        
    def testRiskYearsNegativeMan(self):
        self.assertTrue(chequeo_IVSS("06 07 1963", 'F', 760, 20), "Deberia estar habilitado")
    # 50 anos
    
    def testRiskYearsNegativeWoman(self):
        self.assertTrue(chequeo_IVSS("06 07 1968", 'F', 760, 100), "Deberia estar habilitado")
        
    # Esquina
    
    # 59 anos
        
    def testEveryEdgeNegativeMan(self):
        self.assertTrue(chequeo_IVSS("06 07 1959", 'M', 750, 4), "Deberia estar habilitado")
    
    # 54 anos
        
    def testEveryEdgeNegativeWoman(self):
        self.assertTrue(chequeo_IVSS("06 07 1964", 'F', 750, 4), "Deberia estar habilitado")
        
    # Malicia
    
    # negativos
    
    # si tiene 6 anos menos de la edad y tiene 30 anos de trabajo insalubre
    
    def testBadTimingMan(self):
        self.assertFalse(chequeo_IVSS("06 07 1964", 'M', 760, 30), "No deberia estar habilitado")
    
    def testBadTimingWoman(self):
        self.assertFalse(chequeo_IVSS("06 07 1969", 'F', 760, 30), "No deberia estar habilitado")
        
    # tiene 5 anos menos de la edad pero si tiene las horas de trabajo insalubre
    
    def testGoodTimingMan(self):
        self.assertTrue(chequeo_IVSS("06 07 1963", 'M', 760, 30), "No deberia estar habilitado")
    
    def testGoodTimingWoman(self):
        self.assertTrue(chequeo_IVSS("06 07 1968", 'F', 760, 30), "No deberia estar habilitado")
        
