func maxProduct(words []string) int {
    lenDict := make(map[uint]int, len(words))
    for _, word := range words {
        var mask uint
        for _, char := range word {
            mask |= uint(1) << uint(char - 'a')
        }
        if len(word) > lenDict[mask] {
            lenDict[mask] = len(word)
        }
    }
    ans := 0
    for item := range lenDict {
        for item2 := range lenDict {
            if item & item2 == 0 {
                if lenDict[item] * lenDict[item2] > ans {
                    ans = lenDict[item] * lenDict[item2]
                }
            }
        }
    }
    return ans
}
