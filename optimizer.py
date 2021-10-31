class Locations:
    def __init__(self):
        self.locations = {}
        self.destination = None

    def add_location(self, location_id, latitude, longitude, visited=False):
        self.locations[location_id] = [latitude, longitude, visited]
        return

    def get_locations(self):
        return list(self.locations)

    def get_coordinates(self, location_id):
        return (self.locations[location_id][0], self.locations[location_id][1])

    def set_destination(self, location_id):
        self.destination = location_id
        return

    def get_destination_coordinates(self):
        try:
            return self.get_coordinates(self.destination)
        except KeyError:
            print("Destination not set")
            return None

    def get_destination_id(self):
        return self.destination


class OptimizationGraph:
    def __init__(self, locations):
        self.locations = locations
        self.edges = {}
        self.populate_edges()

    def update_locations(self, locations):
        self.locations = locations
        self.populate_edges()
        return

    def populate_edges(self):
        for start in self.locations.get_locations():
            for end in self.locations.get_locations():
                if start != end:
                    distance = self.calculate_distances(start, end)
                    self.edges[(start,end)] = distance

    def calculate_distances(self, start, end):
        # TODO implement google API querying
        # for now, a very crude distance generator:
        if start < end:
            return 4
        else:
            return 5

    def get_edges(self, cars, passengers):
        destination = self.locations.get_destination_id()
        car_locations = []
        for car_id in cars.keys():
            car = cars[car_id]
            location = car.get_location()
            if not location in car_locations:
                car_locations.append(location)

        to_visit = [destination,]
        for passenger in passengers:
            location = passenger.get_location()
            if not location in to_visit and not passenger.is_in_car():
                to_visit.append(location)

        edges = {}
        for key in self.edges.keys():
            if key[0] in car_locations and key[1] in to_visit:
                edges[key] = self.edges[key]
        return edges

    def get_locations(self):
        return locations


class Passenger:
    def __init__(self, passenger_id, start_location_id):
        self.passenger_id = passenger_id
        self.start_location = start_location_id
        self.location = start_location_id
        self.in_car = False
        self.arrived = False

    def get_id(self):
        return self.passenger_id

    def get_start(self):
        return self.start_location

    def get_location(self):
        return self.location

    def set_location(self, location_id):
        self.location = location_id
        return

    def is_in_car(self):
        return self.in_car

    def pick_up(self):
        self.in_car = True
        return

    def has_arrived(self):
        return self.at_destination

    def set_arrived(self, state: bool):
        self.arrived = state
        return

class Car:
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

    def add_passenger(self, passenger):
        passenger.pick_up()
        self.passengers.append(passenger)
        return
    # for potential future limitations
    def get_weight(self):
        return 1 + len(self.passengers)











