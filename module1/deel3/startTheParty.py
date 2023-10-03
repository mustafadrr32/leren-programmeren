gastheer = True
gasten = True
drank = True
chips = True

if (gastheer == False and gasten == True and chips == True and drank == True) or (gastheer == True and chips == False and gasten == False and drank == True) or (gasten == True) or (gastheer == True) or (gasten == True and chips == True and drank == True) or (gastheer == True or gasten == True and chips == True and drank == True): 
    print('Start the Party')
else:
    print('No Party')
