func findRelativeRanks(nums []int) []string { // 132ms
    length := len(nums)
    ordered := make([]int, length)
    copy(ordered, nums)
    sort.Ints(ordered)
    
    ranksDict := make(map[int]string, length)
    for i := 1; i <= length; i++ {
        ranksDict[ordered[i-1]] = strconv.Itoa(length - i + 1)
    }
    
    ans := make([]string, 0, length)
    for _, score := range nums {
        switch ranksDict[score] {
        case "1": ans = append(ans, "Gold Medal")
        case "2": ans = append(ans, "Silver Medal")
        case "3": ans = append(ans, "Bronze Medal")
        default: ans = append(ans, ranksDict[score])
        }
    }
    return ans
}
