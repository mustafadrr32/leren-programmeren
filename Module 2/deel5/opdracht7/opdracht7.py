from fruitmand import fruitmand

x = 0
for x in range(7):
    if fruitmand[x]['round'] == True:
        print(fruitmand[x]['name'])
        x += 1
        
