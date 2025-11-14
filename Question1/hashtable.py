import time

# ==============================``
# HASH TABLE WITH SEPARATE CHAINING
# ==============================
class HashTable:
    class Entry:
        def __init__(self , key , value):
            self.key = key
            self.value = value

    def __init__(self , capacity = 10):
        self.capacity = capacity # Size of the array of the Hash Table
        self.table = [[] for _ in range(capacity)]
        self.size = 0 # Number of items in the Hash Table

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self , key , value):
        # index = self.index(key) # get the hash index
        index = self._hash(key)
        bucket = self.table[index]

        # if the key already exists , update the value for the same key
        for entry in bucket:
            if entry.key == key: # if the key is found ,this will be true
                entry.value = value # Update the value
                return # exit method

        #if key is not found , add the new entry into the bucket
        bucket.append(self.Entry(key,value))
        self.size += 1

    def search(self , key):
        index  = self._hash(key)
        bucket = self.table[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value

        return None # key not found in the bucket

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for entry in bucket:
            if entry.key == key:
                bucket.remove(entry)  # remove the whole Entry object from the bucket
                self.size -= 1
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}:", end="\n\n ")
            for j, entry in enumerate(bucket):
                # Print the actual entry
                print(f"({entry.key} : {entry.value})", end=" ")

                # Check if we have printed the 3rd item (j=2, 5, 8...)
                # AND that it's not the very last item in the bucket
                if (j + 1) % 3 == 0 and (j + 1) < len(bucket):
                    print()

            print(end="\n\n")