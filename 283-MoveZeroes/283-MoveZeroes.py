# Last updated: 4/8/2026, 9:14:02 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[left] = nums[left], nums[i]
                left+=1
        return nums
        