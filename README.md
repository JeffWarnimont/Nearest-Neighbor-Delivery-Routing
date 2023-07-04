# Nearest-Neighbor-Delivery-Routing

This is a delivery routing simulation application written in Python 3.10 utilizing PyCharm Community Edition 2022.1.1 to address delivery of a list of packages with deadlines, delays, dependencies, and other conflicts. All packages need to be delivered by individual deadlines and the total travel of all 3 available trucks has to be under a certain mileage threshold.  The application utilizes a nearest neighbor algorithm for delivery routing.



The user interface via the console first asks for a number of packages to be delivered for the day.  This number will be used for the hashing bucket count.  Once this input is given, a welcome screen will give the user a list of three options.

Option 1 will display an end of day report which consists of each truck’s mileage and route completion time, the total mileage of all trucks, and a list of all packages with attributes including delivery time.

Option 2 will ask for two more inputs from the user, time and package id, and will then display only that package at the time requested.

Option 3 only asks for the time and displays all packages at that time.  

Options 2 and 3 return the correct status for each package based on the input time by comparing the given time to the time the package was loaded on the truck and the time it was delivered.

If the user enters an incorrectly formatted or out of range input, the program exits and provides an error message to try again.  



Code is commented throughout the program, but this is a general overview of how the program operates under the hood.

The hash table stores key and package object pairs. The key can be used for locating, inserting, updating, or removing package objects from the table.

Package data is read from a CSV file. Package objects are built with that data, and then inserted into the hash table.

Address and distance data from CSV files is read in to build an adjacency list with entries in the format [address1, address2, distance].  

Truck objects include a package list to hold a preselected list of package object keys.

For each truck the list of package keys is used to populate a separate list of package objects from the hash table and the list of keys is cleared. 

This is where the nearest neighbor algorithm comes into play.

Starting from the delivery hub, for each package, find the distance from the delivery hub(current location) to the package address by searching the adjacency list with the address pair.

Add the key of the package with the shortest distance from the current location to the truck package list and remove the package from the unsorted list of packages.

Update the truck mileage traveled by adding the distance from the hub(current location). 

Update the current location to the location of the package address.  

Update the truck time traveled by dividing mileage by MPH and adding the result.

Update the package status as delivered and include the current truck time.

Repeat all above steps until the unsorted list is empty.

Return the truck from the address of the final delivery back to the hub.

Update the total mileage, route end time, and truck location.

