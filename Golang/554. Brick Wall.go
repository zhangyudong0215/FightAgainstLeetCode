func leastBricks(wall [][]int) int {
    hashtable := make(map[int]int, 100)
    for _, row := range wall {
        total := 0
        for _, brick := range row[: len(row)-1] {
            total += brick
            hashtable[total]++
        }
    }
    ans := 0
    for k := range hashtable {
        if hashtable[k] > ans {
            ans = hashtable[k]
        }
    }
    return len(wall) - ans
}
