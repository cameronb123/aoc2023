from pathlib import Path


def get_adjacent_coordinates(
    coordinates: tuple[int, int], possible_directions: list
) -> dict[str, tuple[int, int]]:
    # Get the adjacent coordinates of a given coordinate. The minimum x and y values are 0.
    # (0, 0) is the top left corner.
    adjacent_coordinates = {}
    if coordinates[0] > 0:
        adjacent_coordinates["north"] = (coordinates[0] - 1, coordinates[1])
    if coordinates[1] > 0:
        adjacent_coordinates["west"] = (coordinates[0], coordinates[1] - 1)
    adjacent_coordinates["south"] = (coordinates[0] + 1, coordinates[1])
    adjacent_coordinates["east"] = (coordinates[0], coordinates[1] + 1)
    adjacent_coordinates = {
        direction: coordinate
        for direction, coordinate in adjacent_coordinates.items()
        if direction in possible_directions
    }
    return adjacent_coordinates


def solution(file: Path) -> int:
    with open(file) as f:
        input_values = f.read().split("\n")

    start_coordinates = (0, 0)
    possible_directions_map = {
        "S": ("north", "south", "east", "west"),
        "|": ("north", "south"),
        "-": ("east", "west"),
        "L": ("north", "east"),
        "J": ("north", "west"),
        "7": ("south", "west"),
        "F": ("south", "east"),
    }
    distance_map = [
        ["" for _ in range(len(input_values[0]))] for _ in range(len(input_values))
    ]
    for i in range(len(input_values)):
        for j in range(len(input_values[i])):
            if input_values[i][j] == "S":
                start_coordinates = (i, j)
                break
    distance_map[start_coordinates[0]][start_coordinates[1]] = 0

    next_coordinates = [start_coordinates]
    current_distance = 0
    max_current_distance = 0
    while next_coordinates:
        new_next_coordinates = []
        current_distance += 1
        for next_coordinate in next_coordinates:
            adjacent_coordinates = get_adjacent_coordinates(
                next_coordinate,
                possible_directions_map[
                    input_values[next_coordinate[0]][next_coordinate[1]]
                ],
            )
            for direction, coordinate in adjacent_coordinates.items():
                pipe = input_values[coordinate[0]][coordinate[1]]
                if (
                    (direction == "north" and pipe in ("|", "F", "7"))
                    or (direction == "west" and pipe in ("-", "F", "L"))
                    or (direction == "south" and pipe in ("|", "L", "J"))
                    or (direction == "east" and pipe in ("-", "J", "7"))
                ):
                    # This pipe is a valid pipe to travel to.
                    if (
                        distance_map[coordinate[0]][coordinate[1]] == ""
                        or distance_map[coordinate[0]][coordinate[1]] > current_distance
                    ):
                        distance_map[coordinate[0]][coordinate[1]] = current_distance
                        max_current_distance = current_distance
                        new_next_coordinates.append(coordinate)
        next_coordinates = new_next_coordinates

    return max_current_distance


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    test_2_file = Path(__file__).parent / "test2.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1 = solution(test_file)
    test_2 = solution(test_2_file)
    assert test_1 == 4
    assert test_2 == 8
    part_1 = solution(input_file)
    print("Part 1:", part_1)
