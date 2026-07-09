class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #store vals with indexes here 
        dic = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in dic:
                return [dic[diff], index]

            dic[num] = index

        

             
