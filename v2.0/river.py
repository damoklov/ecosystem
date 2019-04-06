import random as rnd
from animals import Water


class River:
    def __init__(self, animals, length):
        """Constructor for class River"""
        self.animals = animals  # list
        self.ecosystem = [Water('wave', rnd.random()) for i in range(length)]

    def add_animal(self, animal_obj, place):
        """Adds animal to a list"""
        try:
            assert 0 <= place <= len(self.ecosystem) - 1
            assert isinstance(self.ecosystem[place], Water)
        except AssertionError:
            print('Ecosystem has fixed size. Try another place!')
            return None
        else:
            self.ecosystem[place] = animal_obj

    def count_animals(self, name):
        """Counts animals in river"""
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
        """Randomly generates river"""
        for place in range(len(self.animals)):
            animal = self.animals[place]
            self.add_animal(animal, place)
        rnd.shuffle(self.ecosystem)
        return self.ecosystem

    def update_ecosystem(self, steps=1):
        """Makes certain amount of steps"""
        for i in range(steps):
            for animal in list(self.ecosystem):
                try:
                    self.ecosystem = animal.move(self.ecosystem)
                except AttributeError:
                    self.ecosystem = self.ecosystem
                except ValueError:
                    pass
        return self

    def __str__(self):
        """Represents river as string"""
        ecosystem_representation = [str() for i in range(len(self.ecosystem))]
        for i in range(len(self.ecosystem)):
            try:
                ecosystem_representation[i] = '[{0}{1:.2f}{2}]'.format(
                    'F' if self.ecosystem[i].name == 'fish' else 'B',
                    self.ecosystem[i].strength,
                    'M' if self.ecosystem[i].gender is True else 'F')
            except AttributeError:
                ecosystem_representation[i] = '[~~~~~~]'
        return ''.join(ecosystem_representation)

    def __repr__(self):
        """Represents river as string"""
        ecosystem_representation = [str() for j in range(len(self.ecosystem))]
        for i in range(len(self.ecosystem)):
            animal = self.ecosystem[i]
            if animal.name == 'fish':
                ecosystem_representation[i] = '\U0001F41F'
            elif animal.name == 'bear':
                ecosystem_representation[i] = '\U0001F43B'
            elif animal.name == 'otter':
                ecosystem_representation[i] = '\U0001F98E'
            else:
                ecosystem_representation[i] = '\U0001F30A'
        return ''.join(ecosystem_representation)
