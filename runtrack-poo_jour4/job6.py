class Vehicule():
    def __init__(self, marque,annee, prix):
        self.__marque = marque
        self.__annee = annee
        self.__prix = prix
        self.__model = "Classe A"
    def get_marque(self):
        return self.__marque
    def get_annee(self):
        return self.__annee 
    def get_prix(self):
        return self.__prix  
    def get_model(self):
        return self.__model
    def informationVehicule(self):
        print(self.__marque, self.__annee, self.__prix, self.__model)
     
    
    def demarrer(self):
        print("Attention, je roule")   
class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        Vehicule.__init__(self, marque, annee, prix)
        self.__portes = 4
    def get_portes(self):
        return self.__portes
    
    def demarrer(self):
        print("Attention, ma voiture est en marche")
    
    def informationVehicule(self):
           
        print("Marque=", self.get_marque(),"\n",
              "Annee=", self.get_annee(),"\n",
              "Model=", self.get_model(),"\n",
              "Prix=",self.get_prix(),"\n",
              "Nombre de porte=",self.get_portes())
p=Voiture("Mercedes", 2020, 18500)
p.informationVehicule() 
p.demarrer()
      
class Moto(Vehicule): 
    def __init__(self, marque, annee, prix):
        Vehicule.__init__(self, marque, annee, prix) 
        self.__roue=2
        self.__model="1200 Vmax"    
    def get_roue(self):
        return self.__roue
    
    def get_model(self):
        return self.__model
    
    def demarrer(self):
        print("Attention, ma moto est demarrer")
    
    def informationVehicule(self):
        print("Marque=", self.get_marque(),"\n",
              "Annee=", self.get_annee(),"\n",
              "Model=", self.get_model(),"\n",
              "Prix=",self.get_prix(),"\n",
              "Nombre de roue=",self.get_roue())    
moto=Moto("Yamaha", 1987, 4500)
moto.informationVehicule()
moto.demarrer()

