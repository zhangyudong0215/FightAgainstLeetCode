func findDuplicates(nums []int) []int {
    ans := make([]int, 0, len(nums)/2)
    for _, num := range nums {
        if nums[abs(num)-1] < 0 {
            ans = append(ans, abs(num))
        } else {
            nums[abs(num)-1] *= -1
        }
    }
    return ans
}

func abs(a int) int {
    if a < 0 {
        return -a
    } else {
        return a
    }
}
