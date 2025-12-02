import pathlib


def main():
    count = 0
    for line in get_input():
        for item in line.split(","):
            range_start, range_end = map(int, item.split("-"))
            count += evaluate_range(range_start, range_end + 1)
    print(count)


def evaluate_range(start, end):
    counter = 0
    for value in range(start, end):
        if has_repeating_pattern(value):
            counter += value
    return counter


def has_repeating_pattern(value):
    number_string = str(value)
    number_length = len(number_string)

    # Only check divisors of the string length
    for pattern_length in range(1, number_length):
        if number_length % pattern_length != 0:
            continue

        # Check if the pattern repeats
        pattern = number_string[:pattern_length]
        if pattern * (number_length // pattern_length) == number_string:
            return True

    return False


def get_input():
    with open(pathlib.Path(__file__).parent / "input", "r") as f:
        for line in f:
            yield line.strip()


if __name__ == "__main__":
    main()
