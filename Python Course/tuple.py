tup = (2 ,3,4,6)
# print(type(tup), tup)

tuples = ( "John", "Mary", "David")
temp =list(tuples)
temp.append("Asim")
temp.pop(0)
temp[1] = "Umer"
tuples = tuple(temp)
# print(tuples)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i =  i + 1