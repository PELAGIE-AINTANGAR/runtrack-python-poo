class Tache():
    def __init__(self, titre,desciption,status):
        self.__titre = titre
        self.__desciption = desciption
        self.__status = status
        
    def getTitre(self):
        return self.__titre
    def getDesciption(self):
        return self.__desciption
    def getStatus(self):
        return self.__status
    def afficherTache(self):
        return self.__titre, self.__desciption, self.__status 
    def marquerCommeFait(self):
        self.__status = "finie"
        


class LisTaches(Tache):
    def __init__(self, taches):
        Tache.__init__(self, 0, 0, 0)
        self.taches =[taches]
        
    def ajouterTache(self,tache):
        self.taches.append(tache)
    
    def supprimerTache(self,tache):
        self.taches.remove(tache)
        
    
    def marquerFinie(self):
        #print(self.taches)
        for tache in self.taches:
            if tache.getStatus() == "finie":
                print(tache.getTitre(), "La tache est deja finie")
            # else:
            #     taches.marquerCommeFait()
            #     print(tache.getTitre(), "La tache est en cours")
                
           
            
        # else:
        #     tache.status = "en cours"
        #     return tache.status
        
    
    # def marquerCommeFait(self,tache):
    #     tache.status = "en cours"
    #     return tache.status
        
    
    def filterTache(self):
        
        for tache in self.taches:
            if not tache.getStatus() == "finie":
                print(tache.afficherTache())
                
            
    def afficherTaches(self):
        for tache in self.taches:
            print(tache.afficherTache())
    
tache= Tache("titre1","desciption1","finie")
tache1= Tache("titre2","desciption2","finie")
tache2= Tache("titre4","desciption4","en cours")
tache3= Tache("titre5","desciption5","en cours")

taches = LisTaches(tache)
taches.ajouterTache(tache1)
taches.ajouterTache(tache2)
taches.ajouterTache(tache3)
taches.supprimerTache(tache2)

taches.marquerFinie()
taches.afficherTaches()
#print(taches.affichage())
taches.filterTache()

# taches.taches = taches.filterTache()
# print(taches.affichage())



