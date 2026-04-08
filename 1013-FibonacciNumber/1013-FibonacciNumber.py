# Last updated: 4/8/2026, 9:13:50 PM
class Solution:
    def fib(self, n: int) -> int: 
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev, curr = 0,1
        for i in range(2, n+1):
            prev, curr = curr, prev+curr
        return curr