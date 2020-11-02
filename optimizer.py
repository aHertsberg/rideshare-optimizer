


class Locations():
    def __init__(self):
        self.locations = {}
        self.cars = {}
        self.destination = None
        
    def add_location(self, location_id, latitude, longitude):
        self.locations[location_id] = [latitude, longitude, []]

    def add_passenger(self, passenger):
        self.locations[passenger.get_location()][2].append(passenger)

    def get_locations(self):
        return list(self.locations)

    def get_passengers(self, location_id):
        return self.locations[location_id][2]

    def get_coordinates(self, location_id):
        return (self.locations[location_id][0], self.locations[location_id][1])

    def set_destination(self, location_id):
        self.destination = location_id

    def get_destination(self):
        try:
            return self.get_coordinates(self.destination)
        except KeyError:
            print("Destination not set")

    def add_car(self, location_id, car_id):
        self.cars[car_id] = [location_id, 1]
        



class OptimizationGraph():
    def __init__(self, locations):
        self.locations = locations
        self.edges = {}
        self.populate_edges()
    
    def update_locations(self, locations):
        self.locations = locations
        self.populate_edges()

    def populate_edges(self):
        for start in self.locations.get_locations():
            for end in self.locations.get_locations():
                if start != end and self.locations.get_coordinates(start) != self.locations.get_destination():
                    distance = self.calculate_distances(start, end)
                    self.edges[f"{start},{end}"] = distance

    def calculate_distances(self, start, end):
        # TODO implement google API querying

        if start < end:
            return 4
        else:
            return 5

    def get_edges(self):
        return self.edges

    def get_locations(self):
        return locations


          
class Passenger():
    def __init__(self, passenger_id, start_location_id):
        self.passenger_id = passenger_id
        self.start_location = start_location_id
        self.location = start_location_id

    def get_id(self):
        return self.passenger_id

    def get_start(self):
        return self.start_location

    def get_location(self):
        return self.location

class Car():
    def __init__(self, car_id, start_location_id):
        self.car_id = car_id
        self.location_ids = [start_location_id]
        self.passengers = []

    def get_car_id(self):
        return self.car_id

    def get_location(self):
        return self.location_ids[-1]

    def set_location(self, location_id):
        self.location_ids.append(location_id)
        return

    def get_route(self):
        return self.location_ids

    def get_passengers(self):
        return self.passengers

    def add_passengers(self, passenger):
        self.passengers.append(passenger)
        return
