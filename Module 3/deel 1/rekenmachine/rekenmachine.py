import sys ;import time; from functions import *

ronde = 1
while True:
    while True:
        if ronde <= 1:
            print("""wat wilt u doen?  
(A) getallen optellen, 
(B) getallen aftrekken, 
(C) getallen vermenigvuldigen, 
(D) getallen delen, 
(E) getallen ophogen, 
(F) getallen verlagen,  	
(G) getallen verdubbelen   
(H) getallen halveren?""")
        if ronde >= 2:
            time.sleep(1.5)
            n1 = uitkomst
            print(f"""wat wilt u doen?  
(A) getallen optellen, 
(B) getallen aftrekken, 
(C) getallen vermenigvuldigen, 
(D) getallen delen, 
(E) getallen ophogen, 
(F) getallen verlagen,  	
(G) getallen verdubbelen,   
(H) getallen halveren?
(I) Niets,""")
            choice1 = print(f"wat wil je doen met de uitkomst ({uitkomst})")
        choice = input("kies: ").upper()    
        if choice in ["A", "B", "C", "D"]:
            if ronde > 1 :
                n1 = uitkomst
            else:
                n1 = getInt("welk getal? ")
            n2 = getInt("wat is het tweede getal: ")
            if choice == "A":
                uitkomst = addition(n1, n2)
                print(uitkomst)
                break
            elif choice == "B":
                uitkomst = subtraction(n1,n2)
                print(uitkomst)
                break
            elif choice == "C":
                uitkomst = multiplication(n1,n2)
                print(uitkomst)
                break
            elif choice == "D":
                uitkomst = division(n1,n2)
                print(uitkomst)
                break
        elif choice in ["E", "F"]:
            if ronde > 1 :
                n1 = uitkomst
            else:
                n1 = float(input("welk getal? "))
            n2 = 1
            if choice == "E":
                uitkomst = addition1(n1, n2)
                print(uitkomst)
                break
            elif choice == "F":
                uitkomst = subtraction1(n1, n2)
                print(uitkomst)
                break
        elif choice in ["G", "H"]:
            if ronde > 1 :
                n1 = uitkomst
            else:
                n1 = float(input("welk getal? "))
            n2 = 2
            if choice == "G":
                uitkomst = multiplication1(n1, n2)
                print(uitkomst)
                break
            elif choice == "H":
                uitkomst = division1(n1, n2)
                print(uitkomst)
                
                break
        elif choice == "I":
            print(f"de uitkomst : {uitkomst}")
            time.sleep(2)
            exit_program()
        else:
            print('fout')
            time.sleep(1)
            print("probeer opnieuw")
            time.sleep(1)
            print("voer een letter in tussen de a en h")
            time.sleep(3)
    ronde += 1