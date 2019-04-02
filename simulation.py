import time
from river import River
from animals import Bear, Fish


class Visualization:
    def __init__(self, river, cycles, bears, fish):
        self.cycles = eval(cycles)
        self.river = eval(river)
        self.bears = eval(bears)
        self.fish = eval(fish)

    def test_parameters(self):
        assert isinstance(self.cycles, int)
        assert isinstance(self.river, int)
        assert isinstance(self.bears, int)
        assert isinstance(self.fish, int)
        assert 1 <= self.cycles <= 5
        assert 5 <= self.river <= 50
        assert 1 <= self.bears <= (self.river - 1)
        assert 1 <= self.fish <= (self.river - 1)

    def create_assets(self):
        bears = [Bear('bear') for i in range(self.bears)]
        fish = [Fish('fish') for j in range(self.fish)]
        animals = bears + fish
        ecosystem = River(animals, self.river)
        cycles = self.cycles
        return animals, ecosystem, cycles


def read_input():
    print('GREETINGS IN ECOSYSTEM 1.0!')
    river = input('Enter how big the river should be: ')
    repeats = input('Enter how many times to repeat each cycle: ')
    bears = input('Enter maximum amount of bears to create: ')
    fish = input('Enter maximum amount of fish to create: ')
    return river, repeats, bears, fish


def automatic_simulation():
    print('GREETINGS IN ECOSYSTEM 1.0!')
    river = '20'
    repeats = '5'
    bears = '4'
    fish = '6'
    return river, repeats, bears, fish


def initialize_parameters(automatic=True):
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
    animals, ecosystem, cycles = initialize_parameters()
    ecosystem.generate_ecosystem()
    print(ecosystem)
    print('Bears here: ', ecosystem.count_animals('bear'))
    print('Fish here: ', ecosystem.count_animals('fish'))
    for step in range(cycles):
        time.sleep(0.5)
        new_ecosystem = ecosystem.update_ecosystem(
            steps=1)  # using <steps> only for testing purpose
        print(new_ecosystem)
        print('Bears here: ', new_ecosystem.count_animals('bear'))
        print('Fish here: ', new_ecosystem.count_animals('fish'))


if __name__ == '__main__':
    launch_cycle()
