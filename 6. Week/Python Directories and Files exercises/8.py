import os

path=r"C:\Users\User\Desktop\LABS\lab 6\dest.txt"
if os.access(path,os.F_OK):
    os.remove(path)
    print("file deleted")
else:
    print("file doesnt exist")