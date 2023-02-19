#Also, use the global keyword if you want to make a change to a global variable inside a function.
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)