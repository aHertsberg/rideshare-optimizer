import optimizer
import pandas as pd
 

locations = optimizer.Locations()
loc_file = pd.read_csv("locations.csv", sep=";")
for index in loc_file.index:
    locations.add_location(
                           loc_file["id"][index], 
                           loc_file["latitude"][index], 
                           loc_file["longitude"][index])
locations.set_destination(2)
graph = optimizer.OptimizationGraph(locations)
locations.add_location(7, 62.3, 21.93)
graph.update_locations(locations)
passenger_file = pd.read_csv("passengers.csv", sep=";")
for index in passenger_file.index:
    passenger = optimizer.Passenger(
                          passenger_file["passenger_id"][index], 
                          passenger_file["start_id"][index])
    locations.add_passenger(passenger)

print(graph.get_edges())
print(locations.get_passengers(1))


