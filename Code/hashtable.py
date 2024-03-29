#!python

from linkedlist import LinkedList
from utils import time_it

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    @time_it
    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n) Because it loops through all buckets and the items in the buckets """
        # Collect all keys in each bucket
        all_keys = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    @time_it
    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) Because it loops through all buckets and the items in the buckets """
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    @time_it
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) Because it loops through all buckets and adds all the items in the buckets"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []

        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    @time_it
    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n) Because it loops through all buckets and counts all the items in the buckets"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

        count = 0

        for bucket in self.buckets:
            for item in bucket.items():
                count += 1
        return count

    @time_it
    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(l) or O(n/b) Because it finds the index of the bucket and finds the key in the linkedlist"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        bucket = self.buckets[self._bucket_index(key)]
        item = bucket.find(lambda item: item[0] == key)
        
        if item is not None:
            return True
        return False

        # for item, value in bucket.items():
        #     if item == key:
        #         return True
        # return False

    @time_it
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(l) or O(n/b) Because it finds the index of the bucket and finds the key in the linkedlist"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.buckets[self._bucket_index(key)]
        item = bucket.find(lambda item: item[0] == key)

        if self.contains(key):
            return item[1]
        raise KeyError('Key not found: {}'.format(key))

        # for item, value in bucket.items():
        #     if item == key:
        #         return value
        # raise KeyError('Key not found: {}'.format(key))

    @time_it             
    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(l) or O(n/b) Because it finds the index of the bucket and finds the key in the linkedlist and performs the action on it without traversal"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        bucket = self.buckets[self._bucket_index(key)]
        item = bucket.find(lambda item: item[0] == key)

        if item is not None:
            bucket.replace(item, (key, value))
        else:
            bucket.append((key, value))

    @time_it
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(1) Because it finds the index of the bucket and finds the key in the linkedlist"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.buckets[self._bucket_index(key)]

        if self.contains(key):
            bucket.delete((key, self.get(key)))
        else:
            raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
