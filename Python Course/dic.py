# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.get('year'))
# for key in thisdict.keys():
#     print(f" The value corrosponding to the key {key} is {thisdict.get(key)}")

# thisdict = dict(name = "John", age = 36, country = "Norway")
# for key, value in thisdict.items():
#     print(f" The value corrosponding to the key {key} is {value}")

# ep1 = {
#     122 : 80,
#     123 : 90,
#     124 : 70

# }
# ep2 = {
#     222 : 80,
#     223 : 90,
#     224 : 70
# }
# ep1.update(ep2)
# print(ep1)


myfamily = {
  "child1" : {
    "name" : "Asim",
    "year" : 2001
  },
  "child2" : {
    "name" : "Umer",
    "year" : 2007
  }
}
# print(myfamily["child2"]["name"])

for x, object in myfamily.items():
    print(x)

for y  in object:
    print(y + ':' , object[y])