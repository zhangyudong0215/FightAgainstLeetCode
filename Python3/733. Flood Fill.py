class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor: return image # 72ms
        originColor = image[sr][sc]
        rlen = len(image)
        clen = len(image[0])
        def fillnewColor(r, c):
            if image[r][c] == originColor:
                image[r][c] = newColor
                if r > 0: fillnewColor(r-1, c)
                if r < rlen - 1: fillnewColor(r+1, c)
                if c > 0: fillnewColor(r, c-1)
                if c < clen - 1: fillnewColor(r, c+1)
        fillnewColor(sr, sc)
        return image
