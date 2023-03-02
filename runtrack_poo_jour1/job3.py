class Operation():
    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3
    def addition(self):
        return self.nombre1 + self.nombre2
p=Operation()
print("le resultat est", p.addition())
