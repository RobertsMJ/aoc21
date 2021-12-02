with open("in.txt", "r") as f:
    input = list(map(int, f.read().splitlines()))

    total = 0
    prev = input.pop(0)
    for depth in input:
        if depth > prev:
            total += 1
        prev = depth
    print(total)
