"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # brute force
        output = []

        if len(digits) == 0:
            return []

        # create mapping between digits and letters
        mapper = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        output = []  # list of lists
        for d in digits:
            if len(output) == 0:  # first digit
                for letter in mapper[d]:
                    output.append(letter)

            else:  # append next letter
                temp = []
                for i in output:
                    for letter in mapper[d]:
                        temp.append(i + letter)

                output = temp

        return output
