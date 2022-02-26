"""
https://leetcode.com/problems/generate-parentheses/
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # Backtracking
        def backtrack(candidate, num_left_parentheses, num_right_parentheses):

            # found a solution, add to 'combos'
            if len(candidate) == 2 * n:
                solution = "".join(candidate)
                combos.append(solution)
                return

            else:  # continue searching

                if num_left_parentheses < n:
                    # apply value
                    # add a '(' --> add a new pair
                    candidate.append("(")
                    num_left_parentheses += 1

                    # search for solution
                    backtrack(candidate, num_left_parentheses, num_right_parentheses)

                    # remove value
                    candidate.pop()
                    num_left_parentheses = num_left_parentheses - 1

                if num_right_parentheses < num_left_parentheses:
                    # apply value
                    # add a ')' for balance
                    candidate.append(")")
                    num_right_parentheses += 1

                    # search for solution
                    backtrack(candidate, num_left_parentheses, num_right_parentheses)

                    # remove value
                    candidate.pop()
                    num_right_parentheses = num_right_parentheses - 1

        #
        # driver code
        combos = []
        backtrack(candidate=[], num_left_parentheses=0, num_right_parentheses=0)

        return combos
