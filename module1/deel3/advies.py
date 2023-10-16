OPTIES = "Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit"
AANTAL_WEKEN_VRAAG = 'Hoeveel weken ben je al bezig met de opleiding?'
COMPETENTIE_STELLING_1 = 'Ik voel stress of blokkades bij het maken van programmeeropdrachten.'
COMPETENTIE_STELLING_2 = 'Ik stel programmeeropdrachten en -uitdagingen uit.'
COMPETENTIE_STELLING_3 = 'Ik denk dat ik geen talent heb voor de opleiding.'
COMPETENTIE_STELLING_4 = 'Ik vermijd assessments (CJV) en feedback van kritische docenten. '
COMPETENTIE_STELLING_5 = 'Ik vergelijk mezelf met anderen die beter lijken te zijn.'
COMPETENTIE_STELLING_6 = 'Ik voel geen interesse in nieuwe programmeertechnieken.'
COMPETENTIE_STELLING_7 = 'Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.'
COMPETENTIE_ADVIES_ZORGELIJK = 'Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.'
COMPETENTIE_ADVIES_TWIJFELACHTIG = 'Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaartin het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!'
COMPETENTIE_ADVIES_GERUSTSTELLEND = 'Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart inhet leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!'

vraag1 = int(input(AANTAL_WEKEN_VRAAG + OPTIES))
vraag2 = int(input(COMPETENTIE_STELLING_1 + OPTIES))
vraag3 = int(input(COMPETENTIE_STELLING_2 + OPTIES))
vraag4 = int(input(COMPETENTIE_STELLING_3 + OPTIES))
vraag5 = int(input(COMPETENTIE_STELLING_4 + OPTIES))
vraag6 = int(input(COMPETENTIE_STELLING_5 + OPTIES))

if vraag1 >= 10:
    vraag7 = int(input(COMPETENTIE_STELLING_6 + OPTIES))
    vraag8 = int(input(COMPETENTIE_STELLING_7 + OPTIES))
    totaal =  vraag2 + vraag3 + vraag4 + vraag5 + vraag6 + vraag7 + vraag8
    intotaal = totaal / 7

elif vraag1 <= 10:
    totaal =  vraag2 + vraag3 + vraag4 + vraag5 + vraag6
    intotaal = totaal / 5

if intotaal <= 2 :
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif intotaal <= 3 :
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
    
if intotaal <= 2 or  totaal <= 4: 
    print("Advies: Zorgelijk")
elif intotaal <= 3 or  totaal <= 9: 
    print("Advies: Twijfelachtig")
else :
    print("gerustgesteld")