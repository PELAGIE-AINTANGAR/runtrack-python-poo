class Ville():
    def __init__(self, nom, nbPopulation):
        self.__nom = nom
        self.__nbPopulation = nbPopulation
        
    def getNom(self):
        return self.__nom
    def getNbPopulation(self):
        return self.__nbPopulation
    def setNbPopulation(self):
        self.__nbPopulation +=1
        return self.__nbPopulation
    
    
    
class Personne():
    def __init__(self, nom, age, __Ville):
        self.__nom = nom
        self.__age = age
        self.__ville = __Ville
    
    def getNom(self):
        return self.__nom
    def getAge(self):
        return self.__age
    def getVille(self):
        return self.__ville
    def getNbPopula(self):
        return self.__ville.getNbPopulation( )
        
    
    def ajouterPopulation(self):
        self.__ville.setNbPopulation()
        return self.__ville.getNbPopulation()
    
           
villa = Ville("Paris", 1000000)
print(villa.getNbPopulation())

marseille = Ville("Marseille", 861635)
print(marseille.getNbPopulation())

person= Personne("Jean", 20, villa)
person1=Personne("Myrtille", 4, villa)
person2=Personne("Chloé", 18, marseille)

print(person.getNom(), person.getAge(), "ans", "habitant", person.getVille().getNom())
print(person1.getNom(), person1.getAge(), "ans", "habitant", person1.getVille().getNom())
print(person2.getNom(), person2.getAge(), "ans", "habitant", person2.getVille().getNom())


person.ajouterPopulation() 
     
print("La population de", villa.getNom(), ":", villa.getNbPopulation(), "habitants")
print("La population de", marseille.getNom(), ":", marseille.getNbPopulation(), "habitants")
print("Mise a jour de la population de la ville de", villa.getNom(), ":", villa.setNbPopulation(), "habitants")
print("Mise a jour de la population de la ville de", marseille.getNom(), ":",marseille.setNbPopulation(), "habitants")

#print("La population de", villa.getNom(), ":", person.ajouterPopulation(), "habitants")