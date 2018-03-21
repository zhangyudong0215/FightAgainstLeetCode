/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func largestValues(root *TreeNode) []int { // 20ms
    if root == nil {
        return []int{}
    }
    currlevel := []*TreeNode{root}
    nextlevel := []*TreeNode{}
    ans := []int{}
    for len(currlevel) > 0 {
        maxvalue := currlevel[0].Val
        for len(currlevel) > 0 {
            node := currlevel[0]
            currlevel = currlevel[1:]
            if node.Val > maxvalue {
                maxvalue = node.Val
            }
            if node.Left != nil {
                nextlevel = append(nextlevel, node.Left)
            }
            if node.Right != nil {
                nextlevel = append(nextlevel, node.Right)
            }
        }
        ans = append(ans, maxvalue)
        currlevel = nextlevel
        nextlevel = []*TreeNode{}
    }
    return ans
}
