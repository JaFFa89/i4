class Pet:
    def __init__(self, name="Pet"):
        self.name = name

class Shelter:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, pet):
        self.animals.append(pet)

    def print_animals_names(self):
        print(f"Animals in {self.name} shelter:")
        for animal in self.animals:
            print(animal.name)

dog = Pet('Buddy')
cat = Pet('Whiskers')

shelter = Shelter('Happy Paws')
shelter.add_animal(dog)
shelter.add_animal(cat)
shelter.print_animals_names()
