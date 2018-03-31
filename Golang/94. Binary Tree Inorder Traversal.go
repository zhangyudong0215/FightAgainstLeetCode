/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// func inorderTraversal(root *TreeNode) []int { // 递归
//     ans := []int{}
//     recursion(root, &ans)
//     return ans
// }
// func recursion(node *TreeNode, ans *[]int) {
//     if node != nil {
//         recursion(node.Left, ans)
//         *ans = append(*ans, node.Val)
//         recursion(node.Right, ans)
//     }
// }

type TreeNode2 struct { // Golang 构造类似stack数据结构的方法
    Node *TreeNode
    Visited bool
}
func inorderTraversal(root *TreeNode) []int {
    ans := []int{}
    newroot := new(TreeNode2)
    newroot.Node = root
    newroot.Visited = false
    stack := []*TreeNode2{newroot}
    if root == nil {
        return ans
    }
    for len(stack) > 0 {
        node := stack[len(stack)-1]
        stack = stack[: len(stack)-1]
        if node.Visited {
            ans = append(ans, node.Node.Val)
            if node.Node.Right != nil {
                tempnode := new(TreeNode2)
                tempnode.Node = node.Node.Right
                tempnode.Visited = false
                stack = append(stack, tempnode)
            }
        } else {
            tempnode := new(TreeNode2)
            tempnode.Node = node.Node
            tempnode.Visited = true
            stack = append(stack, tempnode)
            if node.Node.Left != nil {
                tempnode := new(TreeNode2)
                tempnode.Node = node.Node.Left
                tempnode.Visited = false
                stack = append(stack, tempnode)
            }
        }
    }
    return ans
}
