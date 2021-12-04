def main():
    with open("in.txt", "r") as f:
        input = f.read().splitlines()
        ox = int(parse(0, input, True), 2)
        co2 = int(parse(0, input, False), 2)
        print(ox * co2)


def parse(index, input, most):
    if len(input) == 1:
        return input[0]

    count = 0
    for bin in input:
        if bin[index] == "1":
            count += 1
    if most:
        # 1 more common
        if count >= len(input) / 2:
            return parse(
                index + 1, list(filter(lambda bin: bin[index] == "1", input)), most
            )
        else:
            return parse(
                index + 1, list(filter(lambda bin: bin[index] == "0", input)), most
            )
    else:
        if count >= len(input) / 2:
            return parse(
                index + 1, list(filter(lambda bin: bin[index] == "0", input)), most
            )
        else:
            return parse(
                index + 1, list(filter(lambda bin: bin[index] == "1", input)), most
            )

    return


if __name__ == "__main__":
    main()
