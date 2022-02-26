"""
https://leetcode.com/problems/generate-parentheses/
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        backtracking
        recursion
        enumeration
        """

        # Backtracking
        def backtrack(candidate, num_left_parentheses, num_right_parentheses):

            # found a solution, add to 'combos'
            if len(candidate) == 2 * n:
                combos.append(candidate)
                return

            else:  # continue searching

                if num_left_parentheses < n:
                    # apply value
                    # add a '(' --> add a new pair
                    candidate = candidate + "("
                    num_left_parentheses += 1

                    # search for solution
                    backtrack(candidate, num_left_parentheses, num_right_parentheses)

                    # remove value
                    candidate = candidate[:-1]
                    num_left_parentheses = num_left_parentheses - 1

                if num_right_parentheses < num_left_parentheses:
                    # apply value
                    # add a ')' for balance
                    candidate = candidate + ")"
                    num_right_parentheses += 1

                    # search for solution
                    backtrack(candidate, num_left_parentheses, num_right_parentheses)

                    # remove value
                    candidate = candidate[:-1]
                    num_right_parentheses = num_right_parentheses - 1

        #
        # driver code
        combos = []
        backtrack(candidate="", num_left_parentheses=0, num_right_parentheses=0)

        return combos
