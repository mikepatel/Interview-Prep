"""
https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # edge cases
        if len(strs) == 0:
            return ""

        elif len(strs) == 1:
            return strs[0]

        else:
            # brute force --> 2 for-loops
            strs = sorted(strs, key=len)  # sorted based on length
            shortest_string = strs[0]
            prefix = ""

            for character in shortest_string:
                # create prefix candidate
                prefix = prefix + character

                # check other strings
                for i in range(1, len(strs)):
                    if not strs[i].startswith(prefix):
                        return prefix[:-1]

            return prefix
