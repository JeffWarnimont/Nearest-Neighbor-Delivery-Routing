# Author: Jefferson Warnimont
# Student ID: 001482272

from helpers import *
from package_hash_table import *
from truck import *

# Retrieve package data from CSV and insert into packages hash table.
retrieve_package_data('package_data.csv')

# Retrieve distance and address data from CSVs and insert into address/distance adjacency list.
build_address_distance_list('distance_data.csv', 'addresses.csv')

# Runs delivery for each truck with departures of 8:00AM, 9:05AM, and  10:20AM.
deliver_packages(truck1)  # Truck 1 departs 8:00 AM
deliver_packages(truck3)  # Truck 3 departs 9:05 AM
deliver_packages(truck2)  # Truck 2 departs 10:20 AM

# User interface welcome menu and options
print('Welcome to the WGUPS delivery tracking system!')
print('----------------------------------------------')
print('What would you like to do today?')
print('Please select option 1, 2, or 3 from the list.')
print('----------------------------------------------')
print('1. View end of day report.')
print('2. Lookup single package status by ID at given time.')
print('3. View all package status at given time.')

# User inputs a choice for information output to console.
# Complexity of terminal display is O(n)
choice = int(input('1, 2, or 3?'))
# Choice 1 results in multiple print statements to console including truck mileage and route completion times.
# A list of all packages with delivery times at end of day is also printed
if choice == 1:
    print('All packages successfully delivered by deadlines with all requirements met!')
    print('Truck 1 total miles: ' + str("%.1f" % truck1.mileage))
    print('Truck 1 route completed: ' + str(truck1.end_time))
    print('Truck 3 total miles: ' + str("%.1f" % truck3.mileage))
    print('Truck 3 route completed: ' + str(truck3.end_time))
    print('Truck 2 total miles: ' + str("%.1f" % truck2.mileage))
    print('Truck 2 route completed: ' + str(truck2.end_time))
    total = float(truck1.mileage + truck2.mileage + truck3.mileage)
    print('Total mileage: ' + str("%.1f" % total))
    print('----------------------------------------------')
    for i in range(1, (len(packages.package_table) + 1)):
        print(packages.package_search(i))
# Choices 2 or 3 require an additional input from the user as they represent a snapshot of a specific moment in time.
# The inputted time is converted to a usable format for time calculations.
elif (choice == 2) or (choice == 3):
    try:
        input_time = input('Please input a time for status check in 24 hour format (HH:MM:SS): ')
        (hour, minute, second) = input_time.split(":")
        converted_time = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
        # Time comparisons are used to update package status to match status at user's requested time.
        for i in range(1, (len(packages.package_table) + 1)):
            package = packages.package_search(i)
            if converted_time < package.load_time:
                package.status = 'At Hub'
            elif converted_time > package.delivered_time:
                package.status = ('Delivered: ' + str(package.delivered_time))
            else:
                package.status = 'En route'
        # Choice 2 requires an additional input of id from user.
        # The chosen package will display with updated status at user's requested time to the console.
        if choice == 2:
            tracking = int(input('Enter package id.'))
            if tracking not in range(1, (len(packages.package_table) + 1)):
                print('Invalid entry. Try again.')
                exit()
            else:
                print(packages.package_search(tracking))
        # Choice 3 prints all packages with updated status at user's requested time to the console.
        if choice == 3:
            # Prints list of all packages
            for i in range(1, (len(packages.package_table) + 1)):
                print(packages.package_search(i))
    # User inputs are checked for errors in format and value and an error message displays if incorrect input entered.
    except ValueError:
        print("Invalid entry. Try again.")
        exit()
else:
    print('Invalid entry. Try again.')
    exit()
