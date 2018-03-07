func twoSum(numbers []int, target int) []int { // 4ms
    left, right := 0, len(numbers)-1
    for left < right {
        if numbers[left] == target - numbers[right] {
            break
        } else if numbers[left] > target - numbers[right] {
            right--
        } else {
            left++
        }
    }
    return []int{left+1, right+1}
}
