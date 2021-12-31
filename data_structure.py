from typing import List, Optional


class Sll:

    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        t = self.head
        while t:
            yield t.data
            t = t.next

    def append(self, data):
        new_node = data
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = data
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node


class HashTable:
    class _Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, size: int = 2000):
        self.array: List[Optional[HashTable._Node]] = [None] * size
        self.size = size
        self.count = 0

    def __getitem__(self, key):
        if self.size == 8000:
            if self.array[key - 1000] is None:
                return
            return self.array[key - 1000]

        for i in range(self.size):
            index = self._hash_function(key, i)
            if self.array[index] is None:
                return

            elif self.array[index].key == key:
                return self.array[index].value

    def __setitem__(self, key, value):
        if self.size == 8000:
            if self.array[key - 1000] is None:
                self.array[key - 1000] = value
                self.count += 1
                return
            return False

        if self.count >= 0.75 * self.size:
            self._extend()
        new_node = HashTable._Node(key, value)
        for i in range(self.size):
            index = self._hash_function(key, i)
            if self.array[index] is None:
                self.array[index] = new_node
                self.count += 1
                return
            elif self.array[index].key == key:
                return False
        raise ValueError("Hashtable is full")

    def __iter__(self):
        count = -1
        while count < self.size:
            count += 1
            if self.array[count] is None:
                continue
            else:
                yield self.array[count].key, self.array[count].value

    def _hash_function(self, x, i):
        if self.size == 8000:
            return x - 1000
        return (hash(x) + i) % self.size

    def _extend(self):
        old_array = self.array
        self.size *= 2
        self.array = [None] * self.size
        self.count = 0
        for element in old_array:
            if isinstance(element, HashTable._Node):
                for i in range(self.size):
                    index = self._hash_function(element.key, i)
                    if self.array[index] is None:
                        self.array[index] = element
                        self.count += 1
                        break

    def values(self):
        count = -1
        while count < self.size:
            count += 1
            if self.array[count] is None:
                continue
            else:
                yield self.array[count].value

    def key(self):
        count = -1
        while count < self.size:
            count += 1
            if self.array[count] is None:
                continue
            else:
                yield self.array[count].key
























