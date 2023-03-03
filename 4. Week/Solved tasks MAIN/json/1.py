import json

f = open("sample-data.json")
memory = json.load(f)

print('Interface Status')
print("="* 90)
print('DN' + " "*60 + 'Description' + " "*10 + 'Speed' + " "*6 + 'MTU') 
print("-"*61 + " " + "-" *20 + " "*2 + "-"*6 + " "*3 + "-"*6)
y=0
for i in memory['imdata']:
    y+=1
    out1=i["l1PhysIf"]["attributes"]["dn"]
    out11=i["l1PhysIf"]["attributes"]["fecMode"]
    out111=i["l1PhysIf"]["attributes"]["mtu"]

    print(out1,' '*39, out11,' ' * 2,out111)
    if y == 3:
        break