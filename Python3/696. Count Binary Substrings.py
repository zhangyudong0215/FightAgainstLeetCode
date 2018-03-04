class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # head = s[0] # 140ms
        # count = 0
        # count_list = []
        # for char in s:
        #     if char == head:
        #         count += 1
        #     else:
        #         count_list.append(count)
        #         head = char
        #         count = 1
        # count_list.append(count)
        # ans = list(map(min, zip(count_list[:-1], count_list[1:])))
        # return sum(ans)

        # head = s[0] # 256ms
        # count_list = [0]
        # for char in s:
        #     if char != head:
        #         count_list.append(1)
        #         head = char
        #     else:
        #         count_list[-1] += 1
        # ans = list(map(min, zip(count_list[:-1], count_list[1:])))
        # return sum(ans)
        
        head = s[0] # 方法类似，但是只记录count_list最后两项，这样空间复杂度为O(1), 136ms
        ans, prev, cur = 0, 0, 0
        for char in s:
            if char != head:
                ans += min(prev, cur)
                head = char
                prev, cur = cur, 1
            else:
                cur += 1
        ans += min(prev, cur)
        return ans
