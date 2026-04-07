class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq_map = {}

        for i, word in enumerate(strs):
            alpha_arr = [0] * 26

            for c in word:
                alpha_i = ord(c) - ord('a') # convert a=0, b=1 .... z=25
                alpha_arr[alpha_i] += 1

            # freq_map[alpha_arr] = i 

            # tuple() because lists cannot be dictionary keys
            key = tuple(alpha_arr)
            
            if key not in freq_map:
                freq_map[key] = []
            freq_map[key].append(word)
        
        # Return just the grouped values (in any order)
        return list(freq_map.values())