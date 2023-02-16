def reverse(list):
    for i in range(len(list)):
        print(list[len(list)-i-1], end=" ")

list = input().split()
reverse(list)