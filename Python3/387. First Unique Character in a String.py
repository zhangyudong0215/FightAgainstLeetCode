class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # countChars = {} # 160ms
        # for char in s:
        #     countChars[char] = countChars.get(char, 0) + 1
        # for index, char in enumerate(s):
        #     if countChars[char] == 1:
        #         return index
        # return -1
        
        # countChars = collections.Counter(s) # 124ms
        # for index, char in enumerate(s):
        #     if countChars[char] == 1:
        #         return index
        # return -1
        
        letters = [chr(i) for i in range(ord('a'), ord('z')+1)] # 88ms
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
