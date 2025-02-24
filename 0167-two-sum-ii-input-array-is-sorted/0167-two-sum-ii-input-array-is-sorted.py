class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            tres = target - numbers[i]  # Find the required complement
            
            # Check for complement in the list after the current index to avoid using the same number twice
            if tres in numbers[i + 1:]:
                j = numbers.index(tres, i + 1)  # Find the index of the complement starting from i+1
                return [i + 1, j + 1]  # Return 1-based indices

        return []  # If no valid pair is found
