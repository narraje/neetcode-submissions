class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Keep track of original indices by storing (value, index)
        indexed_nums = sorted([(num, idx) for idx, num in enumerate(nums)])
        
        i = 0
        j = len(nums) - 1

        while i < j:
            current_sum = indexed_nums[i][0] + indexed_nums[j][0]
            if current_sum > target:
                j -= 1
            elif current_sum < target:
                i += 1
            else:
                # Return the original indices in ascending order
                res = [indexed_nums[i][1], indexed_nums[j][1]]
                res.sort()
                return res