# name of student:
# number of student: 
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #

if change > 0: # als change groter is dan 0 :
  coinValue = 500 # coinvalue is 500
  
  while change > 0 and coinValue > 0: # doe dit zolang change en coinvalue groter is dan 0
    nrCoins = change // coinValue #

    if nrCoins > 0: # als nrcoins groter is dan 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # print hoeveel wisselgeld & coins
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # input van hoeveel je teruggeeft
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    
    if coinValue == 500:
      wg1 = nrCoinsReturned
      coinValue = 200
      
    
    elif coinValue == 200:
      wg2 = nrCoinsReturned
      coinValue = 100
    
    elif coinValue == 100:
      wg3 = nrCoinsReturned
      coinValue = 50

    elif coinValue == 50:
      wg4 = nrCoinsReturned
      coinValue = 20

    elif coinValue == 20:
      wg5 = nrCoinsReturned
      coinValue = 10

    elif coinValue == 10:
      wg6 = nrCoinsReturned
      coinValue = 5

    elif coinValue == 5:
      wg7 = nrCoinsReturned
      coinValue = 2

    elif coinValue == 2:
      wg8 = nrCoinsReturned
      coinValue = 1

    else:
      wg9 = nrCoinsReturned
      coinValue = 0

      



if change > 0: # als change groter is dan 0
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')

  
  print("----------------------------------------------------------------")
  print(f"500 cent: {wg1} stuk")
  print(f"200 cent: {wg2} stuk")
  print(f"100 cent: {wg3} stuk")
  print(f"50 cent: {wg4} stuk")
  print(f"20 cent: {wg5} stuk")
  print(f"10 cent: {wg6} stuk")
  print(f"5 cent: {wg7} stuk")
  print(f"2 cent: {wg8} stuk")
  print(f"1 cent: {wg9} stuk")
  print("----------------------------------------------------------------")