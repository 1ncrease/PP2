import os
folder= r'C:\Users\User\Desktop\LABS\lab 6'
def exi(folder):
    filenamess = os.listdir(folder)
    for filename in filenamess:
        k=os.path.join(folder,filename)
        print(f'File: {filename}')
        print("Exist",os.access(k,os.F_OK),", Readable:",os.access(k,os.R_OK),",Writable:",os.access(k,os.W_OK), "Executable:",os.access(k,os.EX_OK))

exi(folder)