class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        my_map = {}

        for num in nums:
            # if num in my_map:
            #     if my_map[num] == 1: 
            #         return True
            # else:
            #     my_map[num] = 1

            if my_map.get(num, 0) == 1:
                return True
            else:
                 my_map[num] = my_map.get(num, 0) + 1

        return False