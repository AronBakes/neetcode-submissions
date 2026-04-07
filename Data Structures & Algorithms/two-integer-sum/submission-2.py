class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        differences = {}

        # create heashamp such that key:value = num:index

        for i, num in enumerate(nums):
        
            difference = target - nums[i]
            j = differences.get(difference, -1)
            differences[num] = i 

            if j == -1:
                continue
           
            if i < j:
                return [i, j]
            else:
                return [j, i]

