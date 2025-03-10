import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  # Count frequencies of each element
        heap = []
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))  # Push (freq, num) into heap
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the smallest frequency
        
        return [num for freq, num in heap]  # Extract elements from the heap
