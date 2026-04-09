class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)

        left = 0
        right = n-1

        while left < right: 

            if left == right: continue
            if numbers[left] == numbers[right]: continue
            if numbers[left] + numbers[right] == target: break

            if numbers[left] + numbers[right] > target: 
                right -= 1
            else: 
                left += 1

        return [left+1, right+1]