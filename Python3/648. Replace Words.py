class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split(' ')
        dict = sorted(dict, key=lambda x: len(x))
        for i, word in enumerate(words):
            for pattern in dict:
                if word.startswith(pattern):
                    words[i] = pattern
                    break
        return ' '.join(words)
