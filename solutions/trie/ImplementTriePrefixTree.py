"""
Solution of Implement Trie (Prefix Tree)
--------------------------------------------------------------------------------------------------------------
https://leetcode.com/problems/implement-trie-prefix-tree/description/
"""


class Trie:
    def __init__(self):
        # Store the trie as a nested dict
        self.tree = {}

    def insert(self, word: str) -> None:
        # start with the full trie
        current_root = self.tree
        for char in word:
            if char not in current_root:
                current_root[char] = {}
            current_root = current_root[char]
        current_root["end"] = True  # end of token

    def search(self, word: str) -> bool:
        # start with the full trie
        current_root = self.tree

        # for each char in word check that char
        # in current subtrie
        for char in word:
            if char not in current_root:
                return False
            # proceed to the subtrie
            current_root = current_root[char]
        # For the word to be present, the end of token
        # 'end' must be in the final subtrie
        return "end" in current_root

    def startsWith(self, prefix: str) -> bool:
        # Similar to search just that end of token
        # need not be in fina subtrie as just checking prefix
        current_root = self.tree
        for char in prefix:
            if char not in current_root:
                return False
            current_root = current_root[char]
        return True
