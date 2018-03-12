/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func diameterOfBinaryTree(root *TreeNode) int {
    ans := 0
    depth(root, &ans)
    return ans
}

func depth(node *TreeNode, ans *int) int {
    if node == nil {
        return 0
    }
    left := depth(node.Left, ans)
    right := depth(node.Right, ans)
    *ans = max(*ans, left + right)
    return max(left, right) + 1
}

func max(a, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}
