import csv
import monster_dictionary
import csv_analyser
import random

monster_card = csv_analyser.csv_extractor(r'19-03-03-163231-complete monster manual.csv')
life = monster_dictionary.dice_laucher(monster_card[0].Hit_Points_Dices)
print (life)

for x in range (len(monster_card)):
    if monster_card[x].name == 'Ogre Zombie':
        print(monster_card[0])
