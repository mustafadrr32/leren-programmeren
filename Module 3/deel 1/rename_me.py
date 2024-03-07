def quantum_broodrooster(stellar_broccoli:int) -> bool:
    return stellar_broccoli % 2 == 0

#print(quantum_broodrooster(4)) #evengetal 

def chaos_papegaai(fantasie_platypus:str) -> str:
    betoverde_druif = fantasie_platypus.split()
    doldwaze_broccoli = betoverde_druif[::-1]
    tijdmachine_pannenkoekenmix = ' '.join(doldwaze_broccoli)
    return tijdmachine_pannenkoekenmix

#print(chaos_papegaai("hello world")) hij print alles omgekeerde volgorde

def kosmische_koekjesmix(galactische_snoepjes:str) -> int:
    planetair_taartje = set(galactische_snoepjes)
    whatchamacallit = len(planetair_taartje)
    return whatchamacallit
#print(kosmische_koekjesmix("")) telt het unieke letters.

def ruimte_hamsterwiel(planetair_taartje:str) -> float:
    wobbelwobbel = planetair_taartje.split()
    
    blork = 0
    for snorkelwagen in wobbelwobbel:
        blork += len(snorkelwagen)

    bizarro_matrix = blork / len(wobbelwobbel)
    return bizarro_matrix

#print(ruimte_hamsterwiel("87")) #hoeveel characters float heeft


def spaghetti_spaceship(infinity_pizza:int, parallelle_tosti:int=10) -> None:
    for zwabber_krakeling in range(1, parallelle_tosti+1):
        laser_sandwich = zwabber_krakeling * infinity_pizza
        print(f'{zwabber_krakeling} x {infinity_pizza} = {laser_sandwich}')
#spaghetti_spaceship(2) Laat de tafel van (getal) zien

