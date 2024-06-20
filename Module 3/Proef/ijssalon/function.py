from data import PRIJS_BOLLETJE, PRIJS_HOORNTJE, PRIJS_BAKJE
from data import PRIJS_SLAGROOM, PRIJS_SPRINKELS_PER_BOLLETJE, PRIJS_CARAMEL_SAUS_HOORNTJE, PRIJS_CARAMEL_SAUS_BAKJE
from data import totaal_bolletjes, totaal_hoorntjes, totaal_bakjes, smaken, topping_kosten

def welkom():
    print("Welkom bij Papi Gelato")

def vraag_bolletjes():
    global totaal_bolletjes, totaal_bakjes
    while True:
        try:
            a_bolletjes = int(input("Hoeveel bolletjes wilt u? "))
            if 1 <= a_bolletjes <= 3:
                totaal_bolletjes += a_bolletjes
                return a_bolletjes, "keuze"
            elif 4 <= a_bolletjes <= 8:
                totaal_bolletjes += a_bolletjes
                totaal_bakjes += 1
                
                return a_bolletjes, "bakje"
            elif a_bolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet.")
                continue    
            else:
                print("Sorry, dat snap ik niet...")
                continue
        except ValueError:
            print("Sorry, dat snap ik niet...")

def vraag_smaken(a_bolletjes):
    for i in range(1, a_bolletjes + 1):
        while True:
            smaak = input(f"Welke smaak wilt u voor bolletje nummer {i}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ").upper()
            if smaak in ["A", "C", "M", "V"]:
                if smaak == "A":
                    smaken["Aardbei"] += 1
                elif smaak == "C":
                    smaken["Chocolade"] += 1
                elif smaak == "M":
                    smaken["Munt"] += 1
                elif smaak == "V":
                    smaken["Vanille"] += 1
                break
            else:
                print("Sorry dat snap ik niet...")

def vraag_container(a_bolletjes):
    global totaal_hoorntjes, totaal_bakjes
    while True:
        keuze = input(f"Wilt u deze {a_bolletjes} bolletje(s) in een hoorntje of een bakje? ").lower()
        if keuze in ["hoorntje", "bakje"]:
            if keuze == "hoorntje":
                totaal_hoorntjes += 1
            elif keuze == "bakje":
                totaal_bakjes += 1
            return keuze
        else:
            print("Sorry, dat snap ik niet...")

def vraag_topping(container, a_bolletjes):
    global topping_kosten
    while True:
        topping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ").upper()
        if topping in ["A", "B", "C", "D"]:
            if topping == "A":
                return
            elif topping == "B":
                topping_kosten += PRIJS_SLAGROOM
            elif topping == "C":
                topping_kosten += PRIJS_SPRINKELS_PER_BOLLETJE * a_bolletjes
            elif topping == "D":
                if container == "hoorntje":
                    topping_kosten += PRIJS_CARAMEL_SAUS_HOORNTJE
                else:
                    topping_kosten += PRIJS_CARAMEL_SAUS_BAKJE
            return
        else:
            print("Sorry, dat snap ik niet...")

def bevestig_bestelling(container, a_bolletjes):
    print(f"Hier is uw {container} met {a_bolletjes} bolletje(s).")

def vraag_nogmeer():
    while True:
        nogmeer = input("Wilt u nog meer bestellen? (J/N) ").lower()
        if nogmeer == "j":
            return True
        elif nogmeer == "n":
            return False
        else:
            print("Sorry, dat snap ik niet...")

def print_bonnetje():
    print("\n---[ Bonnetje ]---")
    if totaal_bolletjes > 0:
        for smaak, aantal in smaken.items():
            if aantal > 0:
                print(f"  B.{smaak}  : {aantal} x  {PRIJS_BOLLETJE:.2f} = {aantal * PRIJS_BOLLETJE:.2f} ")
    if totaal_hoorntjes > 0:
        print(f"Hoorntjes     : {totaal_hoorntjes} x €{PRIJS_HOORNTJE:.2f} = €{totaal_hoorntjes * PRIJS_HOORNTJE:.2f}")
    if totaal_bakjes > 0:
        print(f"Bakjes        : {totaal_bakjes} x €{PRIJS_BAKJE:.2f} = €{totaal_bakjes * PRIJS_BAKJE:.2f}")
    if topping_kosten > 0:
        print(f"Toppings      : €{topping_kosten:.2f}")
    totaal_prijs = (totaal_bolletjes * PRIJS_BOLLETJE) + (totaal_hoorntjes * PRIJS_HOORNTJE) + (totaal_bakjes * PRIJS_BAKJE) + topping_kosten
    print(f"Totaal        : €{totaal_prijs:.2f}")
    print("-------------------")
