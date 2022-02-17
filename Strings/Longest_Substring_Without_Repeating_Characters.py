"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialize
        max_length = 0

        for i in range(len(s)):  # first pointer
            substring = s[i]  # reset
            characters = {}  # reset
            characters[s[i]] = True
            j = i + 1  # second pointer

            while (j < len(s)) and (s[j] not in characters):
                characters[s[j]] = True
                substring += s[j]
                j += 1

            # found a repeat character
            if len(substring) > max_length:
                max_length = len(substring)

        return max_length
