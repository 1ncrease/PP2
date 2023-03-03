import json

print('Interface Status')
print("="* 90)
print('DN' + " "*60 + 'Description' + " "*10 + 'Speed' + " "*5 + 'MTU') 
print("-"*61 + " " + "-" *19 + " "*2 + "-"*6 + " "*3 + "-"*6)

with open("sample-data.json", "r") as f:
    x = f.read()

d = json.loads(x)

def gen():
    for i in d["imdata"]:
        yield len(i["l1PhysIf"]["attributes"]["dn"])

mx = max(*gen())

for i in d["imdata"]:
    size_of_dn =len(i["l1PhysIf"]["attributes"]["dn"])
    while size_of_dn != mx:
        i["l1PhysIf"]["attributes"]["dn"] += " "
        size_of_dn = len(i["l1PhysIf"]["attributes"]["dn"])
    
    print(i["l1PhysIf"]["attributes"]["dn"] + " "*40 + i["l1PhysIf"]["attributes"]["speed"] + " "*4 +i["l1PhysIf"]["attributes"]["mtu"])