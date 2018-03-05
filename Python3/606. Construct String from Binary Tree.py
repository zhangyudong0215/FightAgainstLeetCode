class Solution:
    def tree2str(self, t): # 76ms
        """
        :type t: TreeNode
        :rtype: str
        """
        def add2str(node):
            if not node:
                return '()'
            elif not node.left and not node.right:
                return '(' + str(node.val) + ')'
            elif node.left:
                return '(' + str(node.val) + add2str(node.left) + add2str(node.right) + ')'
            else:
                return '(' + str(node.val) + '(left)' + add2str(node.right) + ')'
        
        t = add2str(t)
        t = t.split('()')
        t = ''.join(t)
        t = t.replace('(left)', '()')
        return t[1: -1]
