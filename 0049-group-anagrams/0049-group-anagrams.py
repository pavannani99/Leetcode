from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Value: list of anagrams

        for s in strs:
            count = [0] * 26  # Count of each character 'a' to 'z'

            for char in s:
                count[ord(char) - ord('a')] += 1

            # Use tuple(count) as key because lists can't be dict keys
            res[tuple(count)].append(s)

        return list(res.values())
