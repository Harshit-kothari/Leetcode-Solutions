# Last updated: 9/6/2026, 7:45:44 PM
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