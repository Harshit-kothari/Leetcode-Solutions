# Last updated: 6/1/2026, 10:46:02 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge cases: Negative numbers and numbers ending in 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted_num = 0
        
        # Keep moving digits from the back of x to the front of reverted_num
        while x > reverted_num:
            reverted_num = (reverted_num * 10) + (x % 10)
            x //= 10  # Integer division to remove the last digit
            
        # For even lengths: x == reverted_num (e.g., 12 == 12)
        # For odd lengths: x == reverted_num // 10 to ignore the middle digit (e.g., 1 == 12 // 10)
        return x == reverted_num or x == reverted_num // 10