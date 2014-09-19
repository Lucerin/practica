#!usr/bin/env python
from Figuras  import Figuras
import unittest
class TestCase(unittest.TestCase):
	def test_usuario(self):
		self.cal=Figuras()
		self.assertEqual(4, self.cal.cuadrado(2))
		self.assertEqual(6, self.cal.circulo(2.45))
		self.assertEqual(2, self.cal.rectangulo(2,1))
		self.assertEqual(5, self.cal.triangulo(2,5))
		self.assertEqual(12, self.cal.rombo(2,8))
		
		self.assertEqual(25, self.cal.cuadrado(5))
		self.assertEqual(9, self.cal.circulo(2))
		self.assertEqual(14, self.cal.rectangulo(2,7))
		self.assertEqual(4, self.cal.triangulo(2,3))
		self.assertEqual(8, self.cal.rombo(2,8))
		
		self.assertEqual(6, self.cal.cuadrado(2))
		self.assertEqual(13, self.cal.circulo(6))
		self.assertEqual(4, self.cal.rectangulo(2,2))
		self.assertEqual(8, self.cal.triangulo(2,8))
		self.assertEqual(4, self.cal.rombo(2,4))
	
		
		
		
if __name__== '__main__':
	unittest.main()
		
