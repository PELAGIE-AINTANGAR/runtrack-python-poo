class Personnage():
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    
    def gauche(self):
        self.X = self.X - 1
        print("le joeur se deplace a gauche ", self.X)
    def droite(self):
        self.X = self.X + 1
        print("le joeur se deplace a droite ", self.X)
    def haut(self):
        self.Y = self.Y + 1
        print("le joeur se deplace en haut ", self.Y)
    def bas(self):
        self.Y = self.Y - 1
        print("le joeur se deplace en bas ", self.Y)
    def position(self):
        print("la position du joueur est", (self.X , self.Y))
    
    
    
p=Personnage(2, 3)
p.gauche()
p.droite()
p.haut()
p.bas()
p.position()