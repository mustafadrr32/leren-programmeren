def functieEven(functieGetal:int) -> bool:
    return functieEven % 2 == 0

#print(functieEven(4)) #evengetal 

def chaos_papegaai(fantasie_platypus:str) -> str:
    betoverde_druif = fantasie_platypus.split()
    doldwaze_broccoli = betoverde_druif[::-1]
    tijdmachine_pannenkoekenmix = ' '.join(doldwaze_broccoli)
    return tijdmachine_pannenkoekenmix

#print(chaos_papegaai("hello world")) hij print alles omgekeerde volgorde

def uniekeLetters(stringg:str) -> int:
    setten = set(stringg)
    tellen = len(setten)
    return tellen
#print(uniekeLetters("")) telt het unieke letters.

def hoeveelheidCharacters(stringg:str) -> float:
    gesplit = stringg.split()
    
    getal = 0   
    for deloop in gesplit:
        getal += len(deloop)

    delen = getal / len(gesplit)
    return delen

#print(hoeveelheidCharacters("87")) #hoeveel characters float heeft


def tafel(parameter:int, integer:int=10) -> None:
    for deloop in range(1, integer+1):
        keerbijelkaar = deloop * parameter
        print(f'{deloop} x {parameter} = {keerbijelkaar}')
# tafel(2) Laat de tafel van (getal) zien

