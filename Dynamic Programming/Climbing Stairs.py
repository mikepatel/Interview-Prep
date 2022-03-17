"""
https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        # APPROACH 1: RECURSION
        """
        # helper function --> Recursion
        def count_ways(x):
            # base cases
            if x == 1:
                return 1

            elif x == 2:
                return 2

            else:  # n > 2
                return count_ways(x-2) + count_ways(x-1)

        return count_ways(n)
        """

        # APPROACH 2: DYNAMIC PROGRAMMING
        if n == 1:
            return 1

        elif n == 2:
            return 2

        else:  # n > 2
            dp = [0] * (n + 1)  # must account for zero-indexing
            dp[1] = 1
            dp[2] = 2

            for i in range(3, n + 1):
                dp[i] = dp[i - 2] + dp[i - 1]

            return dp[n]
