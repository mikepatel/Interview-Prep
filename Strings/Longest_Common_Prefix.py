"""
https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

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
            matches = [False for i in range(len(strs))]
            matches[0] = True

            for character in shortest_string:
                prefix = prefix + character

                # check other strings
                for i in range(1, len(strs)):
                    if strs[i].startswith(prefix):
                        matches[i] = True
                    else:
                        matches[i] = False
                        break

                if not all(matches):
                    return prefix[:-1]  # drop last character

            result = prefix
            return result
