import re

def find(txt):
    patern = 'a.*b$'
    return re.search(patern, txt)

print(find("amanb"))
print(find("Amab"))
print(find("gikiajmg"))