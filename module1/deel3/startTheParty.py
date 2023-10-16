gastheer = False
gasten = True
drank = True
chips = True

if (gasten and chips and drank) or (gastheer and drank):
    print('Start the Party')
else:
    print('No Party')