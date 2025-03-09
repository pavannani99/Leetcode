from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        set = []  # To store the maximum values deleted in each round
        hello = 0  # Final sum
        
        while any(grid):  # While there are elements left in the grid
            hey = 0
            for i in range(len(grid)):
                if grid[i]:  # If the row is not empty
                    max_val = max(grid[i])  # Find the max in the row
                    grid[i].remove(max_val)  # Remove the max value from the row
                    hey = max(hey, max_val)  # Track the highest value in this round
            
            set.append(hey)  # Store the highest value deleted in this round
            hello += hey  # Add to the final sum
        
        return hello
