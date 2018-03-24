/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findFrequentTreeSum(root *TreeNode) []int {
    sumDict := make(map[int]int)
    recursion(root, &sumDict)
    ans := []int{}
    maxvalue := 0
    for key := range sumDict {
        if sumDict[key] > maxvalue {
            maxvalue = sumDict[key]
            ans = []int{key}
        } else if sumDict[key] == maxvalue {
            ans = append(ans, key)
        }
    }
    return ans
}

func recursion(node *TreeNode, sumDict *map[int]int) int {
    if node != nil {
        left := recursion(node.Left, sumDict)
        right := recursion(node.Right, sumDict)
        total := node.Val + left + right
        (*sumDict)[total]++
        return total
    } else {
        return 0
    }
}
