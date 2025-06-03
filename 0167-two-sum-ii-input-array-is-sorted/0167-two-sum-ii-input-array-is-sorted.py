class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in numbers[i + 1:]:
                j = numbers.index(diff, i + 1)
                return [i+1, j+1]