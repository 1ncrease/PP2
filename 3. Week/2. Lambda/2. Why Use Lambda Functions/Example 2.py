#Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))