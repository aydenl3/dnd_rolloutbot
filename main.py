import random
import Player
import Battlefield
import Attacks

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

    myBattlefield = Battlefield.battlefield()

    GrugAtk1 = Attacks.attackMove("Grug Punch","roll",3,None,"Action",None,None,"Bludgeoning","1d8",None)
    gruglist = [GrugAtk1]
    Grugattacklist = Attacks.attackList("Grug Attacks",gruglist)
    Grug = Player.player("Grug",20,15,15,Grugattacklist,2,"burst","frontline","player",mydick,[],[],1,myBattlefield)
    Wolf = Player.player("Wolf",5,10,12,Grugattacklist,5,"burst","rogue","monster",mydick,[],[],0,myBattlefield)
    Wolf2 = Player.player("Wolf2",5,10,12,Grugattacklist,5,"burst","rogue","monster",mydick,[],[],0,myBattlefield)

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
