def Palindrome(a):
    b=a[::-1]
    if a != b:
        print("Palindrome")
    else:
        print("Not a palindrome")
a=str(input())
Palindrome(a)