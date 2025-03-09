from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # set = []  
        # hello = 0  
        
        # while any(grid):  
        #     hey = 0
        #     for i in range(len(grid)):
        #         if grid[i]:  
        #             max_val = max(grid[i])  
        #             grid[i].remove(max_val)
        #             hey = max(hey, max_val)  
            
        #     set.append(hey) 
        #     hello += hey 
        
        # return hello
         from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # Sort each row in ascending order (to access the largest values easily)
        for row in grid:
            row.sort()

        total_sum = 0
        # Perform the operation n times (number of columns)
        for _ in range(len(grid[0])):
            max_in_round = 0
            for row in grid:
                # Take the last element (which is the largest since sorted)
                max_in_round = max(max_in_round, row.pop())
            total_sum += max_in_round
        
        return total_sum

