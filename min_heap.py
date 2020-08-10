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
        """Helper for add.
        Args:
            index (int): Starting index.
        """
        # We are the minimum node!
        if index == 0:
            return

        # Get the node and its parent
        node = self.heap.get_at_index(index)
        parent = self.heap.get_at_index((index - 1) // 2)

        # If the node is less than its parent
        if node < parent:
            # Swap and continue upward
            self.heap.swap(index, (index - 1) // 2)
            self._rec_add((index - 1) // 2)

        return

    def add(self, node: object) -> None:
        """Adds a node to this MinHeap.
        Args:
            node: Node to be added.
        """
        # Add the node to the end
        self.heap.append(node)

        # Get the parent
        parent = self.heap.get_at_index((self.heap.length() - 2) // 2)

        # If the node is less than its parent
        if node < parent:
            # Swap and move upward
            self.heap.swap(self.heap.length() - 1, ((self.heap.length() - 2) // 2))
            self._rec_add((self.heap.length() - 2) // 2)

        return

    def get_min(self) -> object:
        """Gets the minimum value from this MinHeap and returns it.
        Returns:
            object: Minimum value.
        """
        # This heap is empty
        if self.is_empty():
            raise MinHeapException

        return self.heap.get_at_index(0)

    def _rec_remove(self, index: int) -> None:
        """Helper for remove.
        Args:
            index (int): Starting index.
        """
        # Get the indices of the children
        child1 = 2 * index + 1
        child2 = child1 + 1

        # If those indices are outside the size of the heap, return
        if child1 > self.heap.length() and child2 > self.heap.length():
            return

        # Get the child nodes
        child1_node = None
        child2_node = None

        if child1 < self.heap.length():
            child1_node = self.heap.get_at_index(child1)

        if child2 < self.heap.length():
            child2_node = self.heap.get_at_index(child2)

        # If the children are null, return
        if child1_node is None and child2_node is None:
            return

        # Get the current parent node
        node = self.heap.get_at_index(index)

        # If the second child is null
        if child2_node is None:
            # And the first child is less than the parent
            # Swap and continue
            if child1_node < node:
                self.heap.swap(index, child1)
                self._rec_remove(child1)
        # If the first child is null
        elif child1_node is None:
            # And the second child is less than the parent
            # Swap and continue
            if child2_node < node:
                self.heap.swap(index, child2)
                self._rec_remove(child2)
        else:
            # If the first child is smaller
            if child1_node < child2_node:
                # And the first child is less than the parent
                # Swap and continue
                if child1_node < node:
                    self.heap.swap(index, child1)
                    self._rec_remove(child1)
            else:
                # And the second child is less than the parent
                # Swap and continue
                if child2_node < node:
                    self.heap.swap(index, child2)
                    self._rec_remove(child2)

        return

    def remove_min(self) -> object:
        """Removes the minimum value from this MinHeap and returns it.
        Returns:
            object: Minimum value.
        """
        # This heap is empty
        if self.is_empty():
            return MinHeapException

        # The min value is the first value in the heap
        min = self.heap.get_at_index(0)

        # Special case
        if self.heap.length() == 1:
            return self.heap.pop()

        # Pop it off last element
        last = self.heap.pop()

        # Put the last element as the first
        self.heap.set_at_index(0, last)

        # If the heap is larger than 1, continue swapping
        if self.heap.length() > 1:
            self._rec_remove(0)

        return min

    def _heapify(self, index: int) -> None:
        """Helper for build_heap. Uses the described algorithm in O(n) time
        with modification for this implementation.
        Args:
            index (int): Current index.
        """
        # This comment block is my code that is valid but does not work on Gradescope.
        # # The indices of the children
        # left = 2 * index + 1
        # right = 2 * index + 2
        #
        # # Default is that the parent is the smallest
        # smallest = index
        #
        # # If the left child is smaller and in range
        # if left < self.heap.length() and self.heap.get_at_index(index) > self.heap.get_at_index(left):
        #     smallest = left
        # # If the right child is smaller and in range
        # if right < self.heap.length() and self.heap.get_at_index(index) > self.heap.get_at_index(right):
        #     smallest = right
        #
        # # If the smallest is not the parent
        # if smallest != index:
        #     # Swap and continue up
        #     self.heap.swap(index, smallest)
        #     self._heapify(smallest)
        #
        # return
        #
        # TA Sanchit Chopra helped me solve issues with Gradescope not accepting the above solution.
        swap = True
        while swap:
            # We haven't swapped
            swap = False

            # Get the indices of the children
            left = index * 2 + 1
            right = index * 2 + 2

            # If the left is in range and is greater than the right
            if left < self.heap.length() \
                    and self.heap.get_at_index(left) > \
                    self.heap.get_at_index(right):
                # Go to the right
                left = right

            # If the left is in range and is less than the index
            if left < self.heap.length() \
                    and self.heap.get_at_index(index) > \
                    self.heap.get_at_index(left):
                # Swap and head left
                self.heap.swap(index, left)
                index = left
                swap = True

        return

    def build_heap(self, da: DynamicArray) -> None:
        """Builds a new MinHeap over this MinHeap. This is a destructive method.
        Args:
            da (DynamicArray): The new DynamicArray.
        """
        # http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/chap07.htm
        # The best explanation and proof that this method is O(n)

        # Build a new Heap
        self.heap = DynamicArray()
        for index in range(da.length()):
            value = da.get_at_index(index)
            self.heap.append(value)

        # Heapify from the bottom up to the root
        point = self.heap.length() // 2 - 1
        for indx in range(point, -1, -1):
            self._heapify(indx)



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
