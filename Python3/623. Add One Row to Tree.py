class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        # if d == 1: # 广度搜索 64ms
        #     newroot = TreeNode(v)
        #     newroot.left = root
        #     return newroot
        # lastlevel = []
        # cur = 1
        # curlevel = [root]
        # nextlevel = []
        # while cur < d:
        #     for node in curlevel:
        #         if node:
        #             nextlevel.append(node.left)
        #             nextlevel.append(node.right)
        #     lastlevel = curlevel
        #     curlevel = nextlevel
        #     nextlevel = []
        #     cur += 1
        # count = 0
        # for node in lastlevel:
        #     if node:
        #         templeft, tempright = TreeNode(v), TreeNode(v)
        #         templeft.left = curlevel[count]
        #         tempright.right = curlevel[count+1]
        #         count += 2
        #         node.left = templeft
        #         node.right = tempright
        # return root
        
        if d == 1: # 队列解决 64ms
            newroot = TreeNode(v)
            newroot.left = root
            return newroot
        queue = [(root, 1)]
        for node, level in queue:
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            if level == d-1:
                newleft = TreeNode(v)
                newleft.left = node.left
                newright = TreeNode(v)
                newright.right = node.right
                node.left = newleft
                node.right = newright
        return root
