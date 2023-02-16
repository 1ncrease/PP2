def solve(a,b):
    chikens=b/2-a
    return chikens,a-chikens
a=int(input())
b=int(input())
print (solve(a,b))