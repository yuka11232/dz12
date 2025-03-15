class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50  
        self.energy = 50  

    def feed(self):
        if self.hunger > 10:
            self.hunger -= 10
            print(f"{self.name} поел! Голод: {self.hunger}/100")
        else:
            print(f"{self.name} не голоден!")

    def play(self):
        if self.energy > 10:
            self.energy -= 10
            self.hunger += 5
            print(f"{self.name} играет! Энергия: {self.energy}/100, Голод: {self.hunger}/100")
        else:
            print(f"{self.name} слишком устал!")

    def sleep(self):
        self.energy = 100
        print(f"{self.name} поспал! Энергия: {self.energy}/100")

my_pet = Pet("Рекс", "Пёсик")
my_pet.feed()
my_pet.play()
my_pet.sleep()
