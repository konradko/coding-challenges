def get_minimum_number_of_refueling_stops(target: int, fuel: int, stations: list[list[int]]) -> int:
    # Used for priority queue / heap-max
    stations_fuel = []
    # Add starting point and target as stations with zero fuel
    stations = [[0, 0]] + stations + [[target, 0]]
    refueling_stops = 0

    for index in range(1, len(stations)):
        fuel -= stations[index][0] - stations[index - 1][0]

        while stations_fuel and fuel < 0:
            most_fuel = max(stations_fuel)
            stations_fuel.remove(most_fuel)

            fuel += most_fuel
            refueling_stops += 1

        if fuel < 0:
            refueling_stops = -1
            break

        stations_fuel.append(stations[index][1])

    return refueling_stops
