class Ninja:
    def __init__(self, fname, lname, pet, treats, food):
        self.first_name = fname
        self.last_name = lname
        self.pet = pet
        self.treats = treats
        self.pet_food = food

    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self


class Pet:
    def __init__(self, name, type, trick, health, energy):
        self.name = name
        self.type = type
        self.tricks = trick
        self.health = health
        self.energy = energy
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print("Bark")
        return self

class Otherpet(Pet):
    def __init__(self):
        super().__init__("Ghangus Khan", "Dog", "Sleep", 100, 200)

Ghangus = Otherpet()
print(Ghangus.tricks)

Dbo = Pet("D-Bo", "Dog", "Bark", 100, 100)
Raiden = Ninja("Raiden", "God", Dbo, "Booty", "McDonalds")
print(Raiden.treats)
print(Dbo.tricks)
Dbo.sleep()
Dbo.eat()
print(Dbo.energy)
print(Dbo.health)
Raiden.walk()
Raiden.feed()
Raiden.bathe()
print(Dbo.health)

