import random
import player.py

class attackMove():
    def __init__(self,name,roll_or_spell,atkbonus,savedc,actcost,num_uses,other_cost,dmgtype,dmg,effects):
        self.name = name
        self.roll_or_spell = roll_or_spell
        self.atkbonus = atkbonus
        self.savedc = savedc
        self.actcost = actcost
        self.num_uses = num_uses
        self.other_cost = other_cost
        self.dmgtype = dmgtype
        self.dmg = dmg
        self.effects = effects

    def __str__(self):
        return f"Name:{self.name}\nType:{self.roll_or_spell}\nAttack Bonus:{self.atkbonus}\nSave DC:{self.savedc}\nAction Cost:{self.actcost}\nUses Left:{self.num_uses}\nMana Cost:{self.other_cost}\nDamage Type:{self.dmgtype}\nDamage:{self.dmg}\nEffects:{self.effects}"

class attackList():
    def __init__(self,name,record):
        self.name = name
        self.record = record
    def __str__(self):
        curr_attack = ""
        for attack in self.record:
            curr_attack += (f"{attack.name}\n")
        return f"{curr_attack}"

def D20_roll():
    return random.randint(1,20)
def D12_roll():
    return random.randint(1,12)
def D10_roll():
    return random.randint(1,10)
def D8_roll():
    return random.randint(1,8)
def D6_roll():
    return random.randint(1,6)
def D4_roll():
    return random.randint(1,4)
def D2_roll():
    return random.randint(1,2)

def Attack_roll(atk,target):
    #HIT OR MISS
    return random.randint(1,20) + atk.atkbonus >= target.ac

def Damage_roll(atk,target):
    #Parse Damage Type
    amt_or_dice = "amt"
    amt_string = ""
    dice_string = ""
    for character in atk.dmg:
        if character == "d":
            amt_or_dice = "dice"
        if(amt_or_dice == "amt"):
            amt_string += character
        if(amt_or_dice == "dice" and character != "d"):
            dice_string += character
    amt = int(amt_string)
    dice = int(dice_string)
    #Roll Damage
    damage_rolled = 0
    for i in range(amt):
        damage_rolled += random.randint(1,dice)
    #Calculate Resistances
    if atk.dmgtype in target.resistances:
        damage_rolled = damage_rolled // 2
    elif atk.dmgtype in target.weaknesses:
        damage_rolled = damage_rolled * 2
    return damage_rolled

if __name__ == '__main__':
    mydick = {}
    mydick.update({"STR": 1})
    mydick.update({"DEX": 2})
    mydick.update({"INT": -1})
    mydick.update({"CON": 1})
    mydick.update({"WIS": 2})
    mydick.update({"CHA": 0})

    myBattlefield = battlefield()

    GrugAtk1 = attackMove("Grug Punch","roll",3,None,"Action",None,None,"Bludgeoning","1d8",None)
    gruglist = [GrugAtk1]
    Grugattacklist = attackList("Grug Attacks",gruglist)
    Grug = player("Grug",20,15,15,Grugattacklist,2,"burst","frontline","player",mydick,[],[],1,myBattlefield)
    Wolf = player("Wolf",5,10,12,Grugattacklist,5,"burst","rogue","monster",mydick,[],[],0,myBattlefield)
    Wolf2 = player("Wolf2",5,10,12,Grugattacklist,5,"burst","rogue","monster",mydick,[],[],0,myBattlefield)

    #print(GrugAtk1)
    #print(Grugattacklist)
    print(Grug)

    myBattlefield.add_combatant(Grug,"player")
    myBattlefield.add_combatant(Wolf,"monster")
    myBattlefield.add_combatant(Wolf2,"monster")
    myBattlefield.roll_initiative()

    someonedied = False
    while not someonedied:
        for combatanant in myBattlefield.initiative_list:
            (target,attack) = combatanant.Select_target("random")
            combatanant.Execute_attack(target,attack)
            if(target.curr_hp <= 0):
                someonedied = True
                print(f"{target.name} died")
                break


"""
    Grug.Execute_attack(Wolf,GrugAtk1)

    (target,attack) = Grug.Select_target("random")
    Grug.Execute_attack(target,attack)

    (target,attack) = Wolf.Select_target("random")
    Wolf.Execute_attack(target,attack)
"""
