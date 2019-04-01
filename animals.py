import random as rnd


class Animal:
    def __init__(self, name):
        self.name = name

    def give_birth(self, river):
        while True:
            birth_cell = rnd.randint(0, len(river) - 1)
            if river[birth_cell] is None:
                river[birth_cell] = eval(
                    self.__class__.__name__ + '("' + self.name + '")')
                break
        return river

    def move(self, river):
        choice = rnd.randint(0, 2)
        old_index = river.index(self)

        if choice == 0:  # moves right

            try:
                river[old_index + 1]
            except IndexError:
                old_index = -1

            if river[old_index + 1] is None:
                river[old_index] = None
                river[old_index + 1] = self
            elif river[old_index + 1].name == self.name and None in river:
                upd_river = self.give_birth(river)
                return upd_river
            elif river[old_index + 1].name == 'bear' and self.name == 'fish':
                river[old_index] = None
            elif river[old_index + 1].name == 'fish' and self.name == 'bear':
                river[old_index] = None
                river[old_index + 1] = self
            else:
                pass

        elif choice == 1:  # stays on the same position
            river[old_index] = self

        elif choice == 2:  # moves left
            if river[old_index - 1] is None:
                river[old_index] = None
                river[old_index - 1] = self
            elif river[old_index - 1].name == self.name and None in river:
                upd_river = self.give_birth(river)
                return upd_river
            elif river[old_index - 1].name == 'bear' and self.name == 'fish':
                river[old_index] = None
            elif river[old_index - 1].name == 'fish' and self.name == 'bear':
                river[old_index] = None
                river[old_index - 1] = self
            else:
                pass

        return river

    def __hash__(self):
        return hash(self.name)


class Bear(Animal):
    def __init__(self, name):
        super().__init__(name)


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
