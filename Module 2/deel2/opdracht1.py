alledagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")


print("Alle dagen van de week zijn: ")
for x in alledagen:
    print(x)

print("")


print("De werkdagen zijn: ")

for x in range(5):
    print(alledagen[x])

print("")

print("De weekenddagen zijn: ")

for x in range(5, 7):
    print(alledagen[x])

print("")

print("Alle dagen van de week in omgekeerde volgorde zijn: ")

for x in range(6, -1, -1):
    print(alledagen[x]) 

print("")

print("De werkdagen in omgekeerde volgorde zijn: ")

for x in range (4, -1, -1):
    print(alledagen[x])

print("")

print("De weekenddagen in omgekeerde volgorde zijn: ")

for x in range(6, 4, -1):
    print(alledagen[x])