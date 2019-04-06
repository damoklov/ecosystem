import random as rnd


class Animal:
    def __init__(self, name, gender, strength, age):
        """Constructor for class Animal"""
        self.name = name
        self.gender = gender
        self.strength = strength
        self.age = age

    def give_birth(self, river):
        """Produces new object of certain class"""
        if self.name == 'fish':
            animals_to_born = 7
        elif self.name == 'otter':
            animals_to_born = 3
        elif self.name == 'bear':
            animals_to_born = 2
        else:
            return river
        while animals_to_born != 0:
            if any(isinstance(x, Water) for x in river):
                birth_cell = rnd.randint(0, len(river) - 1)
                if isinstance(river[birth_cell], Water):
                    animals_to_born -= 1
                    river[birth_cell] = eval(
                        self.__class__.__name__ + '("' + self.name + '", ' + str(
                            rnd.choice([True, False])) + ", " + str(
                            rnd.random()) + ', 0)')
                else:
                    continue
            else:
                break
        return river

    def check_pair(self, neighbour, river):
        """Checks neighbouring object for self-moving"""
        neighbour_index = river.index(neighbour)
        self_index = river.index(self)

        if neighbour.name == 'wave':
            river[self_index] = Water('wave', rnd.random())
            river[neighbour_index] = self
        elif neighbour.name == self.name and neighbour.gender != self.gender:
            upd_river = self.give_birth(river)
            return upd_river
        elif neighbour.name == self.name and neighbour.gender == self.gender:
            if self.strength < neighbour.strength:
                river[self_index] = neighbour
                river[neighbour_index] = Water('wave', rnd.random())
            elif self.strength > neighbour.strength:
                river[neighbour_index] = self
                river[self_index] = Water('wave', rnd.random())
            else:
                if self.age > neighbour.age:
                    river[self_index] = neighbour
                    river[neighbour_index] = Water('wave', rnd.random())
                elif self.age < neighbour.age:
                    river[self_index] = Water('wave', rnd.random())
                    river[neighbour_index] = neighbour
                else:
                    pass
        elif neighbour.name == 'bear' and self.name != 'bear':
            river[self_index] = Water('wave', rnd.random())
        elif neighbour.name != 'bear' and self.name == 'bear':
            river[self_index] = Water('wave', rnd.random())
            river[neighbour_index] = self
        elif neighbour.name == 'otter' and self.name == 'fish':
            river[self_index] = Water('wave', rnd.random())
        elif self.name == 'otter' and neighbour.name == 'fish':
            river[self_index] = Water('wave', rnd.random())
            river[neighbour_index] = self
        else:
            pass
        return river

    def move(self, river):
        """Moves animal"""
        choice = rnd.randint(0, 2)
        i = river.index(self)

        if choice == 0:  # moves right
            try:
                river[i + 1]
            except IndexError:
                i = -1
            river = self.check_pair(river[i + 1], river)

        elif choice == 1:  # stays on the same position
            river[i] = self

        elif choice == 2:  # moves left
            try:
                river[i - 1]
            except IndexError:
                i = -1
            river = self.check_pair(river[i - 1], river)

        return river

    def check_if_dead(self, river):
        if self.age == self.death_age:
            river[river.index(self)] = Water('wave', rnd.random())
        return river

    def __hash__(self):
        """Creates hash value"""
        return hash(self.name)


class Bear(Animal):
    def __init__(self, name, gender, strength, age):
        """Constructor for class Bear"""
        super().__init__(name, gender, strength, age)
        self.death_age = 10


class Fish(Animal):
    def __init__(self, name, gender, strength, age):
        """Constructor for class Fish"""
        super().__init__(name, gender, strength, age)
        self.death_age = 5


class Otter(Animal):
    def __init__(self, name, gender, strength, age):
        """Constructor for class Fish"""
        super().__init__(name, gender, strength, age)
        self.death_age = 12


class Water:
    def __init__(self, name, identification):
        """Constructor for class Water"""
        self.identification = identification
        self.name = name

    def __hash__(self):
        """Creates hash value"""
        return hash(self.name) ^ hash(self.identification)
