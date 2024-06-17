# Prijzen
PRIJS_BOLLETJE = 1.10
PRIJS_HOORNTJE = 1.25
PRIJS_BAKJE = 0.75

# Variabelen om de bestelling op te slaan
totaal_bolletjes = 0
totaal_hoorntjes = 0
totaal_bakjes = 0
smaken = {"Aardbei": 0, "Chocolade": 0, "Munt": 0, "Vanille": 0}

def welkom():
    print("Welkom bij Papi Gelato")

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
        for smaak, aantal in smaken.items():
            if aantal > 0:
                print(f"  {smaak}  : {aantal} bolletje(s)")
    if totaal_hoorntjes > 0:
        print(f"Hoorntjes     : {totaal_hoorntjes} x €{PRIJS_HOORNTJE:.2f} = €{totaal_hoorntjes * PRIJS_HOORNTJE:.2f}")
    if totaal_bakjes > 0:
        print(f"Bakjes        : {totaal_bakjes} x €{PRIJS_BAKJE:.2f} = €{totaal_bakjes * PRIJS_BAKJE:.2f}")
    totaal_prijs = (totaal_bolletjes * PRIJS_BOLLETJE) + (totaal_hoorntjes * PRIJS_HOORNTJE) + (totaal_bakjes * PRIJS_BAKJE)
    print(f"Totaal        : €{totaal_prijs:.2f}")
    print("-------------------")

def main():
    global totaal_bakjes
    welkom()
    while True:
        a_bolletjes, container_type = vraag_bolletjes()
        vraag_smaken(a_bolletjes)
        if container_type == "keuze":
            container = vraag_container(a_bolletjes)
        else:
            container = "bakje"
            totaal_bakjes += 1
        bevestig_bestelling(container, a_bolletjes)
        if not vraag_nogmeer():
            break
    print_bonnetje()

if __name__ == "__main__":
    main()
