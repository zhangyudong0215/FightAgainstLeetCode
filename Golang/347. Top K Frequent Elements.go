func topKFrequent(nums []int, k int) []int { // 20ms
    counter := make(map[int]int, len(nums))
    for _, num := range nums {
        counter[num]++
    }
    
    counts := make([]int, 0, len(counter))
    for key := range counter {
        counts = append(counts, counter[key])
    }
    
    sort.Ints(counts)
    min := counts[len(counts)-k]
    
    ans := make([]int, 0, k)
    for key := range counter {
        if counter[key] >= min {
            ans = append(ans, key)
        }
    }
    
    return ans
}
