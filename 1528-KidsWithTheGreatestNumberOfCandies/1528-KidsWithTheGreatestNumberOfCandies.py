# Last updated: 4/8/2026, 9:13:52 PM
import heapq
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False]*len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                res[i] = True
        return res