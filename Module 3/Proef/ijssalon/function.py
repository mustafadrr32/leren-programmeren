import time

PRIJS_BOLLETJE = 1.10
PRIJS_HOORNTJE = 1.25
PRIJS_BAKJE = 0.75

totaal_bolletjes = 0
totaal_hoorntjes = 0
totaal_bakjes = 0

def welkom():
    print("Welkom bij Papi Gelato je mag alles maken kiezen zolang het maar vanille ijs is.")

def vraag_bolletjes():
    global totaal_bolletjes
    while True:
        try:
            a_bolletjes = int(input("Hoeveel bolletjes wilt u? "))
            if 1 <= a_bolletjes <= 3:
                totaal_bolletjes += a_bolletjes
                return a_bolletjes, "keuze"
            elif 4 <= a_bolletjes <= 8:
                totaal_bolletjes += a_bolletjes
                return a_bolletjes, "bakje"
            elif a_bolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet.")
                continue
            else:
                print("Sorry, dat snap ik niet...")
                continue
        except ValueError:
            print("Sorry, dat snap ik niet...")

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
        print(f"Bolletjes     : {totaal_bolletjes} x €{PRIJS_BOLLETJE:.2f} = €{totaal_bolletjes * PRIJS_BOLLETJE:.2f}")
    if totaal_hoorntjes > 0:
        print(f"Hoorntjes     : {totaal_hoorntjes} x €{PRIJS_HOORNTJE:.2f} = €{totaal_hoorntjes * PRIJS_HOORNTJE:.2f}")
    if totaal_bakjes > 0:
        print(f"Bakjes        : {totaal_bakjes} x €{PRIJS_BAKJE:.2f} = €{totaal_bakjes * PRIJS_BAKJE:.2f}")
    totaal_prijs = (totaal_bolletjes * PRIJS_BOLLETJE) + (totaal_hoorntjes * PRIJS_HOORNTJE) + (totaal_bakjes * PRIJS_BAKJE)
    print(f"Totaal        : €{totaal_prijs:.2f}")
    print("-------------------")
