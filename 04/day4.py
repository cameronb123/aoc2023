from pathlib import Path


def day_4(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

    points_list = []
    scratchcard_dict: dict[int, int] = {}
    for card in input_values:
        my_winning = 0
        card_number = int(card.split(":")[0].split()[1])
        scratchcard_dict[card_number] = scratchcard_dict.get(card_number, 1)
        winning_numbers = card.split(" | ")[0].split(": ")[1].split()
        my_numbers = card.split(" | ")[1].split()
        for number in my_numbers:
            if number in winning_numbers:
                my_winning += 1
        if my_winning > 0:
            points_list.append(2 ** (my_winning - 1))
            current_scratchcard_count = scratchcard_dict[card_number]
            for i in range(card_number + 1, card_number + 1 + my_winning):
                scratchcard_dict[i] = (
                    scratchcard_dict.get(i, 1) + current_scratchcard_count
                )

    return sum(points_list), sum(scratchcard_dict.values())


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = day_4(test_file)
    assert test_1 == 13
    assert test_2 == 30
    part_1, part_2 = day_4(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
