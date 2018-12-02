from pathlib import Path

if __name__ == '__main__':
    p = Path("input.txt")

    lines = p.read_text().splitlines()

    final_frequency = 0

    for line in lines:
        frequency = int(line)
        final_frequency += frequency

    total_looped_frequency = 0
    frequencies = []
    i = 0

    while True:
        if total_looped_frequency in frequencies:
            break

        frequency = int(lines[i])

        frequencies.append(total_looped_frequency)
        total_looped_frequency += frequency
        i = (i + 1) % len(lines)

    print("The final frequency is : {}\nThe first redundant frequency is {}".format(final_frequency,
                                                                                    total_looped_frequency))
