class Employe:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Manager(Employe):
    def showLanguage(self):
        print("The language of Manager is Python")
        
        
e = Employe("Asim", 123)
e.showDetails() 
e2 = Manager("Asim" , 1234 )
e2.showLanguage()
