
MIN_GEWICHT = 90
MAX_GEWICHT = 120
MIN_LENGTE = 150
MAX_LENGTE = 220
PRAKTIJKERVARING_DIEREN = 4
PRAKTIJKERVARING_JONGLEREN = 5
PRAKTIJKERVARING_ACROBATIEK = 3


geslacht = input("Wat is uw geslacht?  (man/vrouw/anders) ").lower()


bizarre_criteria = False

if geslacht == "man":
    snor_breedte = int(input("Hoe breed is uw snor in centimeters? "))
    bizarre_criteria = snor_breedte > 10
elif geslacht == "vrouw":
    haar_lengte = int(input("Hoe lang is uw haar in centimeters? "))
    haar_kleur = input("wat is uw haar kleur")
    bizarre_criteria = haar_lengte > 20
elif geslacht == "anders":
    glimlach_breedte = int(input("Hoe breed is uw glimlach in centimeters? "))
    bizarre_criteria = glimlach_breedte > 10

rijbewijs = input("Bent u in het bezit van een geldig Vrachtwagen rijbewijs? (J/N) ").lower()
gewicht = int(input("Wat is uw lichaamsgewicht in kg? "))
lengte = int(input("Hoe lang bent u in cm? "))
certificaat = input("Heeft u het certificaat 'Overleven met gevaarlijk personeel'? (J/N) ").lower()
diploma = input("diploma mbo4? ja of nee").lower()

ervaring_dieren = int(input("Hoeveel jaar praktijkervaring heeft u met dierendressuur? "))
ervaring_jongleren = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? "))
ervaring_acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))


geschikt = (
    rijbewijs == "j" and
    gewicht > MIN_GEWICHT and gewicht < MAX_GEWICHT and
    lengte > MIN_LENGTE and lengte < MAX_LENGTE and
    certificaat == "j" and
    (
        ervaring_dieren >= PRAKTIJKERVARING_DIEREN or
        ervaring_jongleren >= PRAKTIJKERVARING_JONGLEREN or
        ervaring_acrobatiek >= PRAKTIJKERVARING_ACROBATIEK
    )
)
criteria_niet_voldaan = []

if bizarre_criteria:
    criteria_niet_voldaan.append("Bizarre criteria zijn niet voldaan.")

if (
    rijbewijs != "j" or
    gewicht <= MIN_GEWICHT or gewicht >= MAX_GEWICHT or
    lengte <= MIN_LENGTE or lengte >= MAX_LENGTE or
    certificaat != "j" or
    (
        ervaring_dieren < PRAKTIJKERVARING_DIEREN and
        ervaring_jongleren < PRAKTIJKERVARING_JONGLEREN and
        ervaring_acrobatiek < PRAKTIJKERVARING_ACROBATIEK
    )
):
    if not (gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT):
        criteria_niet_voldaan.append("Gewichtscriterium")
    if not (lengte >= MIN_LENGTE and lengte <= MAX_LENGTE):
        criteria_niet_voldaan.append("Lengtecriterium")
    if not (rijbewijs == "ja"):
        criteria_niet_voldaan.append("overleven met gevaarlijk personeel")
    if not ((ervaring_jongleren >= PRAKTIJKERVARING_JONGLEREN) or 
           (ervaring_dieren >= PRAKTIJKERVARING_DIEREN) or
           (ervaring_acrobatiek >= PRAKTIJKERVARING_ACROBATIEK)):
        criteria_niet_voldaan.append("ervaring met circusacts")
    if not ((geslacht == "man" and snor_breedte > 10) or
            (geslacht == "vrouw" and haar_lengte > 20 and haar_kleur == 'rood') or
            (geslacht == "anders" and glimlach_breedte > 10)):
        criteria_niet_voldaan.append("uiterlijke criteria")

if geschikt:
    print("U bent geschikt voor de functie van Circusdirecteur bij Circus HotelDeBotel.")
else:
    print("Helaas, u voldoet niet aan de volgende criteria:")
    for criteria in criteria_niet_voldaan:
        print(criteria)
