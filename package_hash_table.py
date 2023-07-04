# PackageHashTable class using chaining to handle collisions.
# Adapted from: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
class PackageHashTable:
    # Hash table constructor which assigns all buckets with an empty list.
    # The complexity is O(n).
    def __init__(self):
        # By creating an amount of buckets equal to the amount of packages for the day this will ensure O(1) complexity
        # on search, remove, and update functions while the initial table creation will have a complexity of O(n).
        # This assumes that packages will continue to have sequential ids.
        try:
            package_count = int(input('How many packages are we delivering today?'))
            self.package_table = []
            if package_count >= 1:
                for i in range(package_count):
                    self.package_table.append([])
            else:
                print("Invalid entry. Try again.")
                exit()
        except ValueError:
            print("Invalid entry. Try again.")
            exit()

    # Inserts a new package into the hash table or updates an existing package if the key matches.
    # The complexity is O(1).
    def add_package(self, key, package):
        # Uses hash function to determine correct bucket.
        bucket = hash(key) % len(self.package_table)
        bucket_list = self.package_table[bucket]

        # Updates package if key is already in bucket.
        for kp in bucket_list:
            if kp[0] == key:
                kp[1] = package
                return True

        # If key is not already in bucket, the key and package are added to the bucket list.
        key_package = [key, package]
        bucket_list.append(key_package)
        return True

    # Searches the hash table for a package with matching key and returns package if found or None if not found.
    # The complexity is O(1).
    def package_search(self, key):
        # Uses hash function to determine in which bucket this key would be located.
        bucket = hash(key) % len(self.package_table)
        bucket_list = self.package_table[bucket]

        # Searches for the key in the bucket list.
        for kp in bucket_list:
            if kp[0] == key:
                return kp[1]
        return None

    # Removes a package with matching key from the hash table.
    # The complexity is O(1).
    def remove_package(self, key):
        # Uses hash function to determine the bucket list where this package will be removed from.
        bucket = hash(key) % len(self.package_table)
        bucket_list = self.package_table[bucket]

        # Removes the package from the bucket list if it is present.
        for kp in bucket_list:
            if kp[0] == key:
                bucket_list.remove([kp[0], kp[1]])


# Create hash table instance.
packages = PackageHashTable()
