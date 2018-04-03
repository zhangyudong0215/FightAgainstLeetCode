func maxChunksToSorted(arr []int) int {
    ans := 0
    sum1 := 0
    sum2 := 0
    for i, num := range arr {
        sum1 += i
        sum2 += num
        if sum1 == sum2 {
            ans++
        }
    }
    return ans
}
