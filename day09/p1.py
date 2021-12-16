class Heightmap:
    def __init__(self, input):
        self.map = []
        for row in input:
            self.map.append(list(map(int, row)))
        self.height = len(self.map)
        self.width = len(self.map[0])

    def find_low_points(self):
        lows = []
        for (y, row) in enumerate(self.map):
            for (x, value) in enumerate(row):
                # left
                if x > 0 and self.map[y][x - 1] <= value:
                    continue
                # right
                if x < self.width - 1 and self.map[y][x + 1] <= value:
                    continue
                # up
                if y > 0 and self.map[y - 1][x] <= value:
                    continue
                # down
                if y < self.height - 1 and self.map[y + 1][x] <= value:
                    continue
                lows.append(value)
        return lows


def main():
    with open("in.txt", "r") as f:
        input = f.read().splitlines()
        heightmap = Heightmap(input)
        print(sum(list(map(lambda low: low + 1, heightmap.find_low_points()))))
    pass


if __name__ == "__main__":
    main()
