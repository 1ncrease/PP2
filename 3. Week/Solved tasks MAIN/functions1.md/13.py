import random
print("Hello! What is your name?")
a=str(input())
print("Well, "+ a +", I am thinking of a number between 1 and 20.Take a guess.")
d=0
cnt=0
while(d==0):
    b=int(input())
    c= random.randint(1, 20)
    cnt=cnt+1
    if b==c:
        d=1
    else:
        print("Your guess is too low.Take a guess.")
print("Good job, "+ a +"! You guessed my number in "+ str(cnt) +" guesses!")