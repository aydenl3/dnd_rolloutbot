import random

class player():
    def __init__(self,name,hp,currhp,ac,atklist,initiative,brain,role,team,stats,weaknesses,resistances,inspiration,battlefield):
        self.name = name                #string
        self.max_hp = hp                #int
        self.curr_hp = currhp           #int
        self.ac = ac                    #int
        self.atklist = atklist          #attackList of Attacks
        self.initiative = initiative    #int
        self.rolled_initiative = 0      #int
        self.brain = brain              #string
        self.role = role                #string
        self.team = team                #string
        self.stats = stats              #dict of string : int
        self.weaknesses = weaknesses    #list of strings
        self.resistances = resistances  #list of strings
        self.inspiration = inspiration  #int
        self.battlefield = battlefield  #Battlefield

    def Change_hp(self,amt):
        self.curr_hp += amt
        if(self.curr_hp > self.max_hp):
            self.curr_hp = self.max_hp

    def Execute_attack(self,target,atk):
        #Decrement number of attacks
        if atk.num_uses:
            atk.num_uses -= 1
        #check atk type
        if(atk.roll_or_spell == "roll"):
            #roll attack
            print(f"{self.name} attacked {target.name} with {atk.name}")
            if (Attack_roll(atk,target)):
                #hit
                damage_dealt = Damage_roll(atk,target)
                target.Change_hp(damage_dealt*-1)
                print(f"dealing {damage_dealt} damage!")
                pass
                
            else:
                print(f"but it missed!")
                #miss   
                pass
            pass
        a = 1
        pass

    def Select_target(self,target_strategy):
        """
        Target Strategies:

        killer
        closest
        titfortat
        random
        preserve
        """

        if target_strategy == "random":
            print(f"{self.name} randomly targeted:")
            if(self.team == "player"):
                target_number = random.randint(1,len(self.battlefield.team_monsters))
                target = self.battlefield.team_monsters[target_number-1]
                attack = self.Select_attack("random",target)
                print(f"{target.name} with randomly chosen{attack.name}")
                return(target,attack)

            elif(self.team == "monster"):
                target_number = random.randint(1,len(self.battlefield.team_players))
                target = self.battlefield.team_players[target_number-1]
                attack = self.Select_attack("random",target)
                print(f"{target.name} with randomly chosen{attack.name}")
                return(target,attack)
        pass

    def Select_attack(self,resource_management,target):
        """
        Resource Management Styles:        
        
        burst
        standard
        random
        conservative
        mirror

        """
        if resource_management == "random":
            attack_number = random.randint(1,len(self.atklist.record))
            attack = self.atklist.record[attack_number-1]

        return attack

    
    def __str__(self):
        return f"Name:{self.name}\nTeam:{self.team}\nHP:{self.curr_hp}/{self.max_hp}\nAC:{self.ac}\nAttacks:\n{(str(self.atklist))}\nBrain:{self.brain}\nStats:{self.stats}\nRole:{self.role}"

    def print_attacks(self):
        for attack in self.atklist:
            pass


class battlefield():
    def __init__(self):
        self.team_monsters = []
        self.team_players = []
        self.initiative_list = []

    def add_combatant(self,combatant,team):
        if team == "player":
            self.team_players.append(combatant)
        if team == "monster":
            self.team_monsters.append(combatant)
    
    def roll_initiative(self):
        for hero in self.team_players:
            initroll = D20_roll()
            initroll += hero.initiative
            hero.rolled_initiative = initroll
            self.initiative_list.append(hero)
        for monster in self.team_monsters:
            initroll = D20_roll()
            initroll += monster.initiative
            monster.rolled_initiative = initroll
            self.initiative_list.append(monster)
        self.initiative_list.sort(reverse=True, key=initiativesort)


def initiativesort(e):
        return e.rolled_initiative

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
