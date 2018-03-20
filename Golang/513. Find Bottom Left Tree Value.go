/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findBottomLeftValue(root *TreeNode) int { // 12ms
    ans := []int{-1, 0}
    recursion(root, 0, &ans)
    return ans[1]
}

func recursion(node *TreeNode, depth int, ans *[]int) {
    if node == nil {
        return
    }
    recursion(node.Left, depth+1, ans)
    if depth > (*ans)[0] {
        (*ans)[0], (*ans)[1] = depth, node.Val
    }
    recursion(node.Right, depth+1, ans)
}
