# -- coding: utf-8 --
"""
Created on Sun Mar  5 18:34:01 2023

@author: Jorge Roa & Carmen Garro
"""
# Implement a queue-like data structure that supports
# insertion and deletion at both the front and the back of the queue

# Define a custom exception for empty deques
class Empty(Exception):
    pass

# Define the Deque class
class Deque:
    # Set the default capacity for the deque
    DEFAULT_CAPACITY = 10

    # Initialize an empty deque
    def __init__(self):
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    # Check if the deque is empty
    def is_empty(self):
        return self._size == 0

    # Add an element to the front of the deque
    def add_first(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = element
        self._size += 1

    # Add an element to the back of the deque
    def add_last(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        pos = (self._front + self._size) % len(self._data)
        self._data[pos] = element
        self._size += 1

    # Remove the first element from the deque
    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        element = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return element

    # Get the first element in the deque
    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._data[self._front]

    # Get the last element in the deque
    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._data[(self._front + self._size - 1) % len(self._data)]

    # Get the length of the deque
    def __len__(self):
        return self._size

    # Resize the deque when necessary
    def _resize(self, capacity):
        old = self._data
        self._data = [None] * capacity
        j = self._front
        for i in range(self._size):
            self._data[i] = old[j]
            j = (j + 1) % len(old)
        self._front = 0
    
    # Iterate through the deque elements
    def __iter__(self):
        for i in range(self._size):
            yield self._data[(self._front + i) % len(self._data)]
            
    # String representation of the deque
    def __str__(self):
        return '[' + ', '.join(str(item) for item in self) + ']'

# Example usage of the Deque class
d = Deque()
d.add_first(1)
d.add_last(2)
d.delete_first()
d.add_first(0)
d.add_last(3)
d.first()
d.last()
d.is_empty()
d.add_first(None)

print(len(d))
print(d.last())
print(d)