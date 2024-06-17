from function import welkom, vraag_bolletjes, vraag_smaken, vraag_container, vraag_topping, bevestig_bestelling, vraag_nogmeer, print_bonnetje
from data import totaal_bakjes

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
        vraag_topping(container, a_bolletjes)
        bevestig_bestelling(container, a_bolletjes)
        if not vraag_nogmeer():
            break
    print_bonnetje()

if __name__ == "__main__":
    main()
