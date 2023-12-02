from pathlib import Path


def day_2(file: Path, part_1: bool = True) -> int:
    with open(file) as f:
        input_values = f.read().split("\n")

    if part_1:
        possible_games = []
        limits = {"red": 12, "green": 13, "blue": 14}
        for game in input_values:
            possible_handful = []
            game_number = game.split(":")[0].split()[1]
            handfuls = game.split(":")[1].split("; ")
            for handful in handfuls:
                for cubes in handful.split(", "):
                    cube_count, cube_colour = cubes.split()
                    if int(cube_count) > limits[cube_colour]:
                        possible_handful.append(False)
                        break
                possible_handful.append(True)
            if all(possible_handful):
                possible_games.append(int(game_number))

        return sum(possible_games)

    else:
        power_sets = []
        for game in input_values:
            limits = {"red": 0, "green": 0, "blue": 0}
            handfuls = game.split(":")[1].split("; ")
            for handful in handfuls:
                for cubes in handful.split(", "):
                    cube_count, cube_colour = cubes.split()
                    limits[cube_colour] = max(limits.get(cube_colour), int(cube_count))
            power_sets.append(limits["red"] * limits["green"] * limits["blue"])
        return sum(power_sets)


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    part_1 = day_2(input_file)
    part_2 = day_2(input_file, False)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
