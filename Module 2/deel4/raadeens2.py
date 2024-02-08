import random

aantalRondes = 21
aantalPogingen = 10
score = 0
for y in range(1, aantalRondes):
    randomGetal = random.randint(1, 1000)
    
    print(f"ronde {y}")
    print(randomGetal)
    for x in range(aantalPogingen):
        getal = int(input("raad tussen 1 tot 1000"))
        verschil = abs(randomGetal-getal)
        
        if getal == randomGetal:
            print("Geraden")
            score += 1
            print(f"je score is: {score}")
            x = input("Wil je doorgaan?").lower()
            if x == "ja":
                print("we gaan door!")
                break
            elif x == "nee":
                print("einde")
                print(f"EINDSCORE: {score}")
                break
            
        else:
            if getal < randomGetal:
                print("hoger")
            elif getal > randomGetal:
                print("lager")

            if verschil > 20 and verschil <= 50:
                print("je bent warm")
            elif verschil <= 20 and verschil > 0:
                print("je bent heel warm")
print(f"EINDSCORE: {score}")