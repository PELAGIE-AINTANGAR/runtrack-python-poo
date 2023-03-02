class Voiture():
    def __init__(self, marque, modele, année, kilometre):
        self.__marque = marque
        self.__modele = modele
        self.__année = année
        self.__kilometre = kilometre
        self.__enMarche = False
        self.__reservoire = 50
        
        
    def getMarque(self):
        return self.__marque
    def getModele(self):
        return self.__modele
    def getAnnée(self):
        return self.__année
    def getKilometre(self):
        return self.__kilometre
    def getEnMarche(self):
        return self.__enMarche
    
    
    def setMarque(self, marque):
        self.__marque = marque
    def setModele(self, modele):
        self.__modele = modele
    def setAnnée(self, année):
        self.__année = année
    def setKilometre(self, kilometre):
        self.__kilometre = kilometre
    
    
    def demarrer(self):
        if self.__verifierPlein__()>5:
            self.__enMarche = True

    
    def arreter(self):
        if not self.__enMarche:
            self.__enMarche = False
        
    
    def __verifierPlein__(self):
        return self.__reservoire
    
p=Voiture("toyota", "corolla", 2010, 10000)
print(p.getMarque())
print(p.getModele())
print(p.getAnnée())
print(p.getKilometre())
p.setMarque("mercedes")
print(p.getMarque())
p.setModele("benz")
print(p.getModele())
p.setAnnée(2015)
print(p.getAnnée())
p.setKilometre(100000)
print(p.getKilometre())
p.demarrer()
print(p.getEnMarche())
p.arreter()
print(p.getEnMarche())
print(p.__verifierPlein__())