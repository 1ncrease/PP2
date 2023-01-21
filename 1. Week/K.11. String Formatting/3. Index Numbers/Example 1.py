#You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))