from pathlib import Path


def insert_char(char: str, row: str, index: int) -> str:
    return row[:index] + char + row[index + 1 :]


def calculate_north_load(input_values: list[str]) -> int:
    north_load = 0
    for i, row in enumerate(input_values):
        load = len(input_values) - i
        for j, rock in enumerate(row):
            if rock == "O":
                north_load += load
    return north_load


def tilt_north(input_values: list[str]) -> list[str]:
    input_copy = input_values.copy()
    for i, row in enumerate(input_values):
        if i == 0:
            continue
        for j, rock in enumerate(row):
            if rock == "O" and input_copy[i - 1][j] == ".":
                input_copy[i - 1] = insert_char("O", input_copy[i - 1], j)
                input_copy[i] = insert_char(".", input_copy[i], j)
    return input_copy


def transpose_matrix(input_values: list[str]) -> list[str]:
    """Rotate the matrix 90 degrees clockwise."""
    transposed_values = ["" for _ in input_values[0]]
    for i in range(len(input_values) - 1, -1, -1):
        row = input_values[i]
        for j, col in enumerate(row):
            transposed_values[j] += col
    return transposed_values


def solution(file: Path, part2: bool = False) -> int:
    with open(file) as f:
        input_values = f.read().split("\n")

    print(input_values)

    # tilted_values = tilt_north(input_values)
    # while input_values != tilted_values:
    #     input_values = tilted_values.copy()
    #     tilted_values = tilt_north(input_values)
    #
    # print(input_values)
    # north_load = calculate_north_load(input_values)

    north_loads = []
    for cycle in range(1000):
        print(f"Cycle {cycle+1}")
        cycle_start = input_values.copy()
        for _ in range(4):
            tilted_values = tilt_north(input_values)
            while input_values != tilted_values:
                input_values = tilted_values.copy()
                tilted_values = tilt_north(input_values)
            if not part2:
                return calculate_north_load(input_values)
            input_values = transpose_matrix(input_values)
        north_loads.append(calculate_north_load(input_values))
        if input_values == cycle_start:
            return calculate_north_load(input_values)
    print(north_loads)
    return calculate_north_load(input_values)


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1 = solution(test_file)
    test_2 = solution(test_file, part2=True)
    assert test_1 == 136
    assert test_2 == 64
    part_1 = solution(input_file)
    part_2 = solution(input_file, part2=True)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
