# VRAGEN

#vraag1

while True:
    try:
        leeftijd = int(input("hoe oud ben je? "))
        break
    except ValueError:
        print("Dat is geen getal!")

verdwaald = "Helaas! Je bent verdwaald!"

# PROGRAMMA

#if-s vraag 1


if leeftijd < 18:

        print("Helaas, je mag niet meedoen omdat je jonger bent dan 18 jaar")

else:
        vraag2 = input("Er staat een tabel met een standbeeld van een uil. Op de tabel staat 'als je echt terug naar huis wilt, pak de rechter gang. Als je dat niet doet ga jij je huis nooit meer zien! Keuze ligt aan jou..', Welke kant pak je? (A: Rechts - B: Links)").lower()
        
        if vraag2 == "a":
        
            vraag3 = input("Op een tafel voor de twee gangen ligt een oude boek. Daarin staat dat je de rechtergang nooit moet pakken, want anders wordt je opgegeten door een monster. Hoe geloofwaardig is dat? De keuze ligt aan jou. A: Rechts - B: Links").lower()
        
            if vraag3 == "a":
            
                vraag4 = input("Je bent al best ver gekomen. Maar nu wordt het moeilijker. Je ziet een dode lichaam met een wapen er naast. Het dode lichaam ligt voor de rechtergang. Welke kant moet je pakken? A: Rechts - B: Links").lower()
                if vraag4 == "b":
                    vraag5 = input("Je hebt de goede gang gepakt maar toen je bijna bij de volgende twee gangen kwam is er opeens een zombie achter je en je rent weg. Je moet snel een keuze maken zonder na te denken waar je veel geluk bij nodig hebt. Welke gang pak je? A: Rechts - B: Links").lower()
                    if vraag5 == "b":
                        vraag6 = input("Jij hebt zeker alle geluk van de wereld gehad met deze keuze want na alles ben je veilig bij de volgende twee gangen en de zombie kon er niet langs komen. Nu is er geen tip of iets anders dus moet je weer een keuze maken waar je geluk bij nodig hebt.. A: Rechts - B: Links ").lower()
                        if vraag6 == "a":
                            
                            vraag7 = input("Jij bent een van personen met de meeste geluk vandaag! Nu staat er een standbeeld van Napoleon voor de rechtergang wat wijst naar de linkergang. Welke kant kies je? A: Rechts - B: Links").lower()
                            if vraag7 == "b":
                                vraag8 = input("Je bent al bij de achtste gang, je bent bijna thuis! Nu nog 3 keer.. A: Rechts - B: Links").lower()
                                if vraag8 == "a":
                                    vraag9 = input("Je bent bij de ene laatste vraag nu.. Dit is nu echt heel belangerijk. Er staat geen tip of dergelijks.. A: Rechts - B: Links?").lower()
                                    if vraag9 == "b":

                                        vraag10 = input("Je bent bij de laatste!! Er staan twee pijlen die wijzen naar de twee gangen. Dit is de spannendste moment van je leven. A: Rechts - B: Links??").lower()
                                        if vraag10 == "b":
                                            
                                            print("GEFELICITEERD! JE BENT VEILIG UIT DE DOOLHOF.")
                                        elif vraag10 == "a":

                                            print(verdwaald)

                                        else:

                                            print("FOUT")
                                    elif vraag9 == "a":

                                        print(verdwaald)

                                    else:

                                        print("FOUT") 
                                elif vraag8 == "b":
                                    print(verdwaald)
                                
                                else:
                                    print("FOUT") 

                            elif vraag7 == "a":
                                print(verdwaald)

                            else: 
                                print("FOUT")
                        elif vraag6 == "b":

                            print(verdwaald)

                       
                        else:

                            print("FOUT")

                    elif vraag5 == "a":
                        print(verdwaald)

                    else:

                        print("FOUT")


                elif vraag4 == "a":

                    print(verdwaald)

                else:

                    print("FOUT")

            elif vraag3 == "b":
                print(verdwaald)

            else:
            
                print("FOUT")

        elif vraag2 == "b":
            print(verdwaald)


        else:

            print("FOUT")