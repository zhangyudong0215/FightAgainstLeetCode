func arrayNesting(nums []int) int { // 24ms
    ans := 0
    for index := range nums {
        if nums[index] >= 0 {
            count := 0
            tag := index
            for nums[tag] >= 0 {
                count++
                temp := nums[tag]
                nums[tag] = -1
                tag = temp
            }
            if count > ans {
                ans = count
            }
        }
    }
    return ans
}
