func intersection(nums1 []int, nums2 []int) []int {
    hashtable := make(map[int]int, 0)
    for _, num := range nums1 {
        hashtable[num] = 1
    }
    ans := []int{}
    for _, num := range nums2 {
        if hashtable[num] == 1 {
            ans = append(ans, num)
            hashtable[num]++
        }
    }
    return ans
}
