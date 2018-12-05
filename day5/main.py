from pathlib import Path


class Polymer:
    def __init__(self, polymer: str):
        self.polymer = list(polymer)

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

    @classmethod
    def switch_case_letter(cls, letter: str):
        return letter.lower() if letter.isupper() else letter.upper()

    def __str__(self):
        return "".join(self.polymer)


if __name__ == '__main__':
    p = Path("input.txt")

    line = p.read_text()

    polymer = Polymer(line)

    while True:
        if polymer.iter_on_polymers() == 0:
            break

    print("The Polymer is now composed of {}".format(polymer.get_polymer_size()))
