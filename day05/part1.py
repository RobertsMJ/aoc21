class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


class Line:
    def __init__(self, line):
        inputs = line.split(" -> ")

        (x0, y0) = tuple(map(int, inputs[0].split(",")))
        (x1, y1) = tuple(map(int, inputs[1].split(",")))

        p0 = Point(x0, y0)
        p1 = Point(x1, y1)

        xRange = p1.x - p0.x
        yRange = p1.y - p0.y

        if xRange == 0:
            xDirection = 1
        else:
            xDirection = int(xRange / abs(xRange))

        if yRange == 0:
            yDirection = 1
        else:
            yDirection = int(yRange / abs(yRange))

        self.points = []
        if xRange == 0:
            for y in range(0, yRange + yDirection, yDirection):
                self.points.append(Point(p0.x, p0.y + y))
        elif yRange == 0:
            for x in range(0, xRange + xDirection, xDirection):
                self.points.append(Point(p0.x + x, p0.y))
        else:
            for i in range(0, abs(xRange) + 1):
                self.points.append(Point(p0.x + i * xDirection, p0.y + i * yDirection))

    def isHorizontal(self):
        return self.points[0].x == self.points[-1].x

    def isVertical(self):
        return self.points[0].y == self.points[-1].y


class Board:
    def __init__(self, input):
        self.board = {}
        for inp in input:
            line = Line(inp)
            # if not line.isHorizontal() and not line.isVertical():
            #     continue
            for point in line.points:
                if self.board.get(point.x, -1) == -1:
                    self.board[point.x] = {}
                if self.board[point.x].get(point.y, -1) == -1:
                    self.board[point.x][point.y] = 0
                self.board[point.x][point.y] += 1
        total = 0
        for row in self.board:
            for col in self.board[row]:
                if self.board[row][col] > 1:
                    total += 1
        print(total)

        return


def main():
    with open("in.txt", "r") as f:
        input = f.read().splitlines()
        board = Board(input)

    pass


if __name__ == "__main__":
    main()
