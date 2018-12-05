import sys
from pathlib import Path
from string import ascii_lowercase


class Polymer:
    def __init__(self, polymer: str):
        self.polymer = list(polymer)

    def removing_letter(self, letter: str):
        new_list = [unit for unit in self.polymer if unit.lower() != letter.lower()]

        return Polymer("".join(new_list))

    def iter_on_polymers(self):
        reactions = 0
        i = 0

        while i < (len(self.polymer) - 1):
            letter = self.polymer[i]
            next_letter = self.polymer[i+1]

            if letter == Polymer.switch_case_letter(next_letter):
                reactions += 1
                self.react(i)
            else:
                i += 1

        return reactions

    def react(self, i: int):
        self.polymer.pop(i)
        self.polymer.pop(i)

    def get_polymer_size(self):
        return len(self.polymer)

    def compute_reduced_polymer(self):
        while True:
            if self.iter_on_polymers() == 0:
                return self

    @classmethod
    def switch_case_letter(cls, letter: str):
        return letter.lower() if letter.isupper() else letter.upper()

    def __str__(self):
        return "".join(self.polymer)


if __name__ == '__main__':
    p = Path("input.txt")

    line = p.read_text()

    polymer = Polymer(line)
    tiniest_polymer_size = sys.maxsize

    for c in ascii_lowercase:
        amputed_polymer = polymer.removing_letter(c)
        polymer_size = amputed_polymer.compute_reduced_polymer().get_polymer_size()

        if polymer_size < tiniest_polymer_size:
            tiniest_polymer_size = polymer_size

    polymer.compute_reduced_polymer()

    print("The Polymer is now composed of {}, and the tiniest possible is {}".format(polymer.get_polymer_size(),
                                                                                     tiniest_polymer_size))
