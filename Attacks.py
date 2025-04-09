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