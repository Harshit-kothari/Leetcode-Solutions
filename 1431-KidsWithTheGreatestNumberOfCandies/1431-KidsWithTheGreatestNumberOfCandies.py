# Last updated: 9/6/2026, 7:45:26 PM
import heapq
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False]*len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                res[i] = True
        return res