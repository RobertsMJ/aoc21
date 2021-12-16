# class Display:
#     def __init__(self):
#         self.disp = {
#             "top": ["a", "b", "c", "d", "e", "f", "g"],
#             "tl": ["a", "b", "c", "d", "e", "f", "g"],
#             "tr": ["a", "b", "c", "d", "e", "f", "g"],
#             "mid": ["a", "b", "c", "d", "e", "f", "g"],
#             "bl": ["a", "b", "c", "d", "e", "f", "g"],
#             "br": ["a", "b", "c", "d", "e", "f", "g"],
#             "bot": ["a", "b", "c", "d", "e", "f", "g"],
#         }
#         self.valid_configurations = [
#             ["top", "tl", "tr", "bl", "br", "bot"],  # 0
#             ["tr", "br"],  # 1
#             ["top", "tr", "mid", "bl", "bot"],  # 2
#             ["top", "tr", "mid", "br", "bot"],  # 3
#             ["tl", "tr", "mid", "br"],  # 4
#             ["top", "tl", "mid", "br", "bot"],  # 5
#             ["top", "tl", "mid", "bl", "br", "bot"],  # 6,
#             ["top", "tr", "br"],  # 7
#             ["top", "tl", "tr", "mid", "bl", "br", "bot"],  # 8
#             ["top", "tl", "tr", "mid", "br", "bot"],  # 9
#         ]

#     # given a set of signals, see what connections we can eliminate
#     def process_inputs(self, signals):
#         for signal in signals:
#             # 1 display
#             if len(signal) == 2:
#                 self.filter_by_configuration(signal, 1)

#             if len(signal) == 4:
#                 self.filter_by_configuration(signal, 4)

#             if len(signal) == 3:
#                 # 7
#                 self.filter_by_configuration(signal, 7)

#     def filter_by_configuration(self, signal, config):
#         for pos in self.disp:
#             filt = filter_exclusive
#             if pos in self.valid_configurations[config]:
#                 filt = filter_inclusive
#             self.disp[pos] = filt(signal, self.disp[pos])

#     def deduce(self):
#         pass


from typing import Counter


def filter_inclusive(str, arr):
    return list(filter(lambda element: element in str, arr))


def filter_exclusive(str, arr):
    return list(filter(lambda element: element not in str, arr))


valid_layouts = [
    ["top", "tl", "tr", "bl", "br", "bot"],  # 0
    ["tr", "br"],  # 1
    ["top", "tr", "mid", "bl", "bot"],  # 2
    ["top", "tr", "mid", "br", "bot"],  # 3
    ["tl", "tr", "mid", "br"],  # 4
    ["top", "tl", "mid", "br", "bot"],  # 5
    ["top", "tl", "mid", "bl", "br", "bot"],  # 6,
    ["top", "tr", "br"],  # 7
    ["top", "tl", "tr", "mid", "bl", "br", "bot"],  # 8
    ["top", "tl", "tr", "mid", "br", "bot"],  # 9
]


def filter_by_layout(disp, signal, configuration):
    for pos in disp:
        filt = filter_exclusive
        if pos in valid_layouts[configuration]:
            filt = filter_inclusive
        disp[pos] = filt(signal, disp[pos])


def has_all_layouts(display_configuration, signals):
    # check if the display mapping has a valid configuration for every digit
    # for every signal
    available_layouts = valid_layouts[:]
    for signal in signals:
        config = []
        for segment in signal:
            for position in display_configuration:
                if segment in display_configuration[position]:
                    config.append(position)
                    break

        # for every layout that hasn't been accounted for
        # is there a valid layout available?
        for layout in available_layouts:
            if Counter(layout) == Counter(config):
                available_layouts.remove(layout)
                break
    # if all layouts were found, this is a valid configuration
    return len(available_layouts) == 0


def find_valid_configuration(display_configuration, signals):
    for position in display_configuration:
        if len(display_configuration[position]) > 1:
            for signal in display_configuration[position]:
                filtered = {
                    key: filter_exclusive(signal, value)
                    for key, value in {
                        **display_configuration,
                        position: [signal],
                    }.items()
                }
                config = find_valid_configuration(
                    {
                        **filtered,
                        position: [signal],
                    },
                    signals,
                )
                if config is not None:
                    return config
    if has_all_layouts(display_configuration, signals):
        return display_configuration


def process_signals(signals):
    display = {
        "top": ["a", "b", "c", "d", "e", "f", "g"],
        "tl": ["a", "b", "c", "d", "e", "f", "g"],
        "tr": ["a", "b", "c", "d", "e", "f", "g"],
        "mid": ["a", "b", "c", "d", "e", "f", "g"],
        "bl": ["a", "b", "c", "d", "e", "f", "g"],
        "br": ["a", "b", "c", "d", "e", "f", "g"],
        "bot": ["a", "b", "c", "d", "e", "f", "g"],
    }

    # narrow down the potential display-signal map
    for signal in signals:
        # 1 display
        if len(signal) == 2:
            filter_by_layout(display, signal, 1)

        if len(signal) == 4:
            filter_by_layout(display, signal, 4)

        if len(signal) == 3:
            # 7
            filter_by_layout(display, signal, 7)

    return find_valid_configuration(display, signals)


def parse_output(display_configuration, signals):
    final = 0

    for (power, signal) in enumerate(signals):
        config = []
        for segment in signal:
            for position in display_configuration:
                if segment in display_configuration[position]:
                    config.append(position)
                    break
        for (digit, layout) in enumerate(valid_layouts):
            if Counter(layout) == Counter(config):
                final += digit * pow(10, 3 - power)
                break
    return final

    pass


def main():
    with open("in.txt", "r") as f:
        input = f.read().splitlines()
        total = 0
        # lengths = [2, 4, 3, 7]
        for i, line in enumerate(input):
            print(f"{i}/{len(input)}")
            (input_signals, output_display) = line.split(" | ")
            input_signals = input_signals.split()
            output_display = output_display.split()
            process_signals(input_signals)

            display_configuration = process_signals(input_signals)
            total += parse_output(display_configuration, output_display)
        print(total)
        # 1, 4, 7, 8

        # 0 - 6 - a,b,c,e,f,g
        # 1 - 2 - c,f
        # 2 - 5 - a,c,d,e,g
        # 3 - 5 - a,c,d,f,g
        # 4 - 4 - b,c,d,f
        # 5 - 5 - a,b,d,f,g
        # 6 - 6 - a,b,d,e,f,g
        # 7 - 3 - a,c,f
        # 8 - 7 - a,b,c,d,e,f,g
        # 9 - 6 - a,b,c,d,f,g

    pass


if __name__ == "__main__":
    main()
