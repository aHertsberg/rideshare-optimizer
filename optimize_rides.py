import optimizer
import pandas as pd


locations = optimizer.Locations()
loc_file = pd.read_csv("locations.csv", sep=";")
for index in loc_file.index:
    locations.add_location(
        loc_file["id"][index], loc_file["latitude"][index], loc_file["longitude"][index]
    )
locations.set_destination(4)
graph = optimizer.OptimizationGraph(locations)
locations.add_location(7, 62.3, 21.93)
graph.update_locations(locations)

passengers = []
passenger_file = pd.read_csv("passengers.csv", sep=";")
for index in passenger_file.index:
    passenger = optimizer.Passenger(
        passenger_file["passenger_id"][index], passenger_file["start_id"][index]
    )
    passengers.append(passenger)

cars = {}
car_file = pd.read_csv("cars.csv", sep=";")
for index in car_file.index:
    car = optimizer.Car(car_file["car_id"][index], car_file["location_id"][index])
    cars[car.get_car_id()]=car

"""
route = {}
for car in cars:
    route[car.get_car_id] = [car.get_location,]
"""

def iterate(graph, cars, passengers, total_cost=0, minimum=None, minimum_cars=None):
    edges = graph.get_edges(cars, passengers)
    if len(edges) == 0:
        if minimum:
            # this might be excessice since we already earlier check that the 
            # total + edge is smaller than existing minimum
            if total_cost < minimum:
                minimum=total_cost
                minimum_cars=cars
        else:
            minimum = total_cost
            minimum_cars=cars
        return minimum, minimum_cars

    for edge in edges.keys():
        if minimum:
            if total_cost + edges[edge] > minimum: continue
        cars_at_start=[]
        for car_id in cars.keys():
            car = cars[car_id]
            if car.get_location() == edge[0]:
                cars_at_start.append(car_id)
        for car_id in cars_at_start:
            return drive(graph, edge, car_id, edges, cars, passengers, total_cost, minimum, minimum_cars)


def drive(graph, edge, car_id, edges, cars, passengers, total_cost, minimum, minimum_cars):
    print(f"Now driving: {car_id} : {edge}")
    cars[car_id].set_location(edge[1])
    for passenger in passengers:
        if passenger.get_location() == edge[1]:
            cars[car_id].add_passenger(passenger)
    total_cost += edges[edge]
    return iterate(graph, cars, passengers, total_cost, minimum, minimum_cars)    


print(graph.get_edges(cars, passengers))
# Destination not showing as of right now (2020-11-06)
print(locations.get_destination_coordinates())

print(locations.get_destination_id())

print(cars[3].get_location())
print(cars[5].get_location())

total_cost = 0
minimum = None

minimum, min_cars = iterate(graph, cars, passengers)
print(f"Time spent driving:{minimum}")
for car_id in min_cars.keys():
    car = cars[car_id]
    print(f"car {car_id} drove: {car.get_route()}")






