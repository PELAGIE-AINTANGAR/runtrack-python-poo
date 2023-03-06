class Joeur():
    def __init__(self, name, number, position):
        self.__name = name
        self.__number = number
        self.__position = position
        self.__nbButs = 0
        self.__passDecisives = 0
        self.__nbCartonsJaunes = 0
        self.__nbCartonsRouges = 0
        # self.nbPoints = nbButs + passDecisives
    def getName(self):
        return self.__name
    
    def marquerBut(self):
        self.__nbButs += 1
        return self.__nbButs
    def effectuerPassDecisive(self):
        self.__passDecisives += 1
        return self.__passDecisives
    def recevoirCartonJaune(self):
        self.__nbCartonsJaunes += 1
        return self.__nbCartonsJaunes
    def recevoirCartonRouge(self):
        self.__nbCartonsRouges += 1
        return self.__nbCartonsRouges
    def afficherStatistique(self):
        return self.__name, self.__number, self.__position, self.__nbButs, self.__passDecisives, self.__nbCartonsJaunes, self.__nbCartonsRouges
    
class Equipe(Joeur):
    def __init__(self,nom):
        Joeur.__init__(self, nom, 0, 0)
        self.nom = nom
        self.listeJoueurs = []
        
        
    def ajouterJoueur(self, joueur):
        self.listeJoueurs.append(joueur)
    # def afficherStatistiqueJoueur(self, joueur):
    #     return joueur.afficherStatistique()
    
    def mettreAJourStatistique(self, joueur):
        joueur.marquerBut()
        joueur.effectuerPassDecisive()
        joueur.recevoirCartonJaune()
        joueur.recevoirCartonRouge()
        return joueur.afficherStatistique()
        
    def afficherStatistiqueEquipe(self):
        for joueur in self.listeJoueurs:
            print(joueur.afficherStatistique())  
            

        
joueur1 = Joeur("Messi", 10, "attaquant")
print(joueur1.afficherStatistique())
print(joueur1.marquerBut())
print(joueur1.effectuerPassDecisive())
print(joueur1.recevoirCartonJaune())
print(joueur1.recevoirCartonRouge())
#print(joueur1.afficherStatistique())

joueur2 = Joeur("Ronaldo", 7, "attaquant")
equipe1 = Equipe("Barcelone")
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.afficherStatistiqueEquipe()
