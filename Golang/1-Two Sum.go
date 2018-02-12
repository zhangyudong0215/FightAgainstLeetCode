func twoSum(nums []int, target int) []int {
    var results = []int{0, 0}
    for i, num_i := range nums {
        for j, num_j := range nums[i+1:] {
            if num_i == target-num_j {
                results[0] = i
                results[1] = j+i+1
                break
            }
        }
    }
    return results
}