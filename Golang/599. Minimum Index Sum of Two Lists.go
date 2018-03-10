func findRestaurant(list1 []string, list2 []string) []string { // 52-56ms
    indexsumDict := make(map[string]int, len(list1)+len(list2))
    for index, name := range list1 {
        indexsumDict[name] = index + 1000
    }
    min := 4000
    for index, name := range list2 {
        if indexsumDict[name] >= 1000 {
            indexsumDict[name] += index + 1000
            if indexsumDict[name] < min {
                min = indexsumDict[name]
            }
        }
    }
    var ans []string
    for name := range indexsumDict {
        if indexsumDict[name] == min {
            ans = append(ans, name)
        }
    }
    return ans
}
