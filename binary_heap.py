# Next, let's implement the Binary Heap data structure and its basic operations.
# A binary heap is a complete binary tree used commonly for implementing priority queues.

class BinaryHeap:
    """
    A class to represent a binary heap.
    """
    def __init__(self):
        """
        Initialize a new binary heap.
        """
        self.heap = []
        
    def insert(self, val):
        """
        Insert a value into the binary heap.
        
        Parameters:
            val (int): The value to be inserted.
        """
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
        
    def _heapify_up(self, index):
        """
        Heapify up from the given index to maintain the heap property.
        
        Parameters:
            index (int): The index to start heapifying from.
        """
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)
            
    def extract_min(self):
        """
        Extract the minimum value from the heap.
        
        Returns:
            int: The minimum value.
        """
        if len(self.heap) == 0:
            return None
        
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        
        return min_val
    
    def _heapify_down(self, index):
        """
        Heapify down from the given index to maintain the heap property.
        
        Parameters:
            index (int): The index to start heapifying from.
        """
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        
        min_index = index
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[min_index]:
            min_index = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[min_index]:
            min_index = right_child_index
            
        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self._heapify_down(min_index)


# Now let's write tests to validate the implementation.
def test_binary_heap():
    """
    Test the BinaryHeap class.
    """
    # Create a new binary heap
    bh = BinaryHeap()
    
    # Test extract_min on an empty heap
    assert bh.extract_min() == None
    
    # Test insert and extract_min operations
    bh.insert(5)
    bh.insert(2)
    bh.insert(8)
    bh.insert(1)
    bh.insert(3)
    
    assert bh.extract_min() == 1
    assert bh.extract_min() == 2
    assert bh.extract_min() == 3
    assert bh.extract_min() == 5
    assert bh.extract_min() == 8
    assert bh.extract_min() == None

# Run the tests
test_binary_heap()
print("All tests for Binary Heap passed!")
