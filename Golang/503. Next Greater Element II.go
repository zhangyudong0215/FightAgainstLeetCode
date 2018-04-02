func nextGreaterElements(nums []int) []int { // 632ms
    length := len(nums)
    stack := make([]int, 0, length)
    ans := make([]int, length)
    for i := 2*length-1; i >= 0; i-- {
        for len(stack) > 0 && nums[i%length] >= stack[len(stack)-1] {
            stack = stack[: len(stack)-1]
        }
        if len(stack) > 0 {
            ans[i%length] = stack[len(stack)-1]
            stack = append(stack, nums[i%length])
        } else {
            ans[i%length] = -1
            stack = append(stack, nums[i%length])
        }
    }
    return ans
}