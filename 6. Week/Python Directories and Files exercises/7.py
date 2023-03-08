import os
import shutil
source=r"C:\Users\User\Desktop\LABS\lab 6\brands.txt"
open("dest.txt","w")
dest=r"C:\Users\User\Desktop\LABS\lab 6\dest.txt"
def copy(source,dest):
    shutil.copy(source,dest)
copy(source,dest)