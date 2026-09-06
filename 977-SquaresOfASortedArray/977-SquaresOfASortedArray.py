# Last updated: 9/6/2026, 7:45:41 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left,right = 0,len(nums)-1
        result = [] * len(nums)

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] **2)
                left+=1
            else:
                result.append(nums[right] **2)
                right-=1
                
        
        return result[:: -1]