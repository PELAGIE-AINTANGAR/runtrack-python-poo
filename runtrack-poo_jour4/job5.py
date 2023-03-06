class Forme():
    def aire(self):
        return self.longueur * self.largeur
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        
    def aire(self):
        return 3.14 * (self.radius * self.radius)
p=Cercle(2)
print(p.aire())
k=Forme()
k.longueur=2
k.largeur=3
print(k.aire())