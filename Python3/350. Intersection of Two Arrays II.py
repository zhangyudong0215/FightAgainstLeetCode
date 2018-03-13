class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = collections.Counter(nums1)
        nums2 = collections.Counter(nums2)
        ans = []
        for num1 in nums1:
            if num1 in nums2:
                ans.extend([num1] * min(nums1[num1], nums2[num1]))
        return ans
