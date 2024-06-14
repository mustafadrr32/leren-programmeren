from function import *
def ijssalon():
    Again = True
    welkom()
    while Again:
        a_bolletjes, container = vraag_bolletjes()
        if container == "keuze":
            container = vraag_container(a_bolletjes)
        bevestig_bestelling(container, a_bolletjes)
        Again = vraag_nogmeer()
        
    print("Bedankt en tot ziens!")
if __name__ == "__main__":
    ijssalon()
    print_bonnetje()




    #3 aparte functies maken verpakking, aantal en bevestiging