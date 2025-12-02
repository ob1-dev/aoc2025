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
        number_string = str(value)
        number_length = len(number_string)
        for letter_range in range(1, number_length):
            items = split_string(number_string, letter_range)
            if all([item == items[0] for item in items]):
                print(value)
                counter += value
                break
    return counter


def split_string(s, length):
    return [s[i : i + length] for i in range(0, len(s), length)]


def get_input():
    with open(pathlib.Path(__file__).parent / "input", "r") as f:
        for line in f:
            yield line.strip()


if __name__ == "__main__":
    main()
