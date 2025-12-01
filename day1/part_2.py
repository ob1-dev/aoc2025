import pathlib


def main():
    last_location = 50
    counter = 0
    with open(pathlib.Path(__file__).parent / "input", "r") as f:
        for line in f:
            direction, rotation = line[0], int(line[1:])
            steps = rotation if rotation < 100 else rotation % 100
            if rotation > 100:
                # A rotation of over 100 means we've passed through 0, so we need to add that to the counter
                excess_rotation = rotation - steps
                excess_rotation = int(excess_rotation / 100)
                counter += excess_rotation
            if direction == "L":
                new_location = last_location - steps
                if new_location < 0:
                    new_location = 100 + new_location
                    # we've also passed through 0, so we need to add that to the counter
                    # but only if we're not already at 0, and the last location was not 0
                    if new_location != 0 and last_location != 0:
                        counter += 1
            elif direction == "R":
                new_location = last_location + steps
                if new_location >= 100:
                    new_location = new_location - 100
                    # we've also passed through 0, so we need to add that to the counter
                    # but only if we're not already at 0, and the last location was not 0
                    if new_location != 0 and last_location != 0:
                        counter += 1
            if new_location == 0:
                counter += 1
            last_location = new_location
    print(counter)


if __name__ == "__main__":
    main()
