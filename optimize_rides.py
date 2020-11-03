import optimizer
import pandas as pd


locations = optimizer.Locations()
loc_file = pd.read_csv("locations.csv", sep=";")
for index in loc_file.index:
    locations.add_location(
        loc_file["id"][index], loc_file["latitude"][index], loc_file["longitude"][index]
    )
locations.set_destination(2)
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

cars = []
car_file = pd.read_csv("cars.csv", sep=";")
for index in car_file.index:
    car = optimizer.Car(car_file["car_id"][index], car_file["location_id"][index])
    cars.append(car)

print(graph.get_edges())
print(locations.get_destination_coordinates())

locations.set_destination(4)
print(locations.get_destination_id())

print(cars[0].get_location())
