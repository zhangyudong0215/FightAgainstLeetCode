/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDiffInBST(root *TreeNode) int {
    values := make([]int, 0, 100)
    recursion(root, &values)
    ans := abs(values[0], values[1])
    for i := 0; i < len(values) - 1; i++ {
        difference := abs(values[i], values[i+1])
        if ans > difference {
            ans = difference
        }
    }
    return ans
}

func recursion(node *TreeNode, values *[]int) {
    if node != nil {
        recursion(node.Left, values)
        *values = append(*values, node.Val)
        recursion(node.Right, values)
    }
}

func abs(a, b int) int {
    if a > b {
        return a - b
    } else {
        return b - a
    }
}
