class Student():
    def __init__(self, name, prenom, numstudent):
        self.__name = name
        self.__prenom = prenom
        self.__numstudent = numstudent
        self.__nbcredit = 0
        self.__level = self.studentEval()
        
    def getName(self):
        return self.__name
    def getPrenom(self):
        return self.__prenom
    def getNumstudent(self):
        return self.__numstudent
    def getNbcredit(self):
        return self.__nbcredit
    def addCredit(self, credit):
        for i in range(3):
            if credit > 0:
                self.__nbcredit += credit
                
            else:
                print("desole,le nombre de credit est invalide")
        print("le nombre de credit de",self.__name, self.__prenom, "est", self.__nbcredit)
        
    def studentEval(self):
        if self.__nbcredit>=90:
            return "Excellent"
        elif self.__nbcredit>=80:
            return "Tres bien"
        elif self.__nbcredit>=70:
            return "Bien"
        elif self.__nbcredit>=60:
            return "passable"
        elif self.__nbcredit<60:
            return "insuffisant"
            
    def getLevel(self):
        return self.__level
    def studentInfo(self):
        print("Nom=", self.__name, "\n",
              "Prenom=", self.__prenom, "\n",
              "id=", self.__numstudent, "\n",
              "Credits=",self.__nbcredit, "\n",
              "Niveau=", self.__level)
        
        
p=Student("john", "Doe", 145)
print(p.getName())
print(p.getPrenom())
print(p.getNumstudent())
print(p.getNbcredit())
p.addCredit(10)
print(p.getNbcredit())
print(p.getLevel())
p.studentInfo()
