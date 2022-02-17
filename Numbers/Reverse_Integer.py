"""
https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = str(x)
            x = x[::-1]  # reverse string
            x = int(x)
            if x > 2 ** 31 - 1:  # check for overflow
                return 0
            else:
                return x

        else:  # negative
            x = str(x)
            x = x[:0:-1]  # reverse string, except for '-' character
            x = int(x)
            x = x * -1
            if x < -(2 ** 31):  # check for overflow
                return 0
            else:
                return x
