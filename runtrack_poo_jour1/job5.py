class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def afficher(self):
        print("le point est", self.x , self.y)
    def afficheX(self):
        print("le point d'abcisse est", self.x)
    def afficheY(self):
        print("le point d'ordonne est" , self.y)
    def changerX(self, x):
        self.x = x
        print("la nouvelle abcisse est", self.x)
    def changerY(self, y):
        self.y = y
        print("le nouveau ordonne est", self.y)
p=Point(2, 3)
p.afficher()
p.afficheX()
p.afficheY()
p.changerX(4)
p.changerY(5)