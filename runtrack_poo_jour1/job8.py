import math
class Cercle():
    def __init__(self, rayon):
        self.rayon = rayon
    def changer_rayon(self,rayon_nouveau):
        self.rayon = rayon_nouveau
        print("le nouveau rayon", self.rayon)
    def circonference(self):
        return 2*math.pi*self.rayon
    def aire_cercle(self):
        return self.rayon**2*math.pi
    def diametre(self):
        return 2*self.rayon
    
    def afficheInfos(self):
        print("le rayon est:", self.rayon,", la circoonference:", self.circonference(),", l'aire du cercle est:", self.aire_cercle(),", le diametre du cercle est:",self.diametre())

p=Cercle(4)
c=Cercle(7)
p.changer_rayon(2)
print("la circonference du cercle est", p.circonference())
print("l'aire du cercle est", p.aire_cercle())
print("le diametre du cercle est", p.diametre())
p.afficheInfos()
        
c.changer_rayon(3)
print("la circonference du cercle est", c.circonference())
print("l'aire du cercle est", c.aire_cercle())
print("le diametre du cercle est", c.diametre())
c.afficheInfos()
    
