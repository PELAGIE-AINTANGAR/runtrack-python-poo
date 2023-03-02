class Rectancle():
    #constructeur
    def __init__(self, long, width):
        self.longueur = long
        self.largeur = width
    #accesseurs  
    def __getlong__(self):
        return self.longueur
    def __getwidth__(self):
        return self.largeur
    
    #mutateurs
    def __setlong__(self, long):
        self.longueur = long
    def __setwidth__(self, width):
        self.largeur = width
#test       
p=Rectancle(10, 5)  
print(p.longueur)
print(p.largeur)
p.__setlong__(20)
print(p.longueur)
p.__setwidth__(10)
print(p.largeur)

        