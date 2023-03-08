import os
f=open("")
def lines(f):
    text=f.read()
    cnt=0
    text1=text.split("\n")
    for i in text1:
        if i:
            cnt=cnt+1
    print(cnt)
lines(f)