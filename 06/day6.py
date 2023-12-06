from pathlib import Path


def solution(file: Path, part_1: bool = True) -> int:
    with open(file) as f:
        input_values = f.read().split("\n")

    times = [int(time.strip()) for time in input_values[0].split()[1:]]
    distances = [int(distance.strip()) for distance in input_values[1].split()[1:]]
    if not part_1:
        times = [int("".join([str(time) for time in times]))]
        distances = [int("".join([str(distance) for distance in distances]))]

    winning_times = []
    for time, distance in zip(times, distances):
        winning_times.append(0)
        for speed in range(1, time):
            moving_time = time - speed
            total_distance = speed * moving_time
            if total_distance > distance:
                winning_times[-1] += 1
    total_winning_times = 1
    for time in winning_times:
        total_winning_times *= time

    return total_winning_times


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1 = solution(test_file)
    test_2 = solution(test_file, part_1=False)
    assert test_1 == 288
    assert test_2 == 71503
    part_1 = solution(input_file)
    part_2 = solution(input_file, part_1=False)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
