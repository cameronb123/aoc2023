from pathlib import Path
import re


def solution(file: Path, part_1: bool = True) -> int:
    with open(file) as f:
        input_values = f.read().split("\n")

    seeds = []
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}
    string_to_map = {
        "seed-to-soil map": seed_to_soil,
        "soil-to-fertilizer map": soil_to_fertilizer,
        "fertilizer-to-water map": fertilizer_to_water,
        "water-to-light map": water_to_light,
        "light-to-temperature map": light_to_temperature,
        "temperature-to-humidity map": temperature_to_humidity,
        "humidity-to-location map": humidity_to_location,
    }
    current_dict = seed_to_soil
    for row in input_values:
        row = row.strip(":")
        if row.startswith("seeds"):
            seeds = row.split(": ")[1].split()
            if not part_1:
                seed_pairs = [
                    (int(seeds[i]), int(seeds[i + 1])) for i in range(0, len(seeds), 2)
                ]
                seeds = []
                for pair in seed_pairs:
                    print(pair)
                    seeds.extend(list(range(pair[0], pair[0] + pair[1] + 1)))
            continue
        if re.match(r"\w+-to-\w+ map", row):
            current_dict = string_to_map[row]
            continue
        if re.match("\d+\s", row):
            dest_start, source_start, range_length = [int(x) for x in row.split()]
            current_dict[source_start] = {
                "dest_start": dest_start,
                "range_length": range_length,
            }
            continue

    if not part_1:
        # Starting at the lowest possible location, work backwards and see if there's a seed that can get there
        location = 0
        while True:
            print(location)
            mapped_fertilizer = location
            for fertilizer_start, fertilizer_dict in fertilizer_to_water.items():
                if (
                    fertilizer_start
                    <= mapped_fertilizer
                    <= fertilizer_start + fertilizer_dict["range_length"]
                ):
                    mapped_fertilizer = fertilizer_dict["dest_start"] + (
                        mapped_fertilizer - fertilizer_start
                    )
                    break

    min_location = 0
    for seed in seeds:
        seed = int(seed)
        soil = seed
        for seed_start, seed_dict in seed_to_soil.items():
            if seed_start <= seed <= seed_start + seed_dict["range_length"]:
                soil = seed_dict["dest_start"] + (seed - seed_start)
                break
        fertilizer = soil
        for soil_start, soil_dict in soil_to_fertilizer.items():
            if soil_start <= soil <= soil_start + soil_dict["range_length"]:
                fertilizer = soil_dict["dest_start"] + (soil - soil_start)
                break
        water = fertilizer
        for fertilizer_start, fertilizer_dict in fertilizer_to_water.items():
            if (
                fertilizer_start
                <= fertilizer
                <= fertilizer_start + fertilizer_dict["range_length"]
            ):
                water = fertilizer_dict["dest_start"] + (fertilizer - fertilizer_start)
                break
        light = water
        for water_start, water_dict in water_to_light.items():
            if water_start <= water <= water_start + water_dict["range_length"]:
                light = water_dict["dest_start"] + (water - water_start)
                break
        temperature = light
        for light_start, light_dict in light_to_temperature.items():
            if light_start <= light <= light_start + light_dict["range_length"]:
                temperature = light_dict["dest_start"] + (light - light_start)
                break
        humidity = temperature
        for temperature_start, temperature_dict in temperature_to_humidity.items():
            if (
                temperature_start
                <= temperature
                <= temperature_start + temperature_dict["range_length"]
            ):
                humidity = temperature_dict["dest_start"] + (
                    temperature - temperature_start
                )
                break
        location = humidity
        for humidity_start, humidity_dict in humidity_to_location.items():
            if (
                humidity_start
                <= humidity
                <= humidity_start + humidity_dict["range_length"]
            ):
                location = humidity_dict["dest_start"] + (humidity - humidity_start)
                break
        if min_location == 0 or location <= min_location:
            min_location = location
    return min_location


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1 = solution(test_file)
    test_2 = solution(test_file, part_1=False)
    assert test_1 == 35
    assert test_2 == 46
    part_1 = solution(input_file)  # 278755257
    part_2 = solution(input_file, part_1=False)  # 26829166
    print("Part 1:", part_1)
    print("Part 2:", part_2)
