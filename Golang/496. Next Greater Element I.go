func nextGreaterElement(findNums []int, nums []int) []int {
    ans := make([]int, 0, len(findNums))
    length := 0
    for _, num1 := range findNums {
        length++
        index := 0
        for i, num2 := range nums {
            if num1 == num2 {
                index = i
                break
            }
        }
        for _, num2 := range nums[index:] {
            if num1 < num2 {
                ans = append(ans, num2)
                break
            }
        }
        if len(ans) < length {
            ans = append(ans, -1)
        }
    }
    return ans
}
