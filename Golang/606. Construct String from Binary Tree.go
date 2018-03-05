/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func tree2str(t *TreeNode) string { // 24ms
    if t == nil {
        return ""
    }
    sstring := add2str(t)
    sstrings := strings.Split(sstring, "()")
    sstring = strings.Join(sstrings, "")
    sstring = strings.Replace(sstring, "(left)", "()", -1)
    return sstring[1: len(sstring)-1]
}

func add2str(node *TreeNode) string {
    if node == nil {
        return "()"
    } else if node.Left == nil && node.Right == nil {
        return "(" + strconv.Itoa(node.Val) + ")"
    } else if node.Left != nil {
        return "(" + strconv.Itoa(node.Val) + add2str(node.Left) + add2str(node.Right) + ")"
    } else {
        return "(" + strconv.Itoa(node.Val) + "(left)" + add2str(node.Right) + ")"
    }
}
