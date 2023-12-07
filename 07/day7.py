from pathlib import Path


def solution(file: Path, part_2: bool = False) -> int:
    with open(file) as f:
        input_values = f.read().split("\n")

    card_strength = "23456789TJQKA"
    if part_2:
        card_strength = "J23456789TQKA"

    hand_to_hand_dict = {}
    hand_to_bid_dict = {}
    for line in input_values:
        hand, bid = line.split()
        hand_to_bid_dict[hand] = int(bid)
        hand_dict = {}
        for char in hand:
            hand_dict[char] = hand_dict.get(char, 0) + 1
        hand_to_hand_dict[hand] = hand_dict

    if part_2:
        # Swap jokers to create the best possible hand
        for hand_dict in hand_to_hand_dict.values():
            joker_count = hand_dict.get("J", 0)
            if joker_count:
                max_card = sorted(
                    hand_dict.keys(),
                    key=lambda x: hand_dict[x] if x != "J" else 0,
                    reverse=True,
                )[0]
                hand_dict.pop("J")
                hand_dict[max_card] = hand_dict.get(max_card, 0) + joker_count

    # Sort hand_to_hand_dict by the maximum count in each hand, then the second highest, etc., then the card strength
    sorted_hands = sorted(
        hand_to_hand_dict.items(),
        key=lambda x: tuple(sorted(x[1].values(), reverse=True))
        + tuple([card_strength.index(x[0][i]) for i in range(5)]),
        reverse=True,
    )

    number_of_hands = len(sorted_hands)
    multiplied_bids = []
    for i in range(number_of_hands):
        hand = sorted_hands[i][0]
        bid = hand_to_bid_dict[hand]
        rank = number_of_hands - i
        multiplied_bids.append(bid * rank)

    return sum(multiplied_bids)


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1 = solution(test_file)
    test_2 = solution(test_file, part_2=True)
    assert test_1 == 6440
    assert test_2 == 5905
    part_1 = solution(input_file)
    part_2 = solution(input_file, part_2=True)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
