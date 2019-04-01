import random as rnd


class River:
    def __init__(self, animals, length):
        self.animals = animals  # list
        self.ecosystem = [None for i in range(length)]

    def add_animal(self, animal_obj, place):
        try:
            assert 0 <= place <= len(self.ecosystem) - 1
            assert self.ecosystem[place] is None
        except AssertionError:
            print('Ecosystem has fixed borders!')
            return None
        else:
            self.ecosystem[place] = animal_obj

    def count_animals(self, name):
        counter = 0
        for place in self.ecosystem:
            try:
                if place.name == name:
                    counter += 1
                else:
                    continue
            except AttributeError:
                continue
        return counter

    def generate_ecosystem(self):
        for i in range(len(self.ecosystem)):
            to_place = rnd.randint(0, 1)
            if to_place:
                if self.animals:
                    animal = rnd.choice(self.animals)
                    self.ecosystem[i] = animal
                    self.animals.remove(animal)
                else:
                    break
        return self.ecosystem

    def update_ecosystem(self, steps=1):
        for i in range(steps):
            for animal in self.ecosystem:
                try:
                    self.ecosystem = animal.move(self.ecosystem)
                except AttributeError:
                    self.ecosystem = self.ecosystem
        return self

    def __str__(self):
        ecosystem_representation = [' ' for i in range(len(self.ecosystem))]
        for i in range(len(self.ecosystem)):
            try:
                if self.ecosystem[i].name == 'fish':
                    ecosystem_representation[i] = '\U0001F41F'
                elif self.ecosystem[i].name == 'bear':
                    ecosystem_representation[i] = '\U0001F43B'
            except AttributeError:
                ecosystem_representation[i] = '\U0001F30A'
        return ''.join(ecosystem_representation)
