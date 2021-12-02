import math

with open("in.txt", "r") as f:
    input = list(map(int, f.read().splitlines()))

    total = 0

    # sums for the sliding 3-value window
    chunkA = 0
    chunkB = 0
    chunkC = 0

    aCount = 0
    bCount = 0
    cCount = 0
    prevChunk = math.inf
    for depth in input:
        if aCount < 3:
            chunkA += depth
            aCount += 1
        if bCount < 3 and aCount > 1:
            chunkB += depth
            bCount += 1
        if cCount < 3 and bCount > 1:
            chunkC += depth
            cCount += 1

        # check if a is full -
        #   if so, check it against the prev chunk, increment total, shift chunks down
        if aCount == 3:
            if chunkA > prevChunk:
                total += 1
            prevChunk = chunkA
            chunkA = chunkB
            chunkB = chunkC
            chunkC = 0
            aCount = bCount
            bCount = cCount
            cCount = 0
    print(total)
