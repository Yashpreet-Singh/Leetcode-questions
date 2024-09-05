#https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments

class TrieNode:
    def __init__(self):
        self.children={}
        self.end_of_word=False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:


        node=self.root
      
        for letter in word:
            if letter not in node.children:
                node.children[letter]= TrieNode()
            node=node.children[letter]
        node.end_of_word=True #for last letter

        

    def search(self, word: str) -> bool:
        node=self.root

        for letter in word:
            if letter in node.children:
                node=node.children[letter]
            else:
                return False

        return node.end_of_word #word ended but we need to check it its the last letter

        

    def startsWith(self, prefix: str) -> bool:

        node=self.root
       
        for letter in prefix:
            if letter not in node.children:
                return False
            node=node.children[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
