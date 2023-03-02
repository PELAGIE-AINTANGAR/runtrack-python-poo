class Produit():
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prix = prixHT
        self.TVA = TVA
    def calculerPrixTTC(self):
        return (self.prix + self.TVA)/100
    
    def afficher(self):
        return self.nom + " " + str(self.prix) + " " + str(self.TVA)
    
    def modifierNom(self, nom):
        self.mo_nom = nom
        return self.mo_nom
    
    def modifierPrixHT(self, prix):
        self.mo_prix = prix
        return self.mo_prix
    
    def modifierTVA(self, TVA):
        self.mo_TVA = TVA
        return self.mo_TVA
    
    def nom(self):
        return self.nom
    
    def prix(self):
        return self.prix
    
    def afficheNouveau(self):
        return "les nouveaux prix ", self.mo_nom  , self.mo_prix , self.mo_TVA
    
p=Produit("pomme", 100, 18)
print(p.afficher())
print(p.calculerPrixTTC())
print(p.modifierNom("poire"))
print(p.modifierPrixHT(200))
print(p.modifierTVA(20))
print(p.afficheNouveau())