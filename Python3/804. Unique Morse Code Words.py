class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
            "....","..",".---","-.-",".-..","--","-.","---",
            ".--.","--.-",".-.","...","-","..-","...-",".--",
            "-..-","-.--","--.."]
        transformations = []
        for word in words:
            transformation = ''
            for char in word:
                transformation += MORSE[ord(char)-97]
            transformations.append(transformation)
        numDict = collections.Counter(transformations)
        return len(numDict.keys())
