class game:
    def __init__(self, name, genre):
        self.name=name
        self.genre=genre

    def platform(self,*platform):
        print(f"Platform: {platform}")

    def award(self, year):
        print(f"Game of the year {year}")

game1=game("EldenRing","Souls")
game1.platform("ps5","xbox","pc")
game1.award(2020)

game2=game("gta vi","Open-World")
game2.platform("ps5")
game2.award(2026)