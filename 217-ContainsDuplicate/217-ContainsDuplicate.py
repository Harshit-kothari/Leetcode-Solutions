# Last updated: 4/8/2026, 9:14:09 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        #print(nums)
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False

        