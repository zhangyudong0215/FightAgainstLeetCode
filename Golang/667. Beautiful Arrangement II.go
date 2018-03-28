func constructArray(n int, k int) []int {
    if k == 2 {
        ans := make([]int, n)
        ans[0], ans[1], ans[2] = 1, 3, 2
        for i := 3; i < n; i++ {
            ans[i] = i + 1
        }
        return ans
    }
    
    i := 1
    j := n
    ans := make([]int, n)
    count := 0
    reverse := false
    for k > 0 {
        if k > 0 {
            ans[count] = i
            count++
            i++
            k--
            reverse = false
        }
        if k > 0 {
            ans[count] = j
            count++
            j--
            k--
            reverse = true
        }
    }
    if reverse {
        for num := j; num >= i; num-- {
            ans[count] = num
            count++
        }
    } else {
        for num := i; num <= j; num++ {
            ans[count] = num
            count++
        }
    }
    return ans
}
