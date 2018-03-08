class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # childern = sorted(g, reverse=True) # 144ms 倒数25%
        # cookies = sorted(s, reverse=True)
        # count = 0
        # found = True
        # while len(childern) > 0 and found:
        #     child = childern.pop()
        #     found = False
        #     while len(cookies) > 0 and not found:
        #         if cookies.pop() >= child:
        #             found = True
        #             count += 1
        # return count
        
        childern = sorted(g) # 88ms beats 100%
        cookies = sorted(s)
        count, index = 0, 0
        while count < len(childern) and index < len(cookies):
            if cookies[index] >= childern[count]:
                count += 1
            index += 1
        return count
