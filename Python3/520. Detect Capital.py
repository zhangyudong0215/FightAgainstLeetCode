class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # word1 = word.lower()
        # word2 = word.upper()
        # word3 = word[0].upper() + word[1:].lower()
        # return word in [word1, word2, word3]
        
        # return word.islower() or word.isupper() or word.istitle()
        
        return word[1:] == word[1:].lower() or word == word.upper()
