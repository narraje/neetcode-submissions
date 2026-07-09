from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Edge case: if there's only one element in nums
        if len(nums) == 1:
            return [nums[0]]

        # Step 1: Count the frequency of each number in nums
        freq = Counter(nums)  # This creates a dictionary where keys are numbers and values are their counts

        # Step 2: Find the k most common elements
        # Counter has a built-in method `most_common` that returns the k most common elements as (key, count) pairs
        most_common = freq.most_common(k)

        # Step 3: Extract only the elements (keys) from the most common pairs
        result = [item[0] for item in most_common]

        return result

        

