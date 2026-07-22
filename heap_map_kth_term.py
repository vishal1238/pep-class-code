# Design a class to find the k-th largest element in a stream of numbers. Note that it is the k-th largest element in sorted order, not the k-th distinct element.

import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums

        # Convert list into a min heap
        heapq.heapify(self.heap)

        # Keep only k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]


# Example Usage
k = 3
nums = [4, 5, 8, 2]

obj = KthLargest(k, nums)

print(obj.add(3))   # 4
print(obj.add(5))   # 5
print(obj.add(10))  # 5
print(obj.add(9))   # 8
print(obj.add(4))   # 8