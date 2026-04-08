# Last updated: 4/8/2026, 9:14:17 PM
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]+', '', s)
        #print(s1)
        s2 = s[::-1]
        s2 = re.sub('[^a-zA-Z0-9]+', '', s2)
        #print(s2)
        if s == s2:
            return True
        return False