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
    def allerEnCourss(self):
        print("je vais en cours")
        
    def afficheage(self):
        print("j'ai", self.afficheAge, "ans")
        
        
class Prof():
    def __init__(self, matiere):
        self.matiere = matiere
        
    def enseigner(self):
        print("le cours va commencer")
        
        
pela=Person()
print(pela.changeAge(15))

jean = Eleve()
jean.afficheAge()

