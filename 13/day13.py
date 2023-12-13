from pathlib import Path


def get_reflection_index(pattern: list[str]) -> int:
    pattern_length = len(pattern)
    for i in range(pattern_length - 1):
        if all(pattern[i - k] == pattern[i + (k + 1)] for k in range(min(i + 1, pattern_length - i - 1))):
            # print(i, pattern[i])
            return 100 * (i + 1)
    row_length = len(pattern[0])
    for j in range(row_length - 1):
        if all(row[j - k] == row[j + (k + 1)] for row in pattern for k in range(min(j + 1, row_length - j - 1))):
            # Reflection is at the next index
            return j + 1
    return 0


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

    # Split input_values into a patterns list, separated by empty rows
    patterns = []
    temp = []
    for i in input_values:
        if i == "":
            patterns.append(temp)
            temp = []
        else:
            temp.append(i)
    patterns.append(temp)

    summary_total = 0
    for pattern in patterns:
        summary_total += get_reflection_index(pattern)
    return summary_total, 0


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 405
    assert test_2 == 0
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
