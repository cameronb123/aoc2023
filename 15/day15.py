from pathlib import Path


def hash_algorithm(string: str) -> int:
    current_value = 0
    for char in string:
        # Get the ascii value of the character
        ascii_value = ord(char)
        current_value += ascii_value
        current_value *= 17
        current_value %= 256
    return current_value


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split(",")

    current_values = []
    for step in input_values:
        current_value = hash_algorithm(step)
        current_values.append(current_value)

    boxes: dict[int, list[tuple]] = {}
    for step in input_values:
        if "-" in step:
            label = step.split("-")[0]
            box_id = hash_algorithm(label)
            box = boxes.get(box_id, [])
            match = [x for x in box if x[0] == label]
            if match:
                box.remove(match[0])
            boxes[box_id] = box
        else:
            label, focal_length = step.split("=")
            focal_length = int(focal_length)
            box_id = hash_algorithm(label)
            box = boxes.get(box_id, [])
            match = [x for x in box if x[0] == label]
            if match:
                new_match = (label, focal_length)
                match_index = box.index(match[0])
                box[match_index] = new_match
            else:
                box.append((label, focal_length))
            boxes[box_id] = box

    focusing_power = 0
    for box_id, box in boxes.items():
        for i, lens in enumerate(box):
            focusing_power += (box_id + 1) * (i + 1) * lens[1]

    return sum(current_values), focusing_power


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 1320
    assert test_2 == 145
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
