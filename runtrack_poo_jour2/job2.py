class Livre():
    #constructeur
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages
    #accesseurs
    def getTitre(self):
        return self.__titre
    def getAuteur(self):
        return self.__auteur
    def getNbPages(self):
        return self.__nbPages
    
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
            
            
#test
p=Livre("Etudiant de soweto", "Maoundoé Naindouba", 100)
print(p.getTitre())
print(p.getAuteur())
print(p.getNbPages())
p.setTitre("Aya de Yopougon")
print(p.getTitre())
p.setAuteur("marguerite abouet")
print(p.getAuteur())
p.setNbPages(-10)
