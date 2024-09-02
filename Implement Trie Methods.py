class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def create_trie(self, words):
        # === DO NOT MODIFY ===
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word):
        # === DO NOT MODIFY ===
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True
    
    def search(self, word):
        """
        Search the trie for the given word.

        Returns True if the word exists in the trie, False otherwise
        """
        # === YOUR CODE HERE ===

        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.isEndOfWord

    def delete(self, word):
        """
        Deletes the given the word from the Trie.

        Returns None.
        """
        # === YOUR CODE HERE ===
        
        def _delete(node, index):
            # base case: We have reached the end of the word
            if index == len(word):
                if not node.isEndOfWord:
                    return False
                node.isEndOfWord = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            delete_child = _delete(node.children[char], index + 1)
            if delete_child:
                del node.children[char]
                return not node.isEndOfWord and len(node.children) == 0
            return False

        if _delete(self.root, 0):
            if word and word[0] in self.root.children:
                # delete first character from the root's children
                del self.root.children[word[0]]
       



    def trie(self, initialWords, commands):
        # === DO NOT MODIFY ===
        self.create_trie(initialWords)

        output = []
        for command, word in commands:
            if command == "search":
                output.append(self.search(word))
            elif command == "delete":
                self.delete(word)
        return output
