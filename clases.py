class Punto:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return "({},{})".format(self.x,self.y)
    
    def cuadrante(self):
        if self.x > 0:
            if self.y > 0:
                return "esta en el primer cuadrante"
            elif self.y < 0:
                return "esta en el cuarto cuadrante"
        elif self.x < 0:
             if self.y > 0:
                return "esta en el segundo cuadrante"
             elif self.y < 0:
                return "esta en el tercer cuadrante"
        elif self.x == 0:
            if self.y != 0:
             return "se situa en el eje Y"
            if self.y == 0:
                return "se situa en el origen"
        else:
            return "se situa en el eje X"

    def vector(self, oPunto):
        return Punto(oPunto.x - self.x, oPunto.y - self.y)
    
    def distancias(self, oPunto):
        return pow(pow(oPunto.x-self.x, 2)+pow(oPunto.y -self.y,2), 1/2)
    

class Rectangulo:
    def __init__(self, inicial = Punto(0,0), final = Punto(0,0)) -> None:
        self.inicial = inicial
        self.final = final

    def base(self):
        return abs(self.final.x - self.inicial.x)
    
    def altura(self):
        return abs(self.final.y - self.inicial.y)

    def area(self):
        return self.base()*self.altura()
    

if __name__ == "__main__":
    A = Punto(2,3)
    B = Punto(5,5)
    C = Punto(3, -1)
    D = Punto(0,0)
    print(A.cuadrante())
    print(C.cuadrante())
    print(D.cuadrante())
    print(A.vector(B))
    print(B.vector(A))
    print(A.distancias(B))
    print(B.distancias(A))
    print(C.distancias(D) < B.distancias(D) and A.distancias(D) < B.distancias(D))
    rect = Rectangulo(A,B)
    print("Base: {}, Altura: {}, Area: {}".format(rect.base(), rect.altura(), rect.area()))
