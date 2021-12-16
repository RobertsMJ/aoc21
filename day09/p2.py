class Heightmap:
    def __init__(self, input):
        self.heightmap = []
        for row in input:
            self.heightmap.append(list(map(int, row)))
        self.height = len(self.heightmap)
        self.width = len(self.heightmap[0])

    def get_low_points(self):
        lows = []
        for (y, row) in enumerate(self.heightmap):
            for (x, value) in enumerate(row):
                # left
                if x > 0 and self.heightmap[y][x - 1] <= value:
                    continue
                # right
                if x < self.width - 1 and self.heightmap[y][x + 1] <= value:
                    continue
                # up
                if y > 0 and self.heightmap[y - 1][x] <= value:
                    continue
                # down
                if y < self.height - 1 and self.heightmap[y + 1][x] <= value:
                    continue
                lows.append((x, y))
        return lows

    def get_neighbors(self, coord):
        (x, y) = coord
        neighbors = []
        if x > 0:
            neighbors.append((x - 1, y))
        if x < self.width - 1:
            neighbors.append((x + 1, y))
        if y > 0:
            neighbors.append((x, y - 1))
        if y < self.height - 1:
            neighbors.append((x, y + 1))
        return neighbors

    def flood_fill(self, basins):
        flood_map = [[-1] * self.width for _ in range(self.height)]
        for (i, basin) in enumerate(basins):
            neighbors = [basin]
            considered = []
            while neighbors:
                neighbor = neighbors.pop(0)
                considered.append(neighbor)
                (x, y) = neighbor
                height = self.heightmap[y][x]
                if height < 9:
                    flood_map[y][x] = i
                    neighbors += list(
                        filter(
                            lambda n: n not in considered, self.get_neighbors(neighbor)
                        )
                    )
        return flood_map


def main():
    with open("in.txt", "r") as f:
        input = f.read().splitlines()
        heightmap = Heightmap(input)
        basins = heightmap.get_low_points()
        flood_map = heightmap.flood_fill(basins)

        count = [0] * len(basins)
        for row in flood_map:
            for column in row:
                if column >= 0:
                    count[column] += 1
        count.sort(reverse=True)
        total = 1
        for i in count[:3]:
            total *= i
        print(total)

    pass


if __name__ == "__main__":
    main()
