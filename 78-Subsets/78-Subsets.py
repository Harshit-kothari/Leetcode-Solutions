# Last updated: 4/8/2026, 9:14:20 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol, res = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res

            