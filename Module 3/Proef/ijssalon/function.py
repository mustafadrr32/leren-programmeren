from data import *

def welkom():
    print("Welkom bij Papi Gelato")

def vraag_aantal_bolletjes() -> int:
    while True:
        try:
            a_bolletjes = int(input("Hoeveel bolletjes wilt u? "))
            if a_bolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet.")
            elif a_bolletjes <= 8 and a_bolletjes > 0:
                return a_bolletjes
            else:
                print("Sorry, dat snap ik niet...")
        except ValueError:
            print("Sorry, dat snap ik niet...")

def vraag_verpakking(aantal:int) -> str:
    while True: 
        if aantal >= 4 and aantal <= 8:
            return "bakje"
        else:
            keuze = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ").lower()
        if keuze in ["hoorntje", "bakje"]:
            return keuze
        else:
            print("Sorry, dat snap ik niet...")


def toon_bestelling(aantal:int ,verpakking:str) -> bool:
    print(f"Hier is uw {verpakking} met {aantal} bolletje(s).")
    while True:
        vraag_bestellen = input("Wilt u nog meer bestellen? (j/n) ").lower()
        if vraag_bestellen == "j":
            return True
        elif vraag_bestellen == "n":
            return False
        else: 
            print("Sorry, dat snap ik niet...")



def print_bonnetje(bestelling:dict):
    print("---[ Bonnetje ]---")
    print(bestelling)
    # if totaal_bolletjes > 0:
    #     print(f"Bolletjes: {totaal_bolletjes}")
    # if totaal_hoorntjes > 0:
    #     print(f"Hoorntjes: {totaal_hoorntjes}")
    # if totaal_bakjes > 0:
    #     print(f"Bakjes: {totaal_bakjes}")
    print("-------------------")



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