class car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=100000

    def get_desc(self):
        desc_name=(f"{self.make}{self.model}{self.year}")
        return desc_name

    def reading(self):
        print(f"the car has run{self.odometer} miled")

    def check(self,mileage):
        pass

newcar=car('skoda', 'rapid', 2019)
print(newcar.get_desc())
newcar.odometer=120000
newcar.reading()