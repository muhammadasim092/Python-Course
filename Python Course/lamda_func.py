double = lambda x: x*2
cube  = lambda x: x**3
print(double(5))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

x = lambda a, b : a - b
print(x(5, 3))