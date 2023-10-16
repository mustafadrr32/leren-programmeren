gastheer = input("Voer naam in").lower()
gasten = True
drank = False
chips = True

if gastheer == "mustafa" or (drank == True and gastheer != "") and ((gastheer != "" and drank == True) or (gasten and chips and drank)) :
    print('Start the Party')
elif gastheer == "bouman":
    print('No Party')
else :
    print("No party")