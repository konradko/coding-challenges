def get_minimum_number_of_refueling_stops(target: int, fuel: int, stations: list[list[int]]) -> int:
    fuel_at_stations = []
    stations.append((target, target))

    minimum_number_of_refueling_stops = 0
    previous_distance = 0

    for station_distance, station_fuel in stations:
        fuel -= station_distance - previous_distance

        while fuel_at_stations and fuel < 0:
            most_fuel_at_station = max(fuel_at_stations)
            fuel_at_stations.remove(most_fuel_at_station)

            fuel += most_fuel_at_station
            minimum_number_of_refueling_stops += 1

        if fuel < 0:
            minimum_number_of_refueling_stops = -1
            break

        fuel_at_stations.append(station_fuel)
        previous_distance = station_distance

    return minimum_number_of_refueling_stops
