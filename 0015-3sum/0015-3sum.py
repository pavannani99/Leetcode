class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        hey = sorted(nums)  # Sort the array
        hi = []

        for i in range(len(hey)):
            if i > 0 and hey[i] == hey[i - 1]:  # Skip duplicate i
                continue

            target = -hey[i]
            l, r = i + 1, len(nums) - 1  # Left and Right pointers

            while l < r:
                if hey[l] + hey[r] == target:
                    hi.append([hey[i], hey[l], hey[r]])  # Append triplet

                    # Skip duplicates for l and r
                    l += 1
                    while l < r and hey[l] == hey[l - 1]:
                        l += 1

                    r -= 1  # Move right pointer after finding a valid triplet

                elif hey[l] + hey[r] < target:
                    l += 1  # Increase left to get a bigger sum
                else:
                    r -= 1  # Decrease right to get a smaller sum

        return hi
