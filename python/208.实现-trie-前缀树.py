#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start

# 递归实现
# class Trie:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.next = [None for _ in range(26)]
#         self.isEnd = False
#         self.offset = ord('a')

#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         # print("insert ", word)
#         n = len(word)
#         if n == 0:
#             self.isEnd = True
#             return

#         i = ord(word[0]) - self.offset

#         self.next[i] = self.next[i] if self.next[i] else Trie()
#         self.next[i].insert(word[1:n])

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         n = len(word)
#         if n == 0:
#             return self.isEnd

#         i = ord(word[0]) - self.offset
#         if self.next[i]:
#             return self.next[i].search(word[1:n])
#         else:
#             return False

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         # print("startsWith", prefix)
#         n = len(prefix)
#         if n == 0:
#             return True

#         i = ord(prefix[0]) - self.offset
#         if self.next[i]:
#             return self.next[i].startsWith(prefix[1:n])
#         else:
#             return False


# 迭代实现
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = [None for _ in range(26)]
        self.isEnd = False
        self.offset = ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for c in word:
            i = ord(c) - self.offset
            if not node.next[i]:
                node.next[i] = Trie()
            node = node.next[i]
        
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for c in word:
            i = ord(c) - self.offset
            if not node.next[i]:
                return False
            node = node.next[i]
        
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for c in prefix:
            i = ord(c) - self.offset
            if not node.next[i]:
                return False
            node = node.next[i]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

