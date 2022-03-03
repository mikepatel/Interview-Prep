"""
https://leetcode.com/problems/count-and-say/
"""


class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        else:  # n > 1
            output = "1"

            for i in range(2, n + 1):
                string = ""
                count = 1

                for j in range(0, len(output) - 1):
                    current = output[j]

                    if output[j + 1] == current:
                        count += 1

                    else:  # does not match
                        string = string + str(count) + current
                        count = 1  # reset

                # always end with '1'
                string = string + str(count) + "1"

                # update for next output
                output = string

            return output
