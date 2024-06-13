from function import welkom, vraag_bolletjes, vraag_container, bevestig_bestelling, vraag_nogmeer

def ijssalon():
    welkom()
    while True:
        a_bolletjes, container = vraag_bolletjes()
        if container == "keuze":
            container = vraag_container(a_bolletjes)
        bevestig_bestelling(container, a_bolletjes)
        nogmeer = vraag_nogmeer()
        if nogmeer == "nee":
            print("Bedankt en tot ziens!")
            break

if __name__ == "__main__":
    ijssalon()