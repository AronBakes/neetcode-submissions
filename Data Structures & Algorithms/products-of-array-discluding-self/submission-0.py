class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        for i in range(len(nums)):
            out = 1
            for j, n in enumerate(nums):
                if i==j:
                    continue
                else:
                    out = n*out

            output.append(out)
            out = 1


        return output