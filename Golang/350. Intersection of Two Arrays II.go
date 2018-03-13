func intersect(nums1 []int, nums2 []int) []int {
    dict1 := make(map[int]int, len(nums1))
    dict2 := make(map[int]int, len(nums2))
    for _, num := range nums1 {
        dict1[num]++
    }
    for _, num := range nums2 {
        dict2[num]++
    }
    ans := []int{}
    for num := range dict1 {
        j := min(dict1[num], dict2[num])
        for k := 0; k < j; k++ {
            ans = append(ans, num)
        }
    }
    return ans
}

func min(a, b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}
