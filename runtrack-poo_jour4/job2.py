class Person():
    def __init__(self):
        self.__age = 14
        
    def afficheAge(self):
        print(self.__age)
        
    def changeAge(self, age):
        self.__age = age
        return self.__age
    
    def bonjour(self):
        print("hello")
        
        
        
class Eleve(Person):
    def __init__(self):
        Person.__init__(self)
        
    def allerEnCourss(self):
        print("je vais en cours")
        
    def afficheage(self):
        print("j'ai", self.afficheAge, "ans")
        
        
class Prof(Person):
    def __init__(self, matiere):
        Person.__init__(self)
        self.__matiere = matiere
        
    def afficheMatiere(self):
        print(self.__matiere)
        
    def enseigner(self):
        print("le cours va commencer")
        
        
#pela=Person()
#print(pela.changeAge(15))

jean = Eleve()
jean.afficheAge()
jean.bonjour()
jean.allerEnCourss()
print(jean.changeAge(15))

profpela = Prof("maths")
print(profpela.changeAge(40))
profpela.bonjour()
profpela.enseigner()
