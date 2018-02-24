class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        length = 0
        for num in nums1:
            length += 1
            index = nums2.index(num)
            for num2 in nums2[index:]:
                if num2 > num:
                    ans.append(num2)
                    break
            if len(ans) < length:
                ans.append(-1)
        return ans
