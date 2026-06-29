class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
       
        def dfs(start, node):
            cur = node
            for i in range(start, len(word)):
                char = word[i]

                if char == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.end_of_word
        
        return dfs(0, self.root)


        
