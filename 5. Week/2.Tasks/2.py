import re

def find(txt):
    patern = 'a(b{2,3})'
    return re.search(patern, txt)

print(find("abbsa"))
print(find("abb"))
print(find("vadffabbbbbbbsa"))