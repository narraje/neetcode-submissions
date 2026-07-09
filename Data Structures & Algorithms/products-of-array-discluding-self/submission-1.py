class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #total = []
        #for i in range(len(nums)):
        #    subtotal = 1
        #    for j in range(len(nums)):
        #        if j != i:
        #            subtotal *= (nums[j])
        #    total.append(subtotal)  
        #return total          

        n = len(nums)
        output = [1] * n

        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]


        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output        



