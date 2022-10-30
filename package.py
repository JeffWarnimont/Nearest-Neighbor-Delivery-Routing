class Package:
    # Constructor with multiple parameters indicating identity and status for package objects.
    def __init__(self, identifier, address, city, state, zipcode, delivery_deadline, mass,
                 available_time, required_truck, group, status, load_time, delivered_time):
        self.identifier = identifier
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.mass = mass
        self.available_time = available_time
        self.required_truck = required_truck
        self.group = group
        self.status = status
        self.load_time = load_time
        self.delivered_time = delivered_time

    # Overrides package object string display to show field info in terminal instead of an object address reference.
    def __str__(self):
        return "ID:%s, Address: %s,%s,%s,%s, Deadline: %s, Available: %s, Loaded: %s, Status: %s" % (
            self.identifier, self.address, self.city, self.state, self.zipcode, self.delivery_deadline,
            self.available_time, self.load_time, self.status)
