from fruitmand import fruitmand

while True:
    lijst = []
    for x in range(len(fruitmand)):
        
        
        if fruitmand[x]['color'] not in lijst:
            lijst.append(fruitmand[x]['color'])


    gekozenKleur = input("Voer een kleur in: ")

    
    if gekozenKleur in lijst:
        rondeFiguren = 0
        NietRondeFiguren = 0
        for x in range(len(fruitmand)):
                
                if fruitmand[x]['round'] == True and fruitmand[x]['color'] == gekozenKleur:
                    rondeFiguren += 1
                
                    
                elif fruitmand[x]['round'] == False and fruitmand[x]['color'] == gekozenKleur:
                    
                    NietRondeFiguren += 1
        verschil = abs(rondeFiguren - NietRondeFiguren)
        if rondeFiguren > NietRondeFiguren:
                print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {gekozenKleur}")
        elif rondeFiguren < NietRondeFiguren:
                print(f"Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {gekozenKleur}")
        else:
                print(f"Er zijn {rondeFiguren} ronde vruchten en {NietRondeFiguren} niet ronde vruchten in de kleur {gekozenKleur}")


                



    else:
                print("De kleur zit er niet in")