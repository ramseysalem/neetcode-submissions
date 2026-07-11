class Solution:
    def climbStairs(self, n: int) -> int:

        def fibFunc(n): 
            if n == 1: 
                return 1 
            if n == 2: 
                return 2

            return fibFunc(n - 1) + fibFunc(n - 2)

        return fibFunc(n)
        