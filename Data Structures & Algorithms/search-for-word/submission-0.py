class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            # If we matched every character in word
            if i == len(word):
                return True

            # Invalid cases
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[i]
            ):
                return False

            # Choose / mark visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore 4 directions
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # Undo / restore
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False