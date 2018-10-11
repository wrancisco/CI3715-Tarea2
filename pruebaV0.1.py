import unittest
from ChequeoIVSS import *

class FuntionTester(unittest.TestCase):
    
    # separamos las que deberian dar respuesta negativa de las que deberian dar respuestas positivas
    
    # Respuestas negativas
    
    # Fronteras

    # 54 anos
    
    def testAgeNegativeWoman(self):
        self.assertFalse(person_check("06 07 1964", 'F', 760, 0), "No deberia estar habilitado")
    
    # 61 anos
        
    def testHoursNegativeMan(self):
        self.assertFalse(person_check("06 07 1957", 'M', 749, 0), "No deberia estar habilitado")
        
    # 56 anos
    
    def testHoursNegativeWoman(self):
        self.assertFalse(person_check("06 07 1962", 'F', 749, 0), "No deberia estar habilitado")
    
    # 49 anos
        
    def testRiskYearsNegativeMan(self):
        self.assertFalse(person_check("06 07 1969", 'F', 760, 20), "No deberia estar habilitado")
    
    # 54 anos
    
    def testRiskYearsNegativeWoman(self):
        self.assertFalse(person_check("06 07 1974", 'F', 760, 20), "No deberia estar habilitado")
        
    # Esquina
    # 59 anos
        
    def testEveryEdgeNegativeMan(self):
        self.assertFalse(person_check("06 07 1959", 'M', 749, 3), "No deberia estar habilitado")
    
    # 59 anos
        
    def testEveryEdgeNegativeWoman(self):
        self.assertFalse(person_check("06 07 1959", 'F', 749, 3), "No deberia estar habilitado")
    
        
    # Respuestas positivas
    
    # Fronteras
    
    # 60 anos
    def testAgePositiveMan(self):
        self.assertTrue(person_check("06 07 1958", 'M', 760, 0), "Deberia estar habilitado")
        
    # 55 anos
    
    def testAgePositiveWoman(self):
        self.assertTrue(person_check("06 07 1963", 'F', 760, 0), "Deberia estar habilitado")
    
    # 61 anos
        
    def testHoursPositiveMan(self):
        self.assertTrue(person_check("06 07 1957", 'M', 750, 0), "Deberia estar habilitado")
        
    # 56 anos
    
    def testHoursPositiveWoman(self):
        self.assertTrue(person_check("06 07 1962", 'F', 750, 0), "Deberia estar habilitado")
        
    # 55 anos
        
    def testRiskYearsNegativeMan(self):
        self.assertTrue(person_check("06 07 1963", 'F', 760, 20), "Deberia estar habilitado")
    # 50 anos
    
    def testRiskYearsNegativeWoman(self):
        self.assertTrue(person_check("06 07 1968", 'F', 760, 100), "Deberia estar habilitado")
        
    # Esquina
    
    # 59 anos
        
    def testEveryEdgeNegativeMan(self):
        self.assertTrue(person_check("06 07 1959", 'M', 750, 4), "Deberia estar habilitado")
    
    # 54 anos
        
    def testEveryEdgeNegativeWoman(self):
        self.assertTrue(person_check("06 07 1964", 'F', 750, 4), "Deberia estar habilitado")