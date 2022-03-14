"""
https://leetcode.com/problems/unique-paths/
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DYNAMIC PROGRAMMING

        # APPROACH 1
        # BACKTRACK
        # TWO POINTERS
        """
        # backtrack
        @cache  # memoization
        def backtrack(row, col):
            # stopping condition
            if row == m-1:  # cannot move down any further
                return 1

            elif col == n-1:  # cannot move right any further
                return 1

            else:  # search
                paths_moving_right = backtrack(row, col+1)  # move right
                paths_moving_down = backtrack(row+1, col)  # move down
                return paths_moving_right + paths_moving_down

        # driver code
        # edge case
        if m == 0 or n == 0:
            return 0

        elif m == 1 and n == 1:
            return 1

        else:
            num_paths = backtrack(row=0, col=0)
            return num_paths

        """

        # APPROACH 2
        # TWO FOR-LOOPS
        # edge case
        if m == 0 or n == 0:
            return 0

        elif m == 1 and n == 1:
            return 1

        else:
            # initialize 'dp'
            dp = [[0 for j in range(n)] for i in range(m)]

            # initialize / base cases
            for i in range(m):
                for j in range(n):
                    if i == m - 1:  # last row, can only move right; therefore, 1 path to destination
                        dp[i][j] = 1

                    if j == n - 1:  # last column, can only move down; therefore, 1 path to destination
                        dp[i][j] = 1

            # build 'dp' from [m-1][n-1] to [0][0]
            for i in range(m - 2, -1, -1):
                for j in range(n - 2, -1, -1):
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

            return dp[0][0]
