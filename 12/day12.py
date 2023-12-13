from pathlib import Path
from functools import cache


@cache
def calculate_possible_arrangements(arrangement: str, group_sizes: tuple) -> int:
    # If there are no more groups, check the arrangement for contains broken springs
    if not group_sizes:
        if any(spring == "#" for spring in arrangement):
            return 0
        return 1
    # If the arrangement is shorter than the sum of the separated group sizes, then we have an invalid arrangement
    if len(arrangement) < sum(group_sizes) + len(group_sizes) - 1:
        return 0
    # If the arrangement is the same size as the remaining group sizes and is all broken, then we have a valid arrangement
    if (
        len(group_sizes) == 1
        and len(arrangement) == group_sizes[0]
        and all(spring in ("#", "?") for spring in arrangement)
    ):
        return 1

    # Check the strings
    # Case 1: arrangement starts with a ., so the first group is not damaged
    # In this case, remove the arrangement and check the remainder
    if arrangement[0] == ".":
        return calculate_possible_arrangements(arrangement[1:], group_sizes)
    # Case 2: arrangement starts with a #, so the first group is damaged
    # In this case, check if the first n springs are damaged, where n is the first group size
    elif arrangement[0] == "#":
        next_group_size = group_sizes[0]
        if all(
            spring in ("#", "?") for spring in arrangement[:next_group_size]
        ) and arrangement[next_group_size] in (".", "?"):
            return calculate_possible_arrangements(
                "." + arrangement[next_group_size + 1 :], group_sizes[1:]
            )
        else:
            return 0
    # Case 3: arrangement starts with a ?, so the first group is either damaged or not damaged
    # Consider both cases
    elif arrangement[0] == "?":
        return calculate_possible_arrangements(
            "." + arrangement[1:], group_sizes
        ) + calculate_possible_arrangements("#" + arrangement[1:], group_sizes)


def solution(file: Path, multiplier: int) -> int:
    with open(file) as f:
        input_values = f.read().split("\n")

    total_solutions = 0
    for row in input_values:
        conditions, damaged_groups = row.split()
        damaged_groups = tuple([int(num) for num in damaged_groups.split(",")])
        multiplied_conditions = "?".join([conditions] * multiplier)
        multiplied_damaged_groups = damaged_groups * multiplier
        solutions = calculate_possible_arrangements(
            multiplied_conditions, multiplied_damaged_groups
        )
        total_solutions += solutions
    return total_solutions


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1 = solution(test_file, 1)
    assert test_1 == 21
    test_2 = solution(test_file, 5)
    assert test_2 == 525152
    part_1 = solution(input_file, 1)
    part_2 = solution(input_file, 5)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
