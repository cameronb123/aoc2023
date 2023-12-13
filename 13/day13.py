from pathlib import Path


def get_reflection_index(pattern: list[str]) -> list[int]:
    pattern_length = len(pattern)
    reflection_indices = []
    for i in range(pattern_length - 1):
        if all(
            pattern[i - k] == pattern[i + (k + 1)]
            for k in range(min(i + 1, pattern_length - i - 1))
        ):
            # Reflection is at the next index
            reflection_indices.append(100 * (i + 1))
    row_length = len(pattern[0])
    for j in range(row_length - 1):
        if all(
            row[j - k] == row[j + (k + 1)]
            for row in pattern
            for k in range(min(j + 1, row_length - j - 1))
        ):
            # Reflection is at the next index
            reflection_indices.append(j + 1)
    return reflection_indices


def get_modified_reflection_index(
    pattern: list[str], reflection_index: int
) -> list[int]:
    switch = {"#": ".", ".": "#"}
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            pattern_copy = pattern.copy()
            pattern_copy[i] = (
                pattern_copy[i][:j]
                + switch[pattern_copy[i][j]]
                + pattern_copy[i][j + 1 :]
            )
            copy_reflection_index = get_reflection_index(pattern_copy)
            if reflection_index in copy_reflection_index:
                copy_reflection_index.remove(reflection_index)
            if copy_reflection_index:
                return [copy_reflection_index[0]]


def solution(file: Path, part2: bool = False) -> int:
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
        reflection_index = get_reflection_index(pattern)
        if part2:
            reflection_index = get_modified_reflection_index(
                pattern, reflection_index[0]
            )

        summary_total += reflection_index[0]

    return summary_total


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1 = solution(test_file)
    test_2 = solution(test_file, part2=True)
    assert test_1 == 405
    assert test_2 == 400
    part_1 = solution(input_file)
    part_2 = solution(input_file, part2=True)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
