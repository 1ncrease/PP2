n = int(input())
sum = 0
sum2 = 0

for i in range(1, n):
    num = int(input())
    sum += num

for j in range(1, n + 1):
    sum2 += j

print(sum2 - sum)