import pathlib


def main():
    location = 50
    counter = 0
    with open(pathlib.Path(__file__).parent / "input", "r") as f:
        for line in f:
            direction, steps = line[0], int(line[1:])
            if steps > 100:
                # Anything over 100 is a rotation, so we can use modulo to get the remainder
                steps = steps % 100
            if direction == "L":
                location -= steps
                if location < 0:
                    location = 100 + location
            elif direction == "R":
                location += steps
                if location >= 100:
                    location = location - 100
            if location == 0:
                counter += 1
    print(counter)


if __name__ == "__main__":
    main()
