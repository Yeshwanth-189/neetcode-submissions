class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.is_word = True
        

    def search(self, word: str) -> bool:

        def dfs(index, node):
            # If we consumed all characters,
            # this is valid only if current node ends a word
            if index == len(word):
                return node.is_word

            ch = word[index]

            # Normal character
            if ch != '.':
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])

            # Wildcard '.': try every possible child
            for child in node.children.values():
                if dfs(index + 1, child):
                    return True

            return False

        return dfs(0, self.root)