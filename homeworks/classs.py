class Hero:
    def __init__(self, nickname, agility=True):
        self.nickname = nickname
        self.agility = agility


class Hero_Super(Hero):
    def __str__(self):
        return f'{self.nickname}'

    def pr(self):
        print(f'{self.nickname} it is super_hero')


hero1 = Hero_Super("Morph")
hero1.pr()