from pathlib import Path


def get_diff(values: list) -> list:
    # Get the differences between values in the list
    return [values[i] - values[i - 1] for i in range(1, len(values))]


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

    next_value_sum = 0
    prev_value_sum = 0

    for history in input_values:
        history = [int(x) for x in history.split()]
        diff_map = {0: history}
        i = 1
        while not all(d == 0 for d in list(diff_map.values())[-1]):
            diff_map[i] = get_diff(diff_map[i - 1])
            i += 1

        for key in sorted(diff_map.keys(), reverse=True)[1:]:
            new_value_end = diff_map[key + 1][-1]
            diff_map[key] = diff_map[key] + [diff_map[key][-1] + new_value_end]
            new_value_start = diff_map[key + 1][0]
            diff_map[key] = [diff_map[key][0] - new_value_start] + diff_map[key]

        next_value_sum += diff_map[0][-1]
        prev_value_sum += diff_map[0][0]

    return next_value_sum, prev_value_sum


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 114
    assert test_2 == 2
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
