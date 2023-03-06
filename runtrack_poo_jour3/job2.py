class CompteBancaire():
    def __init__(self, nom, prenom, numCompte, solde):
        self.__nom = nom
        self.__prenom = prenom
        self.__numCompte = numCompte
        self.__solde = solde
        self.decouvert = False
        
    def getNom(self):
        return self.__nom
    def getPrenom(self):
        return self.__prenom
    def getNumCompte(self):
        return self.__numCompte
    def getSolde(self):
        return self.__solde
    
    
    def afficher(self):
        print("Nom:", self.getNom(), "Prenom:", self.getPrenom(), "Numéro de compte:", self.getNumCompte(), "Solde:", self.getSolde())
    
    def afficheSolde(self):
        print("Solde:", self.getSolde())
        
    def versement(self,somme):
        self.__solde+=somme
        return self.__solde
    
    def retirer(self,retrait):
        question = input("Voulez-vous utiliser le découvert? (oui/non)")
        reponse=input()
        if reponse == "oui":
            self.decouvert = True
            self.__solde-=retrait
        print(self.__solde)
        # if retrait > self.__solde:
        #     print("Retrait impossible")
        # else:
        #     self.__solde-=retrait
        # print(self.__solde)
    
    
    def agios(self):
        if self.__solde < 0:
            self.__solde-=10
        print("le nouveau solde est:", self.__solde)
        
        
    def virement(self,compte, somme):
        if somme > self.__solde:
            print("Virement impossible")
        else:
            self.__solde-=somme
            compte.__solde+=somme
        print("Le nouveau solde de", self.getNom(), "est:", self.__solde)
        print("Le nouveau solde de", compte.getNom(), "est:", compte.__solde)
        
        
        

        
pelagie= CompteBancaire("Pelagie", "Aintangar", 123456789, 1000)
pelagie.afficher()
pelagie.afficheSolde()
print(pelagie.versement(500))
pelagie.retirer(200)


patrick= CompteBancaire("Patrick", "Aintangar", 987654321, 2000)
pelagie.virement(patrick, 500)
patrick.afficher()