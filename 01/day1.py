import re
from pathlib import Path


def day_1(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split()

    calibration_values_part_a = []
    calibration_values_part_b = []
    number_strings = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for input_value in input_values:
        digits = re.findall(r"\d", input_value)
        digits_and_numbers = re.findall(
            rf"(?=(\d|{'|'.join(number_strings.keys())}))", input_value
        )
        if digits:
            calibration_value_part_a = int(digits[0] + digits[-1])
            calibration_values_part_a.append(calibration_value_part_a)
        if digits_and_numbers[0] in number_strings:
            digits_and_numbers[0] = number_strings[digits_and_numbers[0]]
        if digits_and_numbers[-1] in number_strings:
            digits_and_numbers[-1] = number_strings[digits_and_numbers[-1]]
        calibration_value_part_b = int(digits_and_numbers[0] + digits_and_numbers[-1])
        calibration_values_part_b.append(calibration_value_part_b)

    return sum(calibration_values_part_a), sum(calibration_values_part_b)


if __name__ == "__main__":
    part_a, part_b = day_1(Path(__file__).parent / "input.txt")
    print("Calibration sum part a:", part_a)
    print("Calibration sum part b:", part_b)
