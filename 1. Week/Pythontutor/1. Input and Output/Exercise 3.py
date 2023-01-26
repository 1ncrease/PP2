wkola = int(input())
yabloki = int(input())
if (wkola > yabloki):
    print('0')
    print (yabloki % wkola)
else:
    print (int(yabloki / wkola))
    print (yabloki % wkola)