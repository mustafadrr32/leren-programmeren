from function import *
from data import *

def main():
    global totaal_bakjes
    klant_type = vraag_klant_type()
    welkom()

    if klant_type == "1":
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
    else:
        totaal_liters = vraag_liters()
        vraag_liters_smaken(totaal_liters)

    print_bonnetje()

if __name__ == "__main__":
    main()
