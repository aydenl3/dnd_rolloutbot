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


