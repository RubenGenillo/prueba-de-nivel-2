import unittest
from clases import *

A = Punto(2,3)
B = Punto(5,5)
C = Punto(3, -1)
D = Punto(0,0)

rect = Rectangulo(A,B)


class PuntosYRectangulosTestCase(unittest.TestCase):

    def testCrear(self):
        self.assertIsInstance(A, Punto)
        self.assertIsInstance(B, Punto)
        self.assertIsInstance(C, Punto)
        self.assertIsInstance(D, Punto)
        self.assertEqual(A.__str__(), "(2,3)")
        self.assertEqual(B.__str__(), "(5,5)")
        self.assertEqual(C.__str__(), "(3,-1)")
        self.assertEqual(D.__str__(), "(0,0)")

    def testCuadrantes(self):
        self.assertEqual(A.cuadrante(), "esta en el primer cuadrante")
        self.assertEqual(C.cuadrante(), "esta en el cuarto cuadrante")
        self.assertEqual(D.cuadrante(), "se situa en el origen")
    def testVectores(self):
        self.assertEqual(A.vector(B).__str__(), "(3,2)")
        self.assertEqual(B.vector(A).__str__(), "(-3,-2)")
    def testdistancia(self):
        self.assertEqual(A.distancias(B), 3.605551275463989)
        self.assertEqual(B.distancias(A), 3.605551275463989)
        
    def testMasLejano(self):
        self.assertLess(C.distancias(D),B.distancias(D))
        self.assertLess(A.distancias(D),B.distancias(D))

    def testCrearRectangulo(self):
        self.assertIsInstance(rect, Rectangulo)
        
    def testrectangulo(self):
        self.assertEqual(rect.base(), 3)
        self.assertEqual(rect.altura(), 2)
        self.assertEqual(rect.area(), 6)


if __name__ == "__main__":
    unittest.main()
    
