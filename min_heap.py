# Course: CS261 - Data Structures
# Assignment: 5
# Student: James Leflang
# Description: A MinHeap implementation.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def _rec_add(self, index: int) -> None:
        """

        """
        if index == 0:
            return

        node = self.heap.get_at_index(index)
        parent = self.heap.get_at_index((index - 1) // 2)

        if node < parent:
            self.heap.swap(index, (index - 1) // 2)

            self._rec_add((index - 1) // 2)

        return

    def add(self, node: object) -> None:
        """Adds a node to this MinHeap.
        Args:
            node: Node to be added.
        """
        self.heap.append(node)

        parent = self.heap.get_at_index((self.heap.length() - 2) // 2)

        if node < parent:
            self.heap.swap(self.heap.length() - 1, ((self.heap.length() - 2) // 2))

            self._rec_add((self.heap.length() - 2) // 2)

        return

    def get_min(self) -> object:
        """Gets the minimum value from this MinHeap and returns it.
        Returns:
            object: Minimum value.
        """
        if self.is_empty():
            raise MinHeapException

        return self.heap.get_at_index(0)

    def _rec_remove(self, index: int) -> None:
        """

        """
        child1 = 2 * index + 1
        child2 = child1 + 1

        if child1 > self.heap.length() and child2 > self.heap.length():
            return

        child1_node = None
        child2_node = None

        node = self.heap.get_at_index(index)

        if child1 < self.heap.length():
            child1_node = self.heap.get_at_index(child1)

        if child2 < self.heap.length():
            child2_node = self.heap.get_at_index(child2)

        if child2_node is None:
            if child1_node < node:
                self.heap.swap(index, child1)
                self._rec_remove(child1)
        elif child1_node is None:
            if child2_node < node:
                self.heap.swap(index, child2)
                self._rec_remove(child2)
        else:
            if child1_node < child2_node:
                if child1_node < node:
                    self.heap.swap(index, child1)
                    self._rec_remove(child1)
            else:
                self.heap.swap(index, child2)
                self._rec_remove(child2)

        return

    def remove_min(self) -> object:
        """Removes the minimum value from this MinHeap and returns it.
        Returns:
            object: Minimum value.
        """
        if self.is_empty():
            return MinHeapException

        min = self.heap.get_at_index(0)

        if self.heap.length() == 1:
            return self.heap.pop()

        last = self.heap.pop()

        self.heap.set_at_index(0, last)

        if self.heap.length() > 1:
            self._rec_remove(0)

        return min

    def build_heap(self, da: DynamicArray) -> None:
        """Builds a new MinHeap over this MinHeap. This is a destructive method.
        Args:
            da (DynamicArray): The new DynamicArray.
        """
        pass


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
