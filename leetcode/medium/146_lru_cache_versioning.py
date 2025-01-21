# Solution #2 (Python):
# Description: Use a versioning system and a queue to keep track of order of insertion. Upon eviction, evict elements in a map by looking at the head of the queue, using versioning to ensure freshness.
# Note:
# If order refreshing (e.g. get/ put into a pre-existing key) is the majority of operations, this solution is no longer O(1) time due to outdated versions in the queue.
# If we can identify this to be a common enough use-case (and not common enough for a double linked list), we can use O(log N) to remove existing ordering.
# Would prefer to write this solution and mention the doubly linked list as this is easier and less error-prone.
# Key ideas: Versioning.
#

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._map = dict()
        self._q = []
        self._version = 0


    def get(self, key: int) -> int:
        if key in self._map:
            new_version = self._version + 1
            self._version = new_version
            self._q.append((new_version, key))

            val, _ = self._map[key]
            self._map[key] = (val, new_version)

            return val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        new_version = self._version + 1
        self._version = new_version
        self._q.append((new_version, key))
        self._map[key] = (value, new_version)

        while len(self._map) > self._capacity:
            evict_version, evict_key = self._q.pop(0)
            if evict_version != self._map[evict_key][1]:
                # We have overwritten the value
                continue
            # we can evict the value
            del self._map[evict_key]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
