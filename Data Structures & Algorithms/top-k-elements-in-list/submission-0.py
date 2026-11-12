from collections import Counter 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = []
        # Count the frequencies first of each value such as 
        # {1:1, 2:2, 3:3}
        freq = Counter(nums)

        # Swap to get the max of the frequencies.
        swapped_heap = []
        for key, value in freq.items():
            swapped_heap.append((value, key))

        heapq.heapify_max(swapped_heap)
        for i in range(k):
            topK.append(heapq.heappop_max(swapped_heap)[1])

        return topK