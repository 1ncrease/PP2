import re

def find(text):
    return "".join(x.capitalize() for x in text.split("_"))



print(find("salam_go_v_dotu"))