class Commande():
    def __init__(self,numCommande, statuCommande):
        self.__numCommande = numCommande
        self.__listePlat =[]
        self.__statuCommande = statuCommande
        
    def getNumCommande(self):
        return self.__numCommande
    def getListePlat(self):
        return self.__listePlat
    def getStatuCommande(self):
        return self.__statuCommande
    
    def addPlat(self, plat):
        self.__listePlat.append(plat)
        
    def annulerCommande(self):
        self.__statuCommande = "annulé"
        
        