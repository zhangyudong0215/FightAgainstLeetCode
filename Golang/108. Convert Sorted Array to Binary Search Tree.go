/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode { // 264ms
    length := len(nums)
    if length == 0 {
        return nil
    }
    median := length / 2
    node := &TreeNode{}
    node.Val = nums[median]
    node.Left = sortedArrayToBST(nums[: median])
    node.Right = sortedArrayToBST(nums[median+1: ])
    return node
}
