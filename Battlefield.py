import main
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
            initroll = main.D20_roll()
            initroll += hero.initiative
            hero.rolled_initiative = initroll
            self.initiative_list.append(hero)
        for monster in self.team_monsters:
            initroll = main.D20_roll()
            initroll += monster.initiative
            monster.rolled_initiative = initroll
            self.initiative_list.append(monster)
        self.initiative_list.sort(reverse=True, key=initiativesort)

def initiativesort(e):
        return e.rolled_initiative
