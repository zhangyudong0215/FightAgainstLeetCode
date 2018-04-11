/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthSmallest(root *TreeNode, k int) int {
    stack := make([]*TreeNode, 0, 100)
    order := 0
    for len(stack) > 0 || root != nil {
        if root != nil {
            stack = append(stack, root)
            root = root.Left
        } else {
            root = stack[len(stack)-1]
            stack = stack[: len(stack)-1]
            order++
            if order == k {
                return root.Val
            }
            root = root.Right
        }
    }
    return -1
}
