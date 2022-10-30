from datetime import timedelta


class Truck:
    # Constructor with multiple parameters indicating identity and status for truck objects.
    def __init__(self, start_time, current_time, end_time, mileage, current_location,
                 final_location, package_list):
        self.start_time = start_time
        self.current_time = current_time
        self.end_time = end_time
        self.mileage = mileage
        self.current_location = current_location
        self.final_location = final_location
        self.package_list = package_list

    # Overrides truck object string display to show field info in terminal instead of an object address reference.
    def __str__(self):
        return "%s, %s, %s, %s, %.1f, %s, %s" % (self.start_time, self.current_time, self.end_time, self.mileage,
                                                 self.current_location, self.final_location, self.package_list)


# Create 3 truck object instances with package lists filled manually.
truck1 = Truck(timedelta(hours=8, minutes=0, seconds=0),
               timedelta(hours=8, minutes=0, seconds=0), timedelta(hours=0, minutes=0, seconds=0),
               0.0, 'HUB', 'HUB', [1, 8, 13, 14, 15, 16, 19, 20, 21, 30, 34, 37, 39])
truck2 = Truck(timedelta(hours=10, minutes=20, seconds=0),
               timedelta(hours=10, minutes=20, seconds=0), timedelta(hours=0, minutes=0, seconds=0),
               0.0, 'HUB', 'HUB', [3, 5, 9, 10, 11, 17, 18, 22, 23, 27, 35, 36, 38])
truck3 = Truck(timedelta(hours=9, minutes=5, seconds=0),
               timedelta(hours=9, minutes=5, seconds=0), timedelta(hours=0, minutes=0, seconds=0),
               0.0, 'HUB', 'HUB', [2, 4, 6, 7, 12, 24, 25, 26, 28, 29, 31, 32, 33, 40])
