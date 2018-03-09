func containsDuplicate(nums []int) bool {
    numsDict := make(map[int]int, len(nums))
    for _, num := range nums {
        numsDict[num]++
    }
    for num := range numsDict {
        if numsDict[num] > 1 {
            return true
        }
    }
    return false
}