class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict1 = collections.Counter(ransomNote)
        dict2 = collections.Counter(magazine)
        dict2.subtract(dict1)
        for value in dict2.values():
            if value < 0:
                return False
        return True
