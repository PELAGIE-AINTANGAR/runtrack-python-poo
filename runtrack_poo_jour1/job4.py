class Person():
    def __init__(self, nom, prenom) :
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        return "je suis " + self.nom + self.prenom
p=Person("pelagie " , "AINTANGAR")
j=Person("emmanuel ", "AINTANGAR")
e=Person("eliakim ", "AINTANGAR")
print(p.SePresenter())
print(j.SePresenter())
print(e.SePresenter())