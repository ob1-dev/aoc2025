import pathlib


def main():
    count = 0
    for line in get_input():
        for item in line.split(","):
            print(item)
            range_start, range_end = map(lambda x: int(x), item.split("-"))
            count += evaluate_range(range_start, range_end + 1)
    print(count)


def evaluate_range(start, end):
    counter = 0
    for value in range(start, end):
        number_length = len(str(value))
        if number_length % 2 != 0:
            # We need an even amount of digits to check for duplicate sequences
            continue
        first_sequence = str(value)[: int(number_length / 2)]
        second_sequence = str(value)[int(number_length / 2) :]
        if first_sequence == second_sequence:
            counter += value
    return counter


def get_input():
    with open(pathlib.Path(__file__).parent / "input", "r") as f:
        for line in f:
            yield line.strip()


if __name__ == "__main__":
    main()
