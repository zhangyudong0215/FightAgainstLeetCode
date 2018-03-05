/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// func convertBST(root *TreeNode) *TreeNode { // 448ms 又比python慢
//     recursion(root, 0)
//     return root
// }

// func recursion(node *TreeNode, value int) int {
//     if node == nil {
//         return 0
//     } else {
//         sumOfRight := recursion(node.Right, value)
//         sumOfLeft := recursion(node.Left, sumOfRight + value + node.Val)
//         node.Val += sumOfRight + value
//         return node.Val + sumOfLeft - value
//     }
// }

func convertBST(root *TreeNode) *TreeNode { // 上面那个是自己写的，这个抄的GitHub老哥，500ms
    sum := 0
    travel(root, &sum)
    return root
}

// 从大到小遍历 BST 并沿路更新 sum 和 节点值
func travel(root *TreeNode, sum *int) {
    if root == nil {
        return
    }
    travel(root.Right, sum)
    *sum += root.Val
    root.Val= *sum
    travel(root.Left, sum)
}