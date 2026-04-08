# Last updated: 4/8/2026, 9:14:32 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in seen:
                return [i,seen[num]]
            else:
                seen[nums[i]] = i