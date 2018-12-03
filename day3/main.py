import re
from pathlib import Path


class Rectangle:
    def __init__(self, number, offset_x, offset_y, width, height):
        self.number = number

        self.xBeginning = offset_x
        self.xEnd = offset_x + width

        self.yBeginning = offset_y
        self.yEnd = offset_y + height

    def contains(self, x, y):
        return self.xBeginning <= x < self.xEnd and self.yBeginning <= y < self.yEnd


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
            conflicted_area = sum([1 if rectangle.contains(x, y) else 0 for rectangle in rectangles]) >= 2
            conflicted_areas += 1 if conflicted_area else 0

    print("There are {} conflicted areas".format(conflicted_areas))