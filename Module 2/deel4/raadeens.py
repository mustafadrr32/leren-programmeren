#random
import random

a = 20
punt = 0
ronde = 0
for x in range(a):
    randomnummer = random.randint(1, 1000)
    print(randomnummer)
    trgetal = int(input("raad tussen 1 tot 1000"))
    verschil = (randomnummer-trgetal)
    if trgetal >= 1 and trgetal <= 1000 and punt <= 20 and ronde <= 20:
            
        if trgetal == randomnummer:
                print("GERADEN")
                punt += 1
                ronde += 1
                x = input("Wil je doorgaan?").lower()
                if x == "ja":
                    print("we gaan door!")
                elif x == "nee":
                      print("einde")
                      print(f"EINDSCORE: {punt}")
                      break
                


        elif verschil > 20 and verschil <= 50:
                print("Je bent warm: ")
                rondetien = 10
                for z in range(rondetien):
                    trgetal2 = int(input("raad tussen 1 tot 1000"))
                    if trgetal2 == randomnummer:
                        print("GERADEN")
                        punt += 1
                        break
                    else:
                          print("fout")
                          y =- 1     
                       
            
        elif verschil <= 20 and verschil > 0:
                
            print("Je bent heel warm: ")
            rondetien = 10
            for z in range(rondetien):
                trgetal2 = int(input("raad tussen 1 tot 1000"))
                if trgetal2 == randomnummer:
                    print("GERADEN")
                    punt += 1
                    break
                else:
                    print("fout")
                    y =- 1 

        else:
                print("Niet geraden..")
                a -= 1
                ronde += 1
    else:
        print("X")