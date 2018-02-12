func numJewelsInStones(J string, S string) int {
    dict := make(map[string]int, len(S))
    for _, char := range S {
        dict[string(char)]++
    }
    var total int
    for  _, char := range J {
        total += dict[string(char)]
    }
    return total
}