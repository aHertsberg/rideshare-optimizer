# rideshare-optimizer
##methodology:
* Utilizing [Google's directions API](https://developers.google.com/maps/documentation/directions/overview), query
1. Transit from each passenger to each pickup node, as well as to the vehicles' starting points (does not include drivers)
2. Driving duration from each node to each other, with the exception of starting node to starting node
* Populate all permutations for passengers being located at pickup points
* Filter permutations where the condition exists that one (or more) passenger is located at a node closer to another passenger's starting point than the latter's location
* TBD: How to optimize the driving
