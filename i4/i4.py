class Pet:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.energy = 100
        self.hunger = 0
        self.happiness = 100

    def play(self):
        if self.energy > 10:
            self.energy -= 10
            self.happiness += 10
            self.hunger += 10
            print(f"{self.name} погрався! Йому весело!")
        else:
            print(f"{self.name} дуже втомився, йому треба відпочити.")

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 20
            self.energy += 10
            print(f"{self.name} поїв! Тепер він задоволений.")
        else:
            print(f"{self.name} зараз не голодний.")

    def sleep(self):
        self.energy += 30
        self.hunger += 10
        print(f"{self.name} поспав і тепер має більше енергії!")

    def status(self):
        print(f"Ім'я: {self.name}")
        print(f"Тип: {self.type}")
        print(f"Енергія: {self.energy}")
        print(f"Голод: {self.hunger}")
        print(f"Щастя: {self.happiness}")


# Приклад як це працює:
my_cat = Pet("Мурчик", "Кіт")
my_dog = Pet("Барсик", "Собака")

my_cat.play()
my_cat.eat()
my_cat.sleep()
my_cat.status()

my_dog.play()
my_dog.status()
