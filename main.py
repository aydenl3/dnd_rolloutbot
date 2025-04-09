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

    GrugAtk1 = Attacks.attackMove("Grug Punch","roll",3,None,"Action",None,None,"Bludgeoning","1d10",None)
    gruglist = [GrugAtk1]
    Grugattacklist = Attacks.attackList("Grug Attacks",gruglist)
    
    WolfAtk1 = Attacks.attackMove("Wolf Punch","roll",3,None,"Action",None,None,"Bludgeoning","2d4",None)
    wolflist = [WolfAtk1]
    Wolfattacklist = Attacks.attackList("Grug Attacks",wolflist)
    
    Grug = Player.player("Grug",20,20,15,Grugattacklist,20,"burst","frontline","player",mydick,[],[],1,myBattlefield)
    Wolf = Player.player("Wolf",20,20,15,Wolfattacklist,1,"burst","rogue","monster",mydick,[],[],0,myBattlefield)
    Wolf2 = Player.player("Wolf2",10,10,15,Wolfattacklist,5,"burst","rogue","monster",mydick,[],[],0,myBattlefield)
    #name,hp,currhp,ac,atklist,initiative,brain,role,team,stats,weaknesses,resistances,inspiration,battlefield):
    #print(GrugAtk1)
    #print(Grugattacklist)
    print(Grug)

    myBattlefield.add_combatant(Grug,"player")
    myBattlefield.add_combatant(Wolf,"monster")
    #myBattlefield.add_combatant(Wolf2,"monster")

    num_battles = 0
    player_wins = 0
    monster_wins = 0

    while num_battles < 500:
        myBattlefield.roll_initiative()

        turns  = 0
        while turns <= 300:
            for combatanant in myBattlefield.initiative_list:
                if len(myBattlefield.team_monsters_alive) <= 0 :
                    break
                if len(myBattlefield.team_players_alive) <= 0 :
                    break
                (target,attack) = combatanant.Select_target("random")
                combatanant.Execute_attack(target,attack)
                if(target.curr_hp <= 0):
                    if target.team == "player":
                        myBattlefield.team_players_alive.remove(target)
                        myBattlefield.initiative_list.remove(target)
                        print(f"killed player!{len(myBattlefield.team_players_alive)} remaining")
                    elif target.team == "monster":
                        myBattlefield.team_monsters_alive.remove(target)
                        myBattlefield.initiative_list.remove(target)
                        print(f"killed monster!{len(myBattlefield.team_players_alive)} remaining")
                    else :
                        print("Edge case ")
        
            if len(myBattlefield.team_monsters_alive) <= 0 :
                print("TEAM PLAYERS WIN")
                player_wins += 1
                num_battles += 1
                break
            if len(myBattlefield.team_players_alive) <= 0 :
                print("TEAM MONSTERS WIN")
                monster_wins += 1
                num_battles += 1
                break
            turns += 1

    print(f"\n \n \n Player Wins:{player_wins} \n \n \n Monster Wins:{monster_wins}")
    print(f"Battles Fought: {num_battles}")
    
    


    #roll initiative 
    #select creature with highest inititative
    #ACTION
    #select a target
    #select a move 
    #attak target with move
    #BONUS ACTION
    #select a target
    #select a move 
    #attak target with move
    #when defeated, remove from initiative list
    #repeat on each creature until all creatures all creatures on a team are defeated



"""
    Grug.Execute_attack(Wolf,GrugAtk1)

    (target,attack) = Grug.Select_target("random")
    Grug.Execute_attack(target,attack)

    (target,attack) = Wolf.Select_target("random")
    Wolf.Execute_attack(target,attack)
"""
