/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode2 struct { // 找不出错误
    Node *TreeNode
    Level int
}
func addOneRow(root *TreeNode, v int, d int) *TreeNode {
    if d == 1 {
        newroot := &TreeNode{Val: v, Left: root}
        return newroot
    }
    
    newroot := &TreeNode2{Node: root, Level: 1}
    
    queue := []*TreeNode2{newroot}
    
    for _, node := range queue {
        if node.Node.Left != nil {
            newleft := &TreeNode2{Node: node.Node.Left, Level: node.Level+1}
            queue = append(queue, newleft)
        }
        
        if node.Node.Right != nil {
            newright := &TreeNode2{Node: node.Node.Right, Level: node.Level+1}
            queue = append(queue, newright)
        }
        
        if node.Level == d-1 {
            newleft := &TreeNode{Val: v, Left: node.Node.Left}
            newright := &TreeNode{Val: v, Right: node.Node.Right}
            node.Node.Left = newleft
            node.Node.Right = newright
        }
    }
    return root
}
