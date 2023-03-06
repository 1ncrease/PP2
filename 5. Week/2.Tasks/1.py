import re

def find(txt):
    patern = 'a(b*)'
    return re.search(patern, txt)

print(find("absagaag"))
print(find("aafabbaf"))
print(find("vagagarav"))