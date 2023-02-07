q = 0
while True:
    num = int(input())
    
    if num == 0:
        print(q)
        break
        
    if num % 2 == 0:
        q += 1