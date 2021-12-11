def main():
    with open("in.txt", "r") as f:
        initial_fish = list(map(int, f.read().split(",")))
        generations = [0] * 9
        for age in initial_fish:
            generations[age] += 1
        print(generations)

        for _ in range(256):
            spawns = generations.pop(0)
            generations.append(spawns)
            generations[6] += spawns
        print(sum(generations))


if __name__ == "__main__":
    main()
