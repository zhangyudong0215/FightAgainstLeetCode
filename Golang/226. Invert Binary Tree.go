/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
    return reverse(root)
}

func reverse(node *TreeNode) *TreeNode {
    if node == nil {
        return nil
    }
    
    Left := reverse(node.Left)
    Right := reverse(node.Right)
    
    node.Left = Right
    node.Right = Left
    
    return node
}
