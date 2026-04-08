# Last updated: 4/8/2026, 9:14:05 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)