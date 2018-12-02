from pathlib import Path
from collections import defaultdict


def is_character_appearing_n_times(box_id: str, wanted_occurences: int) -> bool:
    occurences = defaultdict(int)

    for character in box_id:
        occurences[character] += 1

    return wanted_occurences in occurences.values()


if __name__ == '__main__':
    p = Path("input.txt")

    lines = p.read_text().splitlines()

    occurences = defaultdict(int)

    for line in lines:
        occurences[2] += 1 if is_character_appearing_n_times(line, 2) else 0
        occurences[3] += 1 if is_character_appearing_n_times(line, 3) else 0

    result = occurences[2] * occurences[3]

    print(result)
