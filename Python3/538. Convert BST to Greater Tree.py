# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # def recursion(node, value): # 104-112ms
        #     if not node:
        #         return 0
        #     else:
        #         sumright = recursion(node.right, value)
        #         sumleft = recursion(node.left, sumright + value + node.val)
        #         node.val += sumright + value
        #         return node.val + sumleft - value
        # recursion(root, 0)
        # return root
        
        # 另外，由于python没有指针，Go的第二种方法不能实现，只能return回一个值在函数外赋值
        # 尝试使用建立数组[sum]，利用python的引用传递。虽然int型引用传递在此无法发挥作用，但是数组的引用传递应该行
        def recursion(node, sumlist): # 成功，108-116ms 
            if not node: return
            recursion(node.right, sumlist)
            sumlist[0] += node.val
            node.val = sumlist[0]
            recursion(node.left, sumlist)
        sumlist = [0]
        recursion(root, sumlist)
        return root
