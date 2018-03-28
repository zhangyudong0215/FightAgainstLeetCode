func findPoisonedDuration(timeSeries []int, duration int) int {
    length := len(timeSeries)
    
    if length < 2 {
        return length * duration
    }
    
    ans := 0
    i := 0
    j := 1
    for j < length {
        gap := timeSeries[j] - timeSeries[i]
        if gap <= duration {
            ans += gap
        } else {
            ans += duration
        }
        i++
        j++
    }
    return ans + duration
}
