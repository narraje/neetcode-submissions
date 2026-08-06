class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        curr_len = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[curr_len])
                curr_len += 1
            seen.add(s[r])
            max_len = max(max_len, r - curr_len + 1) 
        return max_len       
                     

