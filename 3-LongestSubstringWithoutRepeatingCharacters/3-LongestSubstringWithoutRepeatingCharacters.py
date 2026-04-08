# Last updated: 4/8/2026, 9:14:28 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        left = 0
        res = 0
        if n ==0:
            return 0

        for i in range(n):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            res = max(res, i - left + 1)
        return res
            
            
        