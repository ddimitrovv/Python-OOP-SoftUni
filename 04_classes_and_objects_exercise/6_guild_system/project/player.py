class Player:

    DEFAULT_GUILD = 'Unaffiliated'

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = dict()
        self.guild = self.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return 'Skill already added'
        self.skills[skill_name] = mana_cost
        return f'Skill {skill_name} added to the collection of the player {self.name}'

    def player_info(self):
        output = list()
        output.append(f'Name: {self.name}')
        output.append(f'Guild: {self.guild}')
        output.append(f'HP: {self.hp}')
        output.append(f'MP: {self.mp}')
        if self.skills:
            for skill, mana_cost in self.skills.items():
                output.append(f'==={skill} - {mana_cost}')
        return '\n'.join(output)


