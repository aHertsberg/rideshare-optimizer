


class Locations():
    def __init__(self):
        self.locations = {}
        self.cars = {}
        self.destination = None
        
    def add_location(self, location_id, latitude, longitude):
        self.locations[location_id] = [latitude, longitude, 0]

    def add_person(self, location_id, amount=1):
        self.locations[location_id][2] += amount

    def get_locations(self):
        return list(self.locations)

    def get_persons(self, location_id):
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
    def __init__(self, start_location_id):
        self.start_location = start_location_id
        self.location = start_location_id

    def get_start(self):
        return self.start_location

    def get_location(self):
        return self.location
