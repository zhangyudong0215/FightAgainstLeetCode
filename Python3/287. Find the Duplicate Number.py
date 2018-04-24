class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         # Find the intersection point of the two runners.
#         tortoise = nums[0]
#         hare = nums[0]
#         while True:
#             tortoise = nums[tortoise]
#             hare = nums[nums[hare]]
#             if tortoise == hare:
#                 break
        
#         # Find the "entrance" to the cycle.
#         ptr1 = nums[0]
#         ptr2 = tortoise
#         while ptr1 != ptr2:
#             ptr1 = nums[ptr1]
#             ptr2 = nums[ptr2]
        
#         return ptr1

        # Find the intersection point of the two runners.
        turtle = nums[0]
        rabbit = nums[0]
        while True:
            turtle = nums[turtle]
            rabbit = nums[nums[rabbit]]
            if turtle == rabbit:
                break
        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = turtle
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1
