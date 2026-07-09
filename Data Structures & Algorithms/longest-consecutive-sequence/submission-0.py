class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums.sort()
        #i = 0
        #maxsequence = 0

        #while i < len(nums):
            #currentsequence = 1
            #maxsequence = max(currentsequence, maxsequence)

            #while i + 1 < len(nums) and nums[i+1] - nums[i] <= 1:
                #if nums[i+1] - nums[i] == 1:
                    #currentsequence += 1
                #i += 1    
            #maxsequence = max(maxsequence, currentsequence)
            #i+=1    

        #return maxsequence        
                
        num_set = set(nums)
        maxsequence = 0

        for n in num_set:
            if n-1 not in num_set:
                length = 1
                while n + length in num_set:
                    length += 1
                maxsequence = max(maxsequence, length)
        return maxsequence            

