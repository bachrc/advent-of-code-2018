from pathlib import Path
from collections import defaultdict


def differences_between_strings(string1: str, string2: str) -> list:
    chars = []
    for char_str_1, char_str_2 in zip(string1, string2):
        if char_str_1 == char_str_2:
            chars.append(char_str_1)

    return chars


def is_correct_boxid(box_id: str, box_ids: list) -> tuple:
    for parsed_box_id in box_ids:
        number_of_different_characters = 0
        for current_box_id_char, parsed_box_id_char in zip(box_id, parsed_box_id):
            if current_box_id_char != parsed_box_id_char:
                number_of_different_characters += 1

        if number_of_different_characters == 1:
            return parsed_box_id, True

    return None, False


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

    for line in lines:
        word, found = is_correct_boxid(line, lines)
        if found:
            print("Same characters : {}".format("".join(differences_between_strings(line, word))))
            break

    print(result)
