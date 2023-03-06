import re

def find(text):
    return " ".join(re.findall("[A-Z][a-z]*", text))



print(find("PrivetGoVDotu"))