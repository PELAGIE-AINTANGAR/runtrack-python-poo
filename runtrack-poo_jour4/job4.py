
class Forme():
    def aire(self):
        return self.longueur * self.largeur
    
    
class Rectangle(Forme):
   def __init__(self, longueur, largeur):
       self.longueur = longueur
       self.largeur = largeur
       
p=Rectangle(2, 3)
print(p.aire())
       