# Last updated: 4/8/2026, 9:14:04 PM
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while r >= l:
            m = (r-l)//2 + l
            ver = isBadVersion(m)
            if ver == True:
                r = m-1
            if ver == False:
                l = m+1
        return l