import os
folder= r'C:\Users\User\Desktop\LABS\lab 6'
def names(folder):
    print(os.path.exists(folder))
    print(os.path.dirname(os.getcwd()))
    print(os.path.basename(folder))
names(folder)