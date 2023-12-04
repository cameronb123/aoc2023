from pathlib import Path


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

    return 0, 0


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 0
    assert test_2 == 0
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
