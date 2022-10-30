import csv
import datetime
from package import *
from package_hash_table import *


# Reads in raw package data from a CSV file and assigns variables to the data points.
# The complexity is O(n).
def retrieve_package_data(filename):
    with open(filename) as packageData:
        reader = csv.reader(packageData, delimiter=",")
        for row in reader:
            identifier = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zipcode = row[4]
            delivery_deadline = row[5]
            mass = row[6]
            available_time = row[7]
            required_truck = row[8]
            group = row[9]
            status = 'At Hub'
            load_time = ''
            delivered_time = ''

            # Uses assigned variables to build package objects.
            package = Package(identifier, address, city, state, zipcode, delivery_deadline, mass, available_time,
                              required_truck, group, status, load_time, delivered_time)

            # Adds package objects to package hash table.
            packages.add_package(identifier, package)


# Creates empty list to be used for adjacency list to store distances for all possible two address combinations.
address_distance_list = []


# Pulls data from address and distance CSVs and combines it to populate an adjacency list.
# This function has a complexity of O(n^2)
def build_address_distance_list(distance_file, address_file):
    with open(distance_file) as distanceData:
        distance_reader = csv.reader(distanceData, delimiter=",")
        distance_table = list(distance_reader)
    with open(address_file) as addressData:
        address_reader = csv.reader(addressData, delimiter="\n")
        addr_table = list(address_reader)
    # Fills out distance table blank spaces by duplicating distances (A to B == B to A).
    for row in range(len(distance_table)):
        for col in range(len(distance_table[row])):
            if distance_table[row][col] == '':
                distance_table[row][col] = float(distance_table[col][row])
    # Adds all possible address/distance combinations to the adjacency list in the format [address, address, distance].
    for row in range(len(distance_table)):
        for col in range(len(distance_table[row])):
            if distance_table[row][col] != '':
                address_distance_list.append([addr_table[row][0], addr_table[col][0], float(distance_table[row][col])])


# Finds the distance between two addresses by searching the adjacency list.
# Complexity of this function is O(1) time and O(n) space.
def find_distance(address1, address2):
    for i in range(len(address_distance_list)):
        if (address_distance_list[i][0] == address1 and address_distance_list[i][1] == address2) or (
                address_distance_list[i][0] == address2 and address_distance_list[i][1] == address1):
            return address_distance_list[i][2]


# Uses nearest neighbor algorithm to sort packages on each truck and updates time and distance traveled between stops.
# Complexity of this function is O(n^2)
def deliver_packages(truck):
    unsorted = []
    # List of identifiers on truck is cleared and associated packages are added to a new list for sorting purposes.
    for identifier in truck.package_list:
        package = packages.package_search(identifier)
        unsorted.append(package)
    truck.package_list.clear()
    # Compares address distances and adds next closest delivery to package list in order until unsorted list is empty.
    while len(unsorted) > 0:
        nearest_distance = 100.0
        package_to_add = None
        for package in unsorted:
            if find_distance(truck.current_location, package.address) <= nearest_distance:
                nearest_distance = find_distance(truck.current_location, package.address)
                package_to_add = package
        truck.package_list.append(package_to_add.identifier)
        # Sets package load time to the time it was loaded on the truck.
        package_to_add.load_time = truck.start_time
        unsorted.remove(package_to_add)
        # Updates truck mileage total parameter at each delivery location.
        truck.mileage += nearest_distance
        # Updates current location after routing to the current delivery.
        truck.current_location = package_to_add.address
        # Updates current time after routing to the current delivery.
        truck.current_time += datetime.timedelta(hours=nearest_distance / 18)
        # Sets package delivered time to the time it was delivered.
        package_to_add.delivered_time = truck.current_time
        # Updates package status to show the time it was delivered.
        package_to_add.status = 'Delivered ' + str(truck.current_time)
    # The lines below return the truck to the hub and make final updates to the mileage and end time of the route.
    return_trip = (find_distance(truck.current_location, truck.final_location))
    truck.mileage += return_trip
    truck.current_location = "HUB"
    truck.end_time = truck.current_time + datetime.timedelta(hours=return_trip / 18)
