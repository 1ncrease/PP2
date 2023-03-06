import re

def find(text):
    patern = '[A-Z][a-z]*'
    return re.findall(patern, text)



print(find("SalamGoVDotu"))