class Personnage():
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie
        #self.__attaque = attaque
        
    def getNom(self):
        return self.__nom
    
    def getVie(self):
        return self.__vie
    # def getAttaque(self):
    #     return self.__attaque
    
    def attaquer(self, cible):
        cible.__vie -= 1
        return cible.__vie
    
    
class Jeu():
    def __init__(self, niveau):
        self.__niveau = niveau
        
    def getNiveau(self):
        return self.__niveau
    def choisirNiveau(self):
        self.__niveau = input("Choisissez un niveau: ")
        return self.__niveau
    
    def lancerJeu(self):
        if self.__niveau == "facile":
            print("Vous avez choisi le niveau facile")
        elif self.__niveau == "moyen":
            print("Vous avez choisi le niveau moyen")
        else:
            print("Vous avez choisi le niveau difficile")
       