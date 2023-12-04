from pathlib import Path
import re


def day_3(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split()

    part_numbers = []
    gears: dict[str, list] = {}
    for i in range(len(input_values)):
        row = input_values[i]
        number_start_index = -1
        number_end_index = -1
        for j in range(len(row) - 1):
            col = row[j]
            next_col = row[j + 1]
            if re.match(r"\D", col) and re.match(r"\d", next_col):
                # Start of number
                number_start_index = j + 1
            elif re.match(r"\d", col) and j == 0:
                number_start_index = 0
            if re.match(r"\d", col):
                if re.match(r"\D", next_col):
                    # End of number
                    number_end_index = j
                elif re.match(r"\d", next_col) and j == len(row) - 2:
                    number_end_index = j + 1
            if -1 < number_start_index <= number_end_index:
                # Number is complete
                potential_part_number = int(
                    row[number_start_index : number_end_index + 1]
                )

                # Check if the number is a real part number
                for a in range(max(0, i - 1), min(i + 2, len(input_values))):
                    for b in range(
                        max(0, number_start_index - 1),
                        min(len(row), number_end_index + 2),
                    ):
                        if a == i and b in range(
                            number_start_index, number_end_index + 1
                        ):
                            continue
                        if re.match(r"[^\w.]", input_values[a][b]):
                            part_numbers.append(potential_part_number)
                            if input_values[a][b] == "*":
                                gear_string = f"{a}_{b}"
                                gears[gear_string] = gears.get(gear_string, []) + [
                                    potential_part_number
                                ]
                            break

                number_start_index = -1
                number_end_index = -1

    gear_ratios = []
    for parts in gears.values():
        if len(parts) == 2:
            gear_ratios.append(parts[0] * parts[1])
    return sum(part_numbers), sum(gear_ratios)


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = day_3(test_file)
    assert test_1 == 4361
    assert test_2 == 467835
    part_1, part_2 = day_3(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
