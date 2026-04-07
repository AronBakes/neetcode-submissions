class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: bucket sort — index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        
        # Step 3: collect k most frequent from the end
        result = []
        for i in range(len(buckets) - 1, -1, -1):   # highest freq → lowest
            if buckets[i]:
                result.extend(buckets[i])
                if len(result) >= k:
                    return result[:k]
        
        return result[:k]