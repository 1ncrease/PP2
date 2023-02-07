a = input()
first = a.find('h')
second = a.rfind('h')
print(a[:first + 1] + a[first + 1:second].replace('h','H') + a[second:])
