print("Map and reduce Filter")

# def cube(x):
#     return x*x*x
# print(cube(3))

l = [1,2,3,4,5]
# newl = []
# for item in l:
#     newl.append(cube(item))
#     print(newl)
#     print("\n")

# MAP
# print(list(map(lambda x: x*x*x, l)))

# FILTER
def filter_function(a):
    return a>4
newl = filter(filter_function , l)
# print(list(newl))

from functools import reduce

sum = reduce(lambda x,y:x+y , l)
print(sum)