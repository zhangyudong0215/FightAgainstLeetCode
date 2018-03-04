/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// func findTarget(root *TreeNode, k int) bool { // 深度搜索 44ms
//     node_list := make([]TreeNode, 0)
//     node_list = append(node_list, *root)
//     nums := make(map[int]bool, 0)
    
//     for len(node_list) > 0 {
//         node := node_list[len(node_list)-1]
//         node_list = node_list[:len(node_list)-1]
//         if nums[k - node.Val] {
//             return true
//         } else {
//             nums[node.Val] = true
//             if node.Left != nil {
//                 node_list = append(node_list, *node.Left)
//             }
//             if node.Right != nil {
//                 node_list = append(node_list, *node.Right)
//             }
//         }
//     }
    
//     return false
// }

func findTarget(root *TreeNode, k int) bool { // 广度搜索 56ms
    cur := []*TreeNode{root}
    nextlevel := make([]*TreeNode, 0)
    nums := make(map[int]bool, 0)
    
    for len(cur) > 0 {
        for _, node := range cur {
            if nums[k - node.Val] {
                return true
            } else {
                nums[node.Val] = true
                if node.Left != nil {
                    nextlevel = append(nextlevel, node.Left)
                }
                if node.Right != nil {
                    nextlevel = append(nextlevel, node.Right)
                }
            }
        }
        cur = nextlevel
        nextlevel = []*TreeNode{}
    }
    
    return false
}
