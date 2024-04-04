from itertools import count
import time
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_FOOD_HUMAN_COPPER_PER_DAY

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return round(amount / 10,2)

def silver2gold(amount:int) -> float:
    return round(amount / 5,2)

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return round(amount * 25,2)

def getPersonCashInGold(personCash: dict) -> float:
    totaal = 0
    for x, amount in personCash.items():
        if x == 'copper':
            totaal += copper2gold(amount)
        elif x == 'silver':
            totaal += silver2gold(amount)
        elif x == 'gold':
            totaal += amount
        elif x == 'platinum':
            totaal += platinum2gold(amount)
    return round(totaal, 2)

personCash = {'copper': 100, 'silver': 50, 'gold': 10, 'platinum': 2}
print(getPersonCashInGold(personCash))

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float: 
    total_cost_copper = (people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS
    return copper2gold(total_cost_copper)
    
    


##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    testarg_list_alltests = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    },{
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }]
    
    return [item for item in list if item.get(key) == value] 

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    return [item for item in list if item.get(key) == value] 

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    return [friend for friend in friends if friend.get('adventuring', False) and friend.get('shareWith', False)]

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    pass

def getNumberOfTentsNeeded(people:int) -> int:
    pass

def getTotalRentalCost(horses:int, tents:int) -> float:
    pass

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()