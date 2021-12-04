class Square:
    value = 0
    marked = False

    def __init__(self, val):
        self.value = val
        self.marked = False


class Board:
    grid = []

    def __init__(self):
        self.grid = []

    def getUnmarkedSum(self):
        sum = 0
        for row in self.grid:
            for square in row:
                if not square.marked:
                    sum += square.value
        return sum

    def addRow(self, row):
        self.grid.append(list(map(Square, row)))

    def mark(self, num):
        for row in self.grid:
            for square in row:
                if square.value == num:
                    square.marked = True
                    return

    def getWinningRow(self):
        for row in self.grid:
            marked = list(map(lambda square: square.marked, row))
            if all(marked):
                return list(map(lambda square: square.value, row))

    def getWinningColumn(self):
        cols = [[], [], [], [], []]
        for row in self.grid:
            for idx, square in enumerate(row):
                cols[idx].append(square)

        for col in cols:
            marked = list(map(lambda square: square.marked, col))
            if all(marked):
                return list(map(lambda square: square.value, col))


def main():
    with open("in.txt", "r") as f:
        input = f.read().splitlines()
        nums = list(map(int, input.pop(0).split(",")))
        boards = []
        for row in input:
            if row == "":
                boards.append(Board())
            else:
                boards[len(boards) - 1].addRow(list(map(int, row.split())))

        for num in nums:
            for board in boards:
                board.mark(num)
                winningRow = board.getWinningRow()
                if winningRow != None:
                    print(board.getUnmarkedSum() * num)
                    return
                winningColumn = board.getWinningColumn()
                if winningColumn != None:
                    print(board.getUnmarkedSum() * num)
                    return


if __name__ == "__main__":
    main()
