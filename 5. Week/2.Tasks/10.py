import re

def find(text):
    y = re.sub("0[a-z]*_","", "_0".join(re.split("[A-Z]", text)))
    s = re.sub("0[a-z]*","", y)
    return s + "_".join(x.lower() for x  in re.findall("[A-Z][a-z]*", text))



print(find("SalamGoVDotu"))