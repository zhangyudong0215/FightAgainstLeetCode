func numberOfArithmeticSlices(A []int) int {
    length := len(A)
    if length < 3 {
        return 0
    }
    ans := 0
    count := 0
    for i := 1; i < length - 1; i++ {
        if A[i] - A[i-1] == A[i+1] - A[i] {
            count++
        } else {
            ans += (count+1)*count/2
            count = 0
        }
    }
    ans += (count+1)*count/2
    return ans
}
