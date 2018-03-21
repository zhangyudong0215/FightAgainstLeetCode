class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums) # 44ms 符合要求O(log(n)) time, O(1) space
        head, last = 0, length
        mid = (head + last) // 2
        def check(mid):
            if mid > 0 and mid < length - 1:
                return nums[mid] == nums[mid-1] or nums[mid] == nums[mid+1]
            elif mid == 0:
                return nums[0] == nums[1]
            else:
                return nums[length-1] == nums[length-2]
        while check(mid):
            mid = (head + last) // 2
            if mid%2 == 0:
                if nums[mid] == nums[mid-1]:
                    last = mid - 1
                else:
                    head = mid + 1
            else:
                if nums[mid] == nums[mid+1]:
                    last = mid - 1
                else:
                    head = mid + 1
        return nums[mid]
