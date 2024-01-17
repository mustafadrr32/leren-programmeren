PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de floowchart na

leeftijd = int(input("hoe oud ben je?"))
eindep = "Einde Programma"

if leeftijd < 18:

    print("Sorry je mag niet naar binnen.")
    print(f"Probeer het in in {18-leeftijd} jaar nog eens")
    print(eindep)


else:
    naam = input("Wat is je naam?")
    vip = input("VIP?").lower()
    if vip == "ja":
        if leeftijd >= 21:
            band = "blauw"
            print(f"Je krijgt van mij een {band} bandje")
        else:
            band = "rood"
            print(f"Je krijgt van mij een {band} bandje")
    else:
        if leeftijd >= 21:
            print("Je krijgt van mij een stempel")

    drinken = input("Wat wil je drinken?").lower()
    sorry = "Sorry geen idee wat je bedoeld, hier een glaasje water"
    if drinken == "cola":
        if band == True:
            print("Alstublieft, complimenten van het huis")
        else:
            print(f"Alsjeblieft je {drinken} dat is dan €{DRANKJES[0]}")
            
    elif drinken == "bier":
        if vip != "ja":
            print("Sorry je mag geen alcohol bestellen onder de 21")
        else:
            if band == "blauw" or band == "rood":
                print("Alstublieft, complimenten van het huis")
            else:
                print(f"Alsjeblieft je {drinken} dat is dan €{DRANKJES[1]}")


    elif drinken == "champagne":

        if band == "blauw":
            if band == "blauw":
                print(f"Alsjeblieft je {drinken} dat is dan €{DRANKJES[2]}")
            else:
                print("Sorry je mag geen alcohol bestellen onder de 21")
        else:
            print("Sorry alleen vips mogen champagne bestellen")

print(eindep)
