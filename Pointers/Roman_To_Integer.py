"""
https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        # create a list of integers
        integers = []
        for c in s:
            if c == "I":
                integers.append(1)

            elif c == "V":
                integers.append(5)

            elif c == "X":
                integers.append(10)

            elif c == "L":
                integers.append(50)

            elif c == "C":
                integers.append(100)

            elif c == "D":
                integers.append(500)

            else:
                integers.append(1000)

        # iterate through list of integers
        while integers:
            if len(integers) == 1:
                total = total + integers[0]
                integers.pop(0)

            else:
                if integers[0] >= integers[1]:
                    total = total + integers[0]
                    integers.pop(0)

                else:
                    # integers[0] < integers[1]
                    total = total + (integers[1] - integers[0])
                    integers.pop(0)
                    integers.pop(0)

        return total
