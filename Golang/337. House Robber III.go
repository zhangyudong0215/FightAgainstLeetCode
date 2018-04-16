// /**
//  * Definition for a binary tree node.
//  * type TreeNode struct {
//  *     Val int
//  *     Left *TreeNode
//  *     Right *TreeNode
//  * }
//  */
// type TreeNode2 struct { // 思考确认这里的dp解决方案是不行的, *TreeNode2的内容相同但是地址不同
//     Node *TreeNode
//     IsRobbed bool
// }

// var dp map[*TreeNode2]int

// func rob(root *TreeNode) int {
//     return recursion(&TreeNode2{Node: root, IsRobbed: false})
// }

// func recursion(node *TreeNode2) int {
//     if _, ok := dp[node]; ok {
//         return dp[node]
//     }
    
//     if node.Node != nil {
//         if node.Node.Left == nil && node.Node.Right == nil {
//             if node.IsRobbed {
//                 dp[node] = 0
//             } else {
//                 dp[node] = node.Node.Val
//             }
//             return dp[node]
//         }
        
//         if node.IsRobbed {
//             newleft := &TreeNode2{Node: node.Node.Left, IsRobbed: false}
//             newright := &TreeNode2{Node: node.Node.Right, IsRobbed: false}
//             dp[node] = recursion(newleft) + recursion(newright)
//             return dp[node]
//         } else {
//             newleft1 := &TreeNode2{Node: node.Node.Left, IsRobbed: true}
//             newleft2 := &TreeNode2{Node: node.Node.Left, IsRobbed: false}
//             newright1 := &TreeNode2{Node: node.Node.Right, IsRobbed: true}
//             newright2 := &TreeNode2{Node: node.Node.Right, IsRobbed: false}
//             total1 := node.Node.Val + recursion(newleft1) + recursion(newright1)
//             total2 := recursion(newleft2) + recursion(newright2)
//             if total1 > total2 {
//                 dp[node] = total1
//             } else {
//                 dp[node] = total2
//             }
//             return dp[node]
//         }
//     } else {
//         return 0
//     }
// }

'''
如此分别计算抢劫node和不抢node分别得到的值
'''
func rob(root *TreeNode) int {
    var dfs func(*TreeNode) (int, int)
    
    dfs = func(node *TreeNode) (a, b int) {
        if node == nil {
            return 0, 0
        }
        
        la, lb := dfs(node.Left)
        ra, rb := dfs(node.Right)
        
        a = node.Val + lb + rb
        b = max(la, lb) + max(ra, rb)
        
        return a, b
    }
    
    a, b := dfs(root)
    return max(a, b)
}

func max(a, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}