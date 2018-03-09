/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getMinimumDifference(root *TreeNode) int {
    values := make([]int, 0, 100)
    search(root, &values)
    ans := distance(values[0], values[1])
    i := 0
    for i < len(values)-1 {
        ans = min(ans, distance(values[i], values[i+1]))
        i++
    }
    return ans
}

func search(node *TreeNode, values *[]int) {
    if node != nil {
        search(node.Left, values)
        *values = append(*values, node.Val)
        search(node.Right, values)
    }
}

func min(a, b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}

func distance(a, b int) int {
    if a > b {
        return a - b
    } else {
        return b - a
    }
}
