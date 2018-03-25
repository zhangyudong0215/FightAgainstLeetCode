class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return [0, 0]
        total = 0
        lines = 1
        for char in S:
            if total + widths[ord(char)-97] > 100:
                lines += 1
                total = widths[ord(char)-97]
            else:
                total += widths[ord(char)-97]
        return [lines, total]
