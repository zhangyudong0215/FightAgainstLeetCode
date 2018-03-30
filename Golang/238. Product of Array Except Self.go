func productExceptSelf(nums []int) []int { // 超时了
    length := len(nums)
    ans := make([]int, length)
    p := 1
    for i := 0; i < length; i++ {
        ans[i] = p
        p *= nums[i]
    }
    p = 1
    for i := length-1; i >= 0; i-- {
        ans[i] *= p
        p *= nums[i]
    }
    return ans
}