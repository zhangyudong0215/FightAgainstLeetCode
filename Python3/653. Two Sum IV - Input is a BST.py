class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # node_list = [root] # 深度搜索 # 112ms
        # nums = set()      
        # while node_list:
        #     node = node_list.pop()
        #     if k - node.val in nums:
        #         return True
        #     nums.add(node.val)
        #     if node.left: node_list.append(node.left)
        #     if node.right: node_list.append(node.right)
        # return False
        
        cur = [root] # 广度搜索 # 104ms
        nextlevel = []
        nums = set()
        while cur:
            for node in cur:
                if k - node.val in nums:
                    return True
                nums.add(node.val)
                if node.left: nextlevel.append(node.left)
                if node.right: nextlevel.append(node.right)
            cur = nextlevel
            nextlevel = []
        return False
