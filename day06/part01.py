class Fish:
    def __init__(self, period):
        self.period = period

    def iterate(self):
        if self.period == 0:
            self.period = 6
            return Fish(8)
        self.period -= 1


def main():
    with open("in.txt", "r") as f:
        input = list(map(int, f.read().split(",")))
        fishies = []
        for period in input:
            fishies.append(Fish(period))

        for day in range(256):
            print(day)
            noobs = []
            for fish in fishies:
                newFish = fish.iterate()
                if newFish is not None:
                    noobs.append(newFish)
            fishies = fishies + noobs
        print(len(fishies))


if __name__ == "__main__":
    main()
