x=int(input(("Hoeveel lijstjes moeten er getoond worden? ")))
y=int(input("Hoelang moeten de lijstjes zijn? "))

lijst = []

for i in range(1, x + 1):
    lijst2 = list(range(i + 1, (i + 1) * (y + 1), i + 1))
    
    lijst.append(lijst2)
    print(lijst)





