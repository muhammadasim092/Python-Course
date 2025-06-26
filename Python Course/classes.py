class person:
    name = 'Asim'
    age = 25
    occupation = 'Software Engineer'
    networth = 1000000
    def info(self):
        print(f" {self.name} is a {self.occupation}")
a = person()
# a.name = "Arslan"
# a.occupation = "Enginner"
# print(a.name, a.occupation)
a.info()