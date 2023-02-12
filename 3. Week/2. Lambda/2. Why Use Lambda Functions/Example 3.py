#Or, use the same function definition to make a function that always triples the number you send in:

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))