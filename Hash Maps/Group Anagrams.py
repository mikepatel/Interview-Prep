"""
https://leetcode.com/problems/group-anagrams/
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # build map
        # k --> str (sorted word)
        # v --> [] (combos of word)
        mapper = {}
        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)  # list --> str

            if sorted_word in mapper:
                mapper[sorted_word].append(word)

            else:  # sorted_word not in mapper
                mapper[sorted_word] = [word]

        # go through map, collect values (lists)
        output = []
        for k, v in mapper.items():
            output.append(v)

        return output
