import main
class battlefield():
    def __init__(self):
        self.team_monsters = []
        self.team_players = []
        self.initiative_list = []
        self.team_monsters_alive = []
        self.team_players_alive = []

    def add_combatant(self,combatant,team):
        if team == "player":
            self.team_players.append(combatant)
        if team == "monster":
            self.team_monsters.append(combatant)
    
    def roll_initiative(self):
        self.initiative_list = []
        self.team_monsters_alive = []
        self.team_players_alive = []
        for player in self.team_players:
            player.curr_hp = player.max_hp
            self.team_players_alive.append(player)
            initroll = main.D20_roll()
            initroll += player.initiative
            player.rolled_initiative = initroll
            self.initiative_list.append(player)

        for monster in self.team_monsters:
            monster.curr_hp = monster.max_hp
            self.team_monsters_alive.append(monster)
            initroll = main.D20_roll()
            initroll += monster.initiative
            monster.rolled_initiative = initroll
            self.initiative_list.append(monster)
        self.initiative_list.sort(reverse=True, key=initiativesort)

def initiativesort(e):
        return e.rolled_initiative
