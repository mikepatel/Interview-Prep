"""
https://leetcode.com/problems/word-search/
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # APPROACH: DFS

        # initialization
        num_rows = len(board)
        num_cols = len(board[0])

        # helper function
        def dfs(visited, current_row, current_col, index):
            # stopping condition
            if index == len(word):
                return True

            # boundaries
            if current_row < 0:  # top boundary
                return False

            if current_row >= num_rows:  # bottom boundary
                return False

            if current_col < 0:  # left boundary
                return False

            if current_col >= num_cols:  # right boundary
                return False

            # early stopping condition
            if board[current_row][current_col] != word[index]:
                return False

            else:  # keep searching
                if (current_row, current_col) not in visited:
                    # apply value
                    visited[(current_row, current_col)] = True  # visited

                    # backtrack
                    if any([
                        dfs(visited, current_row + 1, current_col, index + 1),
                        dfs(visited, current_row - 1, current_col, index + 1),
                        dfs(visited, current_row, current_col + 1, index + 1),
                        dfs(visited, current_row, current_col - 1, index + 1)
                    ]):
                        return True

                    # remove value
                    del visited[(current_row, current_col)]
                    return False

        # driver code
        for i in range(num_rows):
            for j in range(num_cols):
                # perform dfs @ each cell as a starting point
                if dfs(visited={}, current_row=i, current_col=j, index=0):
                    return True

        return False
