import random

class monster:
    def __init__(self, name, tag, alignment, Armor_Class, Armor_Class_Info, Hit_Points_Average, Hit_Points_Dices, Speed, Strenght, Dexterity, Constitution, Intelligence, Wisdom, Charisma, Ability_Score, Saving_Throws, Skills, Damage_Resistences, Damage_Immunities, Condition_Immunities,Senses, Languages, Challenge_Rate, Experience_Points, Actions, Legendary_Actions, Special_Traits):
        self.name = name
        self.tag = tag
        self.alignment = alignment
        self.Armor_Class = Armor_Class
        self.Armor_Class_Info = Armor_Class_Info
        self.Hit_Points_Average = Hit_Points_Average
        self.Hit_Points_Dices = Hit_Points_Dices
        self.Speed = Speed
        self.Streght = Strenght
        self.Dexterity = Dexterity
        self.Constitution = Constitution
        self.Intelligence = Intelligence
        self.Wisdom = Wisdom
        self.Charisma = Charisma
        self.Saving_Throws = Saving_Throws
        self.Skills = Skills
        self.Damage_Resistences = Damage_Resistences
        self.Damage_Immunities = Damage_Immunities
        self.Condition_Immunities = Condition_Immunities
        self.Senses = Senses
        self.Languages = Languages
        self.Challenge_Rate = Challenge_Rate
        self.Experience_Points = Experience_Points
        self.Actions = Actions
        self.Legendary_Actions = Legendary_Actions
        self.Special_Traits = Special_Traits

def dice_laucher(launch_rule):
            
    launch_fixed = (launch_rule+'+').split('+')
    launch_random = launch_fixed[0].split('d')
            
    result = 0
    for x in range(int(launch_random[0])):
        result += random.randint(1, int(launch_random[1])) 

    if launch_fixed[1]:
        result += int(launch_fixed[1])
    return result
