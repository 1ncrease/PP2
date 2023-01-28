#Note: The else block will NOT be executed if the loop is stopped by a break statement.

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Break the loop when x is 3, and see what happens with the else block: