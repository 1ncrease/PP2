a = int(input())
im = 0
i = 0
m = 0
while a != 0:
    i+=1
    if a>m:         
        m = a 
        im = i
    a = int(input())    
print(im - 1)