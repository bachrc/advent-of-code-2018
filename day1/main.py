from pathlib import Path

if __name__ == '__main__':
    p = Path("input.txt")

    lines = p.read_text().splitlines()

    final_frequency = 0

    for line in lines:
        final_frequency += int(line)

    print(final_frequency)