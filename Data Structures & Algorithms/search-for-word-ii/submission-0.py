class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # stores full word when a word ends here


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # 1. Build Trie
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            # invalid boundary
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            ch = board[r][c]

            # already visited or no word has this prefix
            if ch == "#" or ch not in node.children:
                return

            # move into trie
            next_node = node.children[ch]

            # found a word
            if next_node.word is not None:
                result.append(next_node.word)
                next_node.word = None   # avoid duplicate result

            # mark visited
            board[r][c] = "#"

            # explore neighbors
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            # undo
            board[r][c] = ch

        # 2. Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result