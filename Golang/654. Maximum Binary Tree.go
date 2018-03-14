/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// func constructMaximumBinaryTree(nums []int) *TreeNode { // 108ms 栈
//     if nums == nil {
//         return nil
//     }
//     stack := make([]*TreeNode, 0, len(nums))
//     for _, num := range nums {
//         curr := &TreeNode{Val: num}
//         for len(stack) > 0 && stack[len(stack)-1].Val < num {
//             curr.Left = stack[len(stack)-1]
//             stack = stack[: len(stack)-1]
//         }
//         if len(stack) > 0 {
//             stack[len(stack)-1].Right = curr
//         }
//         stack = append(stack, curr)
//     }
//     return stack[0]
// }

func constructMaximumBinaryTree(nums []int) *TreeNode { // 108ms 递归 速度也不慢
    length := len(nums)
    if length == 0 {
        return nil
    } 
    if length == 1 {
        return &TreeNode{Val: nums[0]}
    }
    max := 0
    index := 0
    for i, num := range nums {
        if num > max {
            max = num
            index = i
        }
    }
    node := &TreeNode{Val: nums[index]}
    node.Left = constructMaximumBinaryTree(nums[: index])
    node.Right = constructMaximumBinaryTree(nums[index+1: ])
    return node
}
