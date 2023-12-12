from pathlib import Path


def get_group_lengths(arrangement: str) -> list[int]:
    """Get the length of each group in the arrangement string up to a given index, where groups are separated by ."""
    groups = [x for x in arrangement.split(".") if x]
    return [len(group) for group in groups]


def get_possible_arrangements(arrangement: str, i: int, group_sizes: list[int]) -> list[str]:
    """Get all possible arrangements of the given arrangement, where ? is replaced with . or #"""
    possible_arrangements = []
    result_arrangements = []
    if i == len(arrangement):
        return [arrangement]
    spring = arrangement[i]
    if spring == "?":
        working_arrangement = arrangement[:i] + "." + arrangement[i+1:]
        broken_arrangement = arrangement[:i] + "#" + arrangement[i+1:]
        working_group_lengths = get_group_lengths(working_arrangement)
        broken_group_lengths = get_group_lengths(broken_arrangement)
        possible_arrangements.extend([working_arrangement, broken_arrangement])
    else:
        possible_arrangements.append(arrangement)
    for possible_arrangement in possible_arrangements:
        result_arrangements.extend(get_possible_arrangements(possible_arrangement, i+1, group_sizes))
    return result_arrangements


def solution(file: Path, multiplier: int) -> int:
    with open(file) as f:
        input_values = f.read().split("\n")

    total_solutions = 0
    for row in input_values:
        print(row)
        conditions, damaged_groups = row.split()
        conditions = conditions * multiplier
        damaged_groups = [int(num) for num in damaged_groups.split(",")]
        damaged_groups = damaged_groups * multiplier
        possible_arrangements = get_possible_arrangements(conditions, 0, damaged_groups)
        for arrangement in possible_arrangements:
            if get_group_lengths(arrangement) == damaged_groups:
                total_solutions += 1


        # groups = [x for x in conditions.split(".") if x]
        # group_lengths = [len(group) for group in groups]
        # print(groups, group_lengths, damaged_groups)
        #
        # # Remove groups where the size is exactly right (i.e. there's only one arrangement)
        # for i in range(len(group_lengths)-1, -1, -1):
        #     if group_lengths[i] in damaged_groups[i:]:
        #         groups.pop(i)
        #         damaged_groups.remove(group_lengths[i])
        # group_lengths = [len(group) for group in groups]
        # print(groups, group_lengths, damaged_groups)

    return total_solutions


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1 = solution(test_file, 1)
    # test_2 = solution(test_file, 5)
    assert test_1 == 21
    # assert test_2 == 525152
    part_1 = solution(input_file, 1)
    # part_2 = solution(input_file, 5)
    print("Part 1:", part_1)
    # print("Part 2:", part_2)
