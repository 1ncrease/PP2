#Also, if you want to refer to the same value more than once, use the index number:

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))