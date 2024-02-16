from fruitmand import fruitmand

for x in range(len(fruitmand)):

    if fruitmand[x]['name'] == "druif":
        print("druif gevonden")
        fruitmand.pop(x)
        break
lijst = []
for x in range(len(fruitmand)):
    
    
    if fruitmand[x]['color'] not in lijst:
        lijst.append(fruitmand[x]['color'])
print(lijst)