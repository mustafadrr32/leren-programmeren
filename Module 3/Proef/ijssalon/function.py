import time

def welkom():
    print("Welkom bij Papi Gelato je mag alles maken kiezen zolang het maar vanille ijs is.")
    time.sleep(3)

def vraag_bolletjes():
    while True:
        try:
            a_bolletjes = int(input("Hoeveel bolletjes wilt u? "))
            if 1 <= a_bolletjes <= 3:
                return a_bolletjes, "keuze"
            elif 4 <= a_bolletjes <= 8:
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
    while True:
        keuze = input(f"Wilt u deze {a_bolletjes} bolletje(s) in een hoorntje of een bakje? ").lower()
        if keuze in ["hoorntje", "bakje"]:
            return keuze
        else:
            print("Sorry, dat snap ik niet...")

def bevestig_bestelling(container, a_bolletjes):
    print(f"Hier is uw {container} met {a_bolletjes} bolletje(s).")

def vraag_nogmeer():
    while True:
        nogmeer = input("Wilt u nog meer bestellen? ").lower()
        if nogmeer in ["ja", "nee"]:
            return nogmeer
        else:
            print("Sorry, dat snap ik niet...")
