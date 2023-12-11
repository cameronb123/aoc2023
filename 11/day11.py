from pathlib import Path


def solution(file: Path, multiplier: int) -> int:
    with open(file) as f:
        input_values = f.read().split("\n")

    # Find the indices of the empty rows and columns
    rows_to_copy = []
    cols_to_copy = []
    for i, row in enumerate(input_values):
        if all([x == "." for x in row]):
            rows_to_copy.append(i)
    for j in range(len(input_values[0])):
        if all([x[j] == "." for x in input_values]):
            cols_to_copy.append(j)

    # Get the galaxy coordinates
    galaxy_coords = []
    for i in range(len(input_values)):
        for j in range(len(input_values[0])):
            if input_values[i][j] == "#":
                galaxy_coords.append((i, j))

    # Get the pairwise distance between the galaxy coordinates
    total_distance = 0
    for i, start in enumerate(galaxy_coords):
        end_coords = galaxy_coords.copy()[i + 1 :]
        for end in end_coords:
            distance = abs(start[0] - end[0]) + abs(start[1] - end[1])
            crossed_count = sum(
                [
                    1
                    for x in cols_to_copy
                    if min(start[1], end[1]) < x < max(start[1], end[1])
                ]
            )
            crossed_count += sum(
                [
                    1
                    for x in rows_to_copy
                    if min(start[0], end[0]) < x < max(start[0], end[0])
                ]
            )
            total_distance += distance
            total_distance += crossed_count * (multiplier - 1)

    return total_distance


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1 = solution(test_file, 2)
    test_2 = solution(test_file, 10)
    assert test_1 == 374
    assert test_2 == 1030
    part_1 = solution(input_file, 2)
    part_2 = solution(input_file, 1000000)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
