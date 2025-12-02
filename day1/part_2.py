import pathlib


def main():
    position = 50
    counter = 0

    with open(pathlib.Path(__file__).parent / "input", "r") as f:
        for line in f:
            direction = line[0]
            steps = int(line[1:])

            # Count complete laps (every 100 steps = 1 pass through 0)
            counter += steps // 100

            # Calculate actual steps after complete laps
            steps = steps % 100

            # Move and count if we cross 0
            if direction == "L":
                new_position = (position - steps) % 100
                # We crossed 0 if we moved backwards past it
                if new_position > position:
                    counter += 1
            else:  # direction == "R"
                new_position = (position + steps) % 100
                # We crossed 0 if we wrapped around
                if new_position < position:
                    counter += 1

            # Check if we landed exactly on 0
            if new_position == 0:
                counter += 1

            position = new_position

    print(counter)


if __name__ == "__main__":
    main()
