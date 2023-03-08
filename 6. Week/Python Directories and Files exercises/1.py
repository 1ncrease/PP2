import os
folder= r'C:\Users\User\Desktop\LABS\lab 6'
def dirs(folder):
    filenamess = os.listdir(folder)
    for filename in filenamess:
        k=os.path.join(folder,filename)
        if os.path.isdir(k):
            print(f'DIR: {filename}')

def fileandfold(folder):
    filenamess = os.listdir(folder)
    for filename in filenamess:
        k=os.path.join(folder,filename)
        if os.path.isdir(k):
            print(f'DIR: {filename}')
        if os.path.isfile(k):
            print(f'File: {filename}')

def files(folder):
    filenamess = os.listdir(folder)
    for filename in filenamess:
        k=os.path.join(folder,filename)
        if os.path.isfile(k):
            print(f'File: {filename}')

dirs(folder)
fileandfold(folder)
files(folder)