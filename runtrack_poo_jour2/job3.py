class Livre():
    #constructeur
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages
        self.__disponible = True
    #accesseurs
    def getTitre(self):
        return self.__titre
    def getAuteur(self):
        return self.__auteur
    def getNbPages(self):
        return self.__nbPages
    def getDisponible(self):
        return self.__disponible
    
    #mutateurs
    def setTitre(self, titre):
        self.__titre = titre
    def setAuteur(self, auteur):
        self.__auteur = auteur
    def setNbPages(self, nbPages):
        if nbPages > 0:
            self.__nbPages = nbPages
        else:
            print("desole,le nombre de pages est invalide")
            
    def verifierDisponibilite(self):
        return self.__disponible
        
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
        
        else:
            print("indisponible")
    def rendre(self):
        if not self.verifierDisponibilite():
            self.__disponible = True
            
p=Livre("Etudiant de soweto", "Maoundoé Naindouba", 100)
print(p.getTitre())
print(p.getAuteur())
print(p.getNbPages())
print(p.getDisponible())
p.setTitre("Aya de Yopougon")
print(p.getTitre())
p.setAuteur("marguerite abouet")
print(p.getAuteur())
p.setNbPages(-10)
p.emprunter()
print(p.getDisponible())
p.rendre()
print(p.getDisponible())


    