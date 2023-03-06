import re

def find(text):
    ToFind = '[ .,]'
    return re.sub(ToFind,":",text)



print(find("privet, kak dela ????     "))