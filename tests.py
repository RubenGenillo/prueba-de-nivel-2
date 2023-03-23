import unittest
from clases import *

A = Punto(2,3)
B = Punto(5,5)
C = Punto(3, -1)
D = Punto(0,0)


class PuntosYRectangulosTestCase(unittest.TestCase):
    def testCrear(self):
        self.assertIsInstance(A, Punto)
        self.assertIsInstance(B, Punto)
        self.assertIsInstance(C, Punto)
        self.assertIsInstance(D, Punto)
        self.assertIS

    


        #self.assertFalse(self, expresion)

        #Same as self.assertTrue(isinstance(obj, cls)), with a nicer
     #  |      default message.

if __name__ == "__main__":
    unittest.main()
    

