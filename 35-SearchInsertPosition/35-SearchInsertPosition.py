# Last updated: 4/8/2026, 9:14:24 PM
class Solution:
    def searchInsert(self, nums, T):
        def search(L, R):
            if L > R: return L
            mid = (L + R) // 1
            if nums[mid] == T: return mid
            if nums[mid] < T:
                return search(mid +1,R)
            else:
                return search(L,mid-1)
        return search(0, len(nums)-1)