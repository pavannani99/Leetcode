class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat_matrix = [element for row in matrix for element in row]
        flat_matrix.sort()
        return flat_matrix[k-1]