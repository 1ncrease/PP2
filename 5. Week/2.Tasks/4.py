import re

def find(txt):
    patern = '[A-Z]{1}[a-z]+'
    return re.search(patern, txt)

print(find("Abaag"))
print(find("AGjmgjag"))
print(find("akmgkGAGgmjagm"))
print(find("jgmjangja"))