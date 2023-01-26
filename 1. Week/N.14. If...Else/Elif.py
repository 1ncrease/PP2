#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".