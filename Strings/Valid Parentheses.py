"""
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True

        else:
            temp = s  # before
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

            if s == temp:  # after
                return False

            else:
                return self.isValid(s)
