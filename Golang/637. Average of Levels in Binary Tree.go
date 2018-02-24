/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func averageOfLevels(root *TreeNode) []float64 {
    layer := 0
    nums := []float64{}
    counts := []float64{}
    dealNode(root, layer, &nums, &counts)
    for i, _ := range nums {
        nums[i] /= counts[i]
    }
    return nums
}

func dealNode(node *TreeNode, layer int, nums, counts *[]float64) {
    if node != nil {
        if layer < len(*nums) {
            (*nums)[layer] += float64(node.Val)
            (*counts)[layer]++ 
        } else {
            *nums = append(*nums, float64(node.Val))
            *counts = append(*counts, 1)
        }
        dealNode(node.Left, layer+1, nums, counts)
        dealNode(node.Right, layer+1, nums, counts)
    }
}
