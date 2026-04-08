# Last updated: 4/8/2026, 9:14:16 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(nums)
        ans = 1
        tmp = 1
        for i in range(len(nums)-1):
            print(ans, tmp)
            if nums[i] == nums[i+1]:
                continue
            if nums[i]+1 != nums[i+1]:
                ans = max(ans, tmp)
                tmp = 0
            tmp += 1
        return max(ans, tmp)
                