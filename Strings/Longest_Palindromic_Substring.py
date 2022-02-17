"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        longest_substring = ""
        previously_seen_substrings = {}

        # helper function
        def is_palindrome(string):
            for i in range(int(len(string) / 2)):
                if string[i] != string[len(string) - i - 1]:
                    return False

            return True

        # outer logic
        if len(s) == 0:
            return ""

        elif len(s) == 1:
            return s

        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        else:  # at least 3 characters long
            for i in range(len(s)):
                for j in range(i, len(s), 1):
                    # brute force --> iterate over all possible substrings
                    substring = s[i:j + 1]
                    if substring not in previously_seen_substrings:
                        previously_seen_substrings[substring] = True
                        if is_palindrome(substring):
                            if len(substring) > max_length:
                                max_length = len(substring)
                                longest_substring = substring

        return longest_substring
