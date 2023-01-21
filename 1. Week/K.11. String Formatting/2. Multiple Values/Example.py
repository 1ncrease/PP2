#If you want to use more values, just add more values to the format() method:

#print(txt.format(price, itemno, count))
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

