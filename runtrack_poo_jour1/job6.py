class Animal():
    def __init__(self, age=0, prenom=""):
        self.age = age
        print("l'age de l'animal ", self.age, " ans")
        
    def vieillir(self):
        self.age += 1
        print("l'age de l'animal ", self.age, " ans")
        
    def nommer(self, prenom):
        self.prenom = prenom
        print("l'animal se nomme ", self.prenom)
        
p=Animal()
p.age
p.vieillir()
p.nommer("luna")