class person:
    def __init__(self , o,n):
        
        print("Hey i am a person")
        self.name = n
        self.occupation = o
    def info(self):
        print(f" {self.name} is a {self.occupation}")
a = person("asim","ai enginner")
b = person("arslan","web enginner")
a.info()
b.info() 