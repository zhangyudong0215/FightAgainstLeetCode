class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Dict = []
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.Dict = dict
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for item in self.Dict:
            if len(word) == len(item):
                count = 0
                for i in range(len(word)):
                    if word[i] != item[i]:
                        count += 1
                    if count > 1:
                        break
                if count == 1:
                    return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)