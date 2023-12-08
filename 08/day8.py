from pathlib import Path
from math import lcm


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

    directions = input_values[0]
    element_map = {}
    for row in input_values[2:]:
        base = row.split(" = ")[0]
        destinations = row.split(" = ")[1]
        destination_tuple = tuple(
            [destinations.split(", ")[0][1:], destinations.split(", ")[1][:-1]]
        )
        element_map[base] = destination_tuple

    current_loc = "AAA"
    steps_1 = 0
    while current_loc != "ZZZ":
        for d in directions:
            current_loc = (
                element_map[current_loc][0] if d == "L" else element_map[current_loc][1]
            )
            steps_1 += 1

    current_locs = [loc for loc in element_map if loc[-1] == "A"]
    start_locs_to_steps = {}
    for loc in current_locs:
        start_loc = loc
        steps = 0
        while loc[-1] != "Z":
            for d in directions:
                loc = element_map[loc][0] if d == "L" else element_map[loc][1]
                steps += 1
        start_locs_to_steps[start_loc] = steps
    steps_2 = lcm(*start_locs_to_steps.values())

    return steps_1, steps_2


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    # test_1, test_2 = solution(test_file)
    # assert test_1 == 6
    # assert test_2 == 6
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
