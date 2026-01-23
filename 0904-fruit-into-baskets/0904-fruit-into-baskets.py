class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        trees = {}
        left, right,max_fruits = 0,0,1
        while right < len(fruits):
            trees[fruits[right]] = right
            if len(trees) > 2:
                max_fruits = max(max_fruits, right - left)
                left = trees.pop(min(trees, key = trees.get)) + 1
            right +=1
        return max(max_fruits, right - left)