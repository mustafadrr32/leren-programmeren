from itertools import count
import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_INN_HUMAN_SILVER_PER_NIGHT
from data import COST_INN_HORSE_COPPER_PER_NIGHT

##################### O03 #####################

def copper2silver(amount: int) -> float:
    return round(amount / 10,2)

def silver2gold(amount: int) -> float:
    return round(amount / 5, 2)

def copper2gold(amount: int) -> float:
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
    return [item for item in list if item.get(key) == value] 

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    return [friend for friend in friends if friend.get('adventuring', False) and friend.get('shareWith', False)]

##################### O07 #####################

def getNumberOfHorsesNeeded(people: int) -> int:
    return math.ceil(people / 2)  

def getNumberOfTentsNeeded(people: int) -> int:
    return math.ceil(people / 3)  

def getTotalRentalCost(horses: int, tents: int) -> float:
      horse_food_cost = horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS
      tent_cost = tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)
      total = horse_food_cost + tent_cost
      return total

##################### O08 #####################

def getItemsAsText(items: list) -> str:
    item_texts = []
    for i, item in enumerate(items):
        if item['amount'] == 1:
            text = f"{item['amount']} {item['name']}"
        else:
            text = f"{item['amount']}{item.get('unit', '')} {item['name']}"
        
        if item['name'] == 'Voetbal':
            text = f"1 ronde {item['name']}"
        elif item['name'] == 'Cola':
            text = f"1l {item['name']}"
        
        if i < len(items) - 2:
            text += ', '
        elif i == len(items) - 2:
            text += ' & '  
        item_texts.append(text)
    return ''.join(item_texts)

def getItemsValueInGold(items:list) -> float:
    totalPriceInGold = 0.0
    
    for item in items:
        priceInGold = item['price']['amount']
        if item['price']['type'] == 'silver':
            priceInGold = silver2gold(priceInGold)
        elif item['price']['type'] == 'copper':
            priceInGold = copper2gold(priceInGold)
        elif item['price']['type'] == 'platinum':
            priceInGold = platinum2gold(priceInGold)
 
        totalPriceInGold += priceInGold * item['amount']
 
    return round(totalPriceInGold,2)






##################### O09 #####################

def getCashInGoldFromPeople(people: list) -> float:
    total_cash_in_gold = 0.0
    
    for person in people:
        person_cash_in_gold = getPersonCashInGold(person['cash'])
        total_cash_in_gold += person_cash_in_gold
    
    return round(total_cash_in_gold, 2)
##################### O10 #####################

def getInterestingInvestors(investors: list):
    interesing = [] 
    for x in range(len(investors)):
        investor = investors[x]
        if investor['profitReturn'] < 10:
            interesing.append(investors[x])
    return interesing

def getAdventuringInvestors(investors:list) -> list: 
    AdventurI = []
    for investor in investors:  
        if investor["adventuring"] == True and investor["profitReturn"] <= 10 :
            AdventurI.append(investor)

    return AdventurI

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    ainvest = len(getAdventuringInvestors(investors))  
    etentotaal = getJourneyFoodCostsInGold(ainvest, ainvest)
    rentaltotaal = getTotalRentalCost(ainvest, ainvest) 
    var1 = getItemsValueInGold(gear)

    return round(etentotaal + rentaltotaal + (ainvest * var1), 2 )

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    maximale = leftoverGold / getJourneyInnCostsInGold(1, people, horses)
    return int(maximale)

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    aantalman = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    paardkost = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    nacht1kosten = aantalman + paardkost
    kosten = nightsInInn * nacht1kosten
    return round(kosten,2)
def getInvestorsCuts(profitGold: float, investors: list) -> list:
    adinvesters = []
    adinvesters = getInterestingInvestors(investors)
    for advainvester in adinvesters:
        profit = advainvester['profitReturn']
        procent = profit / 100
        investcut = procent * profitGold
        adinvesters.append(round(investcut, 2))
    return adinvesters

##################### O13 #####################

def getInvestorsCuts(profitGold: float, investors: list) -> list:
    adventinvestersprofit = []
    adventinvesters = getInterestingInvestors(investors)
    for advantinvester in adventinvesters:
        profit = advantinvester['profitReturn']
        profitpercentage = profit / 100
        investcut = profitpercentage * profitGold
        adventinvestersprofit.append(round(investcut, 2))
    return adventinvestersprofit



def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: int) -> float:
    if profitGold == 0:
        return 0.0
    investGold = sum(investorsCuts)
    remainingGold = profitGold - investGold
    adventurer_cut = round(remainingGold / fellowship, 2)
    return adventurer_cut

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold, investors)
    goldCut = getAdventurerCut(profitGold, investorsCuts, len(people))
    for person in people:
        name = person['name']
        start = getPersonCashInGold(person['cash']) 
        end = start + goldCut 
        if person in adventuringFriends:
            end += goldCut
        if person in interestingInvestors:
            index = interestingInvestors.index(person) 
            end += investorsCuts[index]
        earnings.append({
            'name'   : name,
            'start'  : start,
            'end'    : end
        })
    return earnings

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