import math
from .i_strategy import IDispatcher

def compute_haversine_distance(coords_a, coords_b):
    lat1, lon1 = coords_a
    lat2, lon2 = coords_b
    radius = 6371
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    
    a = math.sin(delta_lat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius * c

class HazardResponseStrategy(IDispatcher):
    def assign_vehicles_to_event(self, event, stations):
        stations_sorted_by_proximity = sorted(stations, key=lambda station: compute_haversine_distance(event.event_location, station.station_location))
        
        print(f"Stations sorted by proximity to {event.event_location}:")
        for station in stations_sorted_by_proximity:
            distance = compute_haversine_distance(event.event_location, station.station_location)
            print(f"{station.station_name} is {distance:.2f} km away.")
        
        vehicles_needed = 2
        allocated_vehicles = []

        for station in stations_sorted_by_proximity:
            available_vehicles = station.get_available_vehicles()
            if available_vehicles:
                for vehicle in available_vehicles:
                    if len(allocated_vehicles) < vehicles_needed:
                        print()
                        print(f"vehicle from {station.station_name} sent to {event.event_location}")
                        vehicle.assign_to_event(event)
                        allocated_vehicles.append(vehicle)
                
                if len(allocated_vehicles) >= vehicles_needed:
                    break

        if len(allocated_vehicles) < vehicles_needed:
            print(f"Not enough vehicles available to handle local hazard at {event.event_location}")

        return allocated_vehicles


class FireResponseStrategy(IDispatcher):
    def assign_vehicles_to_event(self, event, stations):
        stations_sorted_by_proximity = sorted(stations, key=lambda station: compute_haversine_distance(event.event_location, station.station_location))

        print(f"Stations sorted by proximity to fire at {event.event_location}:")
        for station in stations_sorted_by_proximity:
            distance = compute_haversine_distance(event.event_location, station.station_location)
            print(f"{station.station_name} is {distance:.2f} km away.")

        vehicles_needed = 3
        allocated_vehicles = []

        for station in stations_sorted_by_proximity:
            available_vehicles = station.get_available_vehicles()
            if available_vehicles:
                for vehicle in available_vehicles:
                    if len(allocated_vehicles) < vehicles_needed:
                        print()
                        print(f"vehicle from {station.station_name} sent to {event.event_location}")
                        vehicle.assign_to_event(event)
                        allocated_vehicles.append(vehicle)

                if len(allocated_vehicles) >= vehicles_needed:
                    break

        if len(allocated_vehicles) < vehicles_needed:
            print(f"Not enough vehicles available to handle local hazard at {event.event_location}")

        return allocated_vehicles
