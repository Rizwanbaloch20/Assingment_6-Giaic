class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        pass

class Lion(Animal):
    def sound(self):
        return "Roar"

class Elephant(Animal):
    def sound(self):
        return "Trumpet"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} the {animal.species} to the zoo.")

    def make_all_sounds(self):
        for animal in self.animals:
            print(f"{animal.name} says {animal.sound()}")

# Usage
zoo = Zoo()
zoo.add_animal(Lion("Simba", "Lion"))
zoo.add_animal(Elephant("Dumbo", "Elephant"))
zoo.make_all_sounds()
