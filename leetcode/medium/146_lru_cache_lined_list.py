# Solution #1 (Python):
# Description: Using a doubly linked list to update, elements in the linked list are stored as pointers to the underlying map structure which provide O(1) access.
# Key ideas: Linked list for updating ordering.
# Map for query

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev_node = None
        self.next_node = None

def link(first: Node, second: Node) -> None:
    if first:
        first.next_node = second
    if second:
        second.prev_node = first

class LRUCache:

    def __init__(self, capacity: int):
        self._storage = dict()

        self._oldest = None
        self._newest = None

        self._size = 0
        self._capacity = capacity

    def get(self, key: int) -> int:
        if key not in self._storage:
            return -1
        node = self._storage[key]

        if node != self._newest:
            if node == self._oldest:
                self._oldest = node.next_node

            link(node.prev_node, node.next_node)
            link(node, None)
            link(self._newest, node)
            self._newest = node

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self._storage:
            self._storage[key].value = value
            # update order
            self.get(key)
        else:
            if self._size == self._capacity:
                # we need to evict
                oldest = self._oldest
                link(None, oldest.next_node)
                self._oldest = oldest.next_node
                if self._newest == oldest:
                    self._newest = None
                del self._storage[oldest.key]
            else:
                self._size += 1

            node = Node(key, value)
            link(self._newest, node)
            self._newest = node
            if self._oldest is None:
                self._oldest = node

            self._storage[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)