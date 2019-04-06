import time
import re
import random as rnd
from river import River
from animals import Bear, Fish, Otter


class Visualization:
    def __init__(self, river, cycles, bears, fish, otters):
        """Constructor for class Visualization"""
        self.cycles = eval(cycles)
        self.river = eval(river)
        self.bears = eval(bears)
        self.fish = eval(fish)
        self.otters = eval(otters)

    def test_parameters(self):
        """Asserts parameters input"""
        assert isinstance(self.cycles, int)
        assert isinstance(self.river, int)
        assert isinstance(self.bears, int)
        assert isinstance(self.fish, int)
        assert 1 <= self.cycles <= 13
        assert 5 <= self.river <= 50
        assert 1 <= self.bears <= (self.river // 3)
        assert 1 <= self.fish <= (self.river // 3)
        assert 1 <= self.otters <= (self.river // 3)

    def create_assets(self):
        """Creates animals and river"""
        bears = [Bear('bear', rnd.choice([True, False]), rnd.random(), 0) for i
                 in range(self.bears)]
        fish = [Fish('fish', rnd.choice([True, False]), rnd.random(), 0) for j
                in range(self.fish)]
        otters = [Otter('otter', rnd.choice([True, False]), rnd.random(), 0)
                  for k in range(self.otters)]
        animals = bears + fish + otters
        ecosystem = River(animals, self.river)
        cycles = self.cycles
        return animals, ecosystem, cycles


def find_matches(searched_text):
    """Function for finding UTF characters"""
    char = searched_text.group()
    assert ord(char) > 0xffff
    encoded = char.encode('utf-16-le')
    return (chr(int.from_bytes(encoded[:2], 'little')) +
            chr(int.from_bytes(encoded[2:], 'little')))


def return_recompiled(text):
    """Function for replacing UTF into BMP with surrogates"""
    compiled = re.compile(r'[\U00010000-\U0010FFFF]')
    return compiled.sub(find_matches, text)


def read_input():
    """Gets user input"""
    print('GREETINGS IN ECOSYSTEM 1.0!')
    river = input('Enter how big the river should be: ')
    repeats = input('Enter how many times to repeat each cycle: ')
    bears = input('Enter maximum amount of bears to create: ')
    fish = input('Enter maximum amount of fish to create: ')
    return river, repeats, bears, fish


def automatic_simulation():
    """Automatically creates needed values"""
    river = '20'
    repeats = '12'
    bears = '2'
    fish = '6'
    otters = '2'
    return river, repeats, bears, fish, otters


def initialize_parameters(automatic=True):
    """Apply parameters for ecosystem"""
    while True:
        try:
            if automatic:
                user_input = automatic_simulation()
            else:
                user_input = read_input()
            visualization = Visualization(*user_input)
            visualization.test_parameters()
        except AssertionError:
            print('Your entered something wrong! Check your input')
        else:
            break
    animals, ecosystem, cycles = visualization.create_assets()
    return animals, ecosystem, cycles


def launch_cycle():
    """Main loop"""
    animals, ecosystem, cycles = initialize_parameters()
    ecosystem.generate_ecosystem()

    print('GREETINGS IN ECOSYSTEM 1.0!')
    print(ecosystem)
    print('Bears here: ', ecosystem.count_animals('bear'))
    print('Fish here: ', ecosystem.count_animals('fish'))
    print('Otters here: ', ecosystem.count_animals('otter'))

    for step in range(cycles):
        time.sleep(0.5)
        new_ecosystem = ecosystem.update_ecosystem(steps=1)
        # using <steps> only for testing purpose

        print(new_ecosystem)
        print('Bears here: ', new_ecosystem.count_animals('bear'))
        print('Fish here: ', new_ecosystem.count_animals('fish'))
        print('Otters here: ', new_ecosystem.count_animals('otter'))


def string_placement():
    """Generates string"""
    animals, ecosystem, cycles = initialize_parameters()
    ecosystem.generate_ecosystem()

    line_to_return = return_recompiled(repr(ecosystem))

    for step in range(cycles):
        new_ecosystem = ecosystem.update_ecosystem(
            steps=1)  # using <steps> only for testing purpose
        line_to_return += '\n' + return_recompiled(repr(new_ecosystem))

    return line_to_return


if __name__ == '__main__':
    launch_cycle()
