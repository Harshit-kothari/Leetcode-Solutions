# Last updated: 4/26/2026, 9:27:01 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height) -1

        while l<r:
            area = min(height[l], height[r]) * (r-l)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
            res = max(res, area)
        return res