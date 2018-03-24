# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # sumDict = {} # 68ms
        # if not root: return []
        # def recursion(node):
        #     if node.left:
        #         left = recursion(node.left)
        #         sumDict[left] = sumDict.get(left, 0) + 1
        #     else:
        #         left = 0
        #     if node.right:
        #         right = recursion(node.right)
        #         sumDict[right] = sumDict.get(right, 0) + 1
        #     else:
        #         right = 0
        #     return node.val + left + right
        # total = recursion(root)
        # sumDict[total] = sumDict.get(total, 0) + 1
        # ans = []
        # value = max(sumDict.values())
        # for key in sumDict.keys():
        #     if sumDict[key] == value:
        #         ans.append(key)
        # return ans
        
        sumDict = collections.defaultdict(lambda: 0)
        if not root: return []
        def recursion(node):
            if node:
                left = recursion(node.left)
                right = recursion(node.right)
                total = node.val + left + right
                sumDict[total] += 1
                return total
            else:
                return 0
        recursion(root)
        ans = []
        maxvalue = -1
        for key, value in sumDict.items():
            if value > maxvalue:
                maxvalue = value
                ans = [key]
            elif value == maxvalue:
                ans.append(key)
        return ans
