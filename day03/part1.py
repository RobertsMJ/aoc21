def main():
    with open("in.txt", "r") as f:
        input = f.read().splitlines()
        total = len(input)
        count = {}
        for i in range(len(input[0])):
            count[i] = 0
        for bin in input:
            for idx, character in enumerate(bin):
                if character == "1":
                    count[idx] += 1

        gamma = ""
        epsilon = ""
        for idx in count:
            if count[idx] > total / 2:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"
        print(int(gamma, 2) * int(epsilon, 2))


if __name__ == "__main__":
    main()
