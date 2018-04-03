func generateParenthesis(n int) []string {
    ans := make([]string, 0, 2*n)
    recursion(&ans, "", n, 0, 0)
    return ans
}

func recursion(ans *[]string, s string, n, left, right int) {
    if len(s) == 2*n {
        *ans = append(*ans, s)
    }
    if left < n {
        recursion(ans, s+"(", n, left+1, right)
    }
    if right < left {
        recursion(ans, s+")", n, left, right+1)
    }
}
