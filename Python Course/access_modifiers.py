class Employee:
    def __init__(self):
        self.__name = 'Asim'

a = Employee()
# print(a.__name)  # Output: Asim cannot be access through __ name attribute

# __ is used for private access modifier in python 
print(a._Employee__name)