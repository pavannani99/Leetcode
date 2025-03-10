class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = [num for row in matrix for num in row]  # Flatten the matrix

        heap =[-num for num in nums[:k]]
        heapq.heapify(heap)  # Create a min-heap with the first k elements

        for num in nums[k:]:
            if num < -heap[0]:
                heapq.heapreplace(heap, -num)  # Replace the smallest element

        return -heap[0]  # The
