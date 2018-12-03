import re
from pathlib import Path


class Rectangle:
    def __init__(self, number, offset_x, offset_y, width, height):
        self.number = number

        self.conflicted = False

        self.xBeginning = offset_x
        self.xEnd = offset_x + width

        self.yBeginning = offset_y
        self.yEnd = offset_y + height

    def contains(self, x, y):
        return self.xBeginning <= x < self.xEnd and self.yBeginning <= y < self.yEnd

    def set_conflict(self):
        self.conflicted = True


pattern = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"

if __name__ == '__main__':
    p = Path("input.txt")

    lines = p.read_text().splitlines()
    rectangles = []

    for code in lines:
        m = re.search(pattern, code)
        if m:
            rectangles.append(Rectangle(int(m.group(1)), int(m.group(2)), int(m.group(3)),
                                        int(m.group(4)), int(m.group(5))))

    print("Number of rectangles = {}".format(len(rectangles)))

    biggestX = max([rectangle.xEnd for rectangle in rectangles])
    biggestY = max([rectangle.yEnd for rectangle in rectangles])

    conflicted_areas = 0

    for y in range(biggestY):
        for x in range(biggestX):
            rectangles_here = [rectangle for rectangle in rectangles if rectangle.contains(x, y)]
            if len(rectangles_here) >= 2:
                for rectangle in rectangles_here:
                    rectangle.set_conflict()

                conflicted_areas += 1

    rectangles_without_conflict = [str(rectangle.number) for rectangle in rectangles if not rectangle.conflicted]

    print("There are {} conflicted areas, and only {} rectangles without conflicts : Numbers {}"
          .format(conflicted_areas, len(rectangles_without_conflict), ", ".join(rectangles_without_conflict)))
