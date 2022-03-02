"""
https://leetcode.com/problems/implement-strstr/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        else:  # 'needle' is a non-empty string
            if needle in haystack:
                return haystack.index(needle)

            else:
                return -1
