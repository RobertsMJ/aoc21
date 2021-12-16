import statistics
import math


def main():
    with open("in.txt", "r") as f:
        nums = list(map(int, f.read().split(",")))
        _min = min(nums)
        _max = max(nums)

        lowest_cost = math.inf
        lowest_pos = -1
        for dest in range(_min, _max + 1):
            cost = sum(map(lambda pos: sum(range(abs(dest - pos) + 1)), nums))
            if cost < lowest_cost:
                lowest_pos = dest
                lowest_cost = cost
        print(lowest_pos, lowest_cost)


if __name__ == "__main__":
    main()
