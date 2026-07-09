class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        n = len(nums)
        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n -1
            target = -nums[i]

            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1  
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return result                    