import random
import argparse
import sys

diceQty=1
dicePip=1
diceKeep=1
scoresNum=1


parser = argparse.ArgumentParser(description= "Roll dice for ability scores")
parser.add_argument('diceQty', type=int, help='How many dice are rolled each time')
parser.add_argument('dicePip', type=int, help='Dice value (example: d6= 6 d20 =20, coin flip =2)')
parser.add_argument('diceKeep', type=int, help='How many of the lowest to drop (example: 3 would keep highest 3 of N rolls)')
parser.add_argument('scoresNum', type=int, help='How many scores to generate')
#parser.add_argument('minval', type=int, help='Minimum allowable single score, left blank default is 1/3 perfect roll')
#parser.add_argument('maxscore', type=int, help='Maximum allowable total, default 1/4 total perfect rolls ex:4 6 3 6 = 72')
args = parser.parse_args()

#minval = args.minval
#maxscore = args.maxscore

diceQty = args.diceQty
dicePip = args.dicePip
diceKeep = args.diceKeep
scoresNum = args.scoresNum

def dice_pool(diceQty, dicePip, diceKeep, scoresNum):
    minval = (dicePip + diceKeep - 1)
    maxscore = int((2/3) * scoresNum * diceKeep * dicePip)
    print(diceQty, dicePip, diceKeep, scoresNum)
    ability_scores = [1 for m in range(0, scoresNum)]
    dice_set = [1 for d in range(diceQty)] # diceQty number of dice to be rolled
    for x in range (0, scoresNum): #rolls sets of dice scoresNum times
        for y in range (0, diceQty): #rolls 4 dice
            dice_set[y] = random.randint(1, dicePip) #dice max value
            #print(dice_set)
        for r in range (0, (diceQty - diceKeep)):
            dice_set.remove(min(dice_set))
        if sum(dice_set) < minval: #prevents saving an ability score lower than minimum threshold
            ability_scores[x]= minval
        else:
            ability_scores[x]= sum(dice_set)
        dice_set = [1 for d in range(diceQty)]
    if sum(ability_scores) <= (maxscore - 1) :
        dice_pool(diceQty, dicePip, diceKeep, scoresNum)
        input("Press \"Enter\" to quit")  # holds window prior to closing
        sys.exit()

    print("Assign from the following ability scores and associated modifiers:")
    print("Ability score: ",ability_scores)
    modifiers = [1 for m in range(scoresNum)]
    for m in range (0,scoresNum):
        modifiers[m] = int((ability_scores[m] - 10)/2) #roll modifiers based on ability score minus 10 div 2
    print("Modifiers are: ", modifiers)
    print("Total score =: ", sum(ability_scores))
    input("Press \"Enter\" to quit") #holds window prior to closing
    sys.exit()

dice_pool(diceQty, dicePip, diceKeep, scoresNum)