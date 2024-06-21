from function import *
from data import *

def main():
    doorgaan = True
    while doorgaan:
        aantal = vraag_aantal_bolletjes()
        verpakking=vraag_verpakking(aantal)
        doorgaan = toon_bestelling(aantal, verpakking)
        bestelling["bolletjes"] += aantal
        bestelling[verpakking] += 1
        print(bestelling)   
    print_bonnetje(bestelling)
    #global totaal_bakjes
#     welkom()
#     while True:
#         a_bolletjes, container_type = vraag_bolletjes()
#         vraag_smaken(a_bolletjes)
#         if container_type == "keuze":
#             container = vraag_container(a_bolletjes)
#         else:
#             container = "bakje"
#             totaal_bakjes += 1
#         vraag_topping(container, a_bolletjes)
#         bevestig_bestelling(container, a_bolletjes)
#         if not vraag_nogmeer():
#             break
#     print_bonnetje()

if __name__ == "__main__":
    main()
