class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}

        for i, num in enumerate(nums):
            if num in dup:
                return True
            else:
                dup[num] = True
        return False            
        