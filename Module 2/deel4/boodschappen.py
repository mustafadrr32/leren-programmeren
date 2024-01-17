boodschappenlijst = []
a = 1
boodschappenlijst.append(input("Voeg item toe: "))

while a != 0:
    vraag = input("Wil je meer toevoegen? ").lower()
    if vraag == "ja":
        boodschappenlijst.append(input("Voeg item toe: "))
    else:
        a = 0
        print("-[ BOODSCHAPPENLIJST ]-")
        print(boodschappenlijst)