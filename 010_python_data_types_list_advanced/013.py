"""

Write a Python a function to implement a LRU cache.

From Wikipedia - Least recently used (LRU) Discards the least recently used items first. This algorithm requires
keeping track of what was used when, which is expensive if one wants to make sure the algorithm always discards the
least recently used item. General implementations of this technique require keeping "age bits" for cache-lines and
track the "Least Recently Used" cache-line based on age-bits. In such an implementation, every time a cache-line
is used, the age of all other cache-lines changes.

Implement an LRU Cache that basically has a predefined capacity and provides the following features:
    1. stores some data in a dict fashion
    2. gets new data a key-val pair
        a. and obviously, the new provided pair is the most recently one
        b. this method can also change a key's value when provided with a pair whose key is already in the cache
        c. when the cache exceeds the predefined capacity, it would pop the least recently used key-val pair
    3. return the val of a provided key
        a. and hence, the key would be the last used element
        b. if the key is not present in the cache, return -1

The LRU Cache capacity is 2

put(10, 10)
put(20, 20)
get(10)         =>  10
put(30, 30)
get(20)         =>  -1
put(40, 40)
get(10)         =>  -1
get(30)         =>  30
get(40)         =>  40


"""


from collections import OrderedDict


class LRU:
    def __init__(self, capacity: int):
        self._c = capacity
        self._cache = OrderedDict()

    def put(self, key: int, val: int):
        if not len(self._cache) < self._c:
            self._cache.popitem(last=False)
            self._cache[key] = val

        self._cache[key] = val
        self._cache.move_to_end(key, last=True)

    def get(self, key):
        if key not in self._cache:
            return -1
        else:
            self._cache.move_to_end(key, last=True)
            return self._cache[key]


def main():
    lru = LRU(2)

    lru.put(10, 10)
    lru.put(20, 20)
    print(lru.get(10))
    lru.put(30, 30)
    print(lru.get(20))
    lru.put(40, 40)
    print(lru.get(10))
    print(lru.get(30))
    print(lru.get(40))


if __name__ == "__main__":
    main()
