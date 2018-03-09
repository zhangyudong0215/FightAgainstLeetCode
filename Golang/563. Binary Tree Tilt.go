/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findTilt(root *TreeNode) int {
    ans := 0
    _ = recursion(root, &ans)
    return ans
}

func recursion(node *TreeNode, ans *int) int {
    if node == nil {
        return 0
    } else {
        left := recursion(node.Left, ans)
        right := recursion(node.Right, ans)
        *ans += abs(left, right)
        return node.Val + left + right
    }
}

func abs(a, b int) int {
    if a > b {
        return a - b
    } else {
        return b - a
    }
}
