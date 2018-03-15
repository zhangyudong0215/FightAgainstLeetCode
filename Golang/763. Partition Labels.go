func partitionLabels(S string) []int { // 无法执行
    index := make([]int, 0, len(S))
    indexDict := [26][2]int{}
    for i, char := range S {
        if indexDict[int(char)-'a'][0] > 0 {
            indexDict[int(char)-'a'][1] = i + 1 //加一和默认值区别开来
        } else {
            indexDict[int(char)-'a'] = [2]int{i+1, i+1}
        }
    }
    for i := 0; i < 26; i++ {
        for j := indexDict[i][0]-1; j < indexDict[i][1]-1; j++ {
            index[j] = 1
        }
    }
    fmt.Println(index)
    ans := make([]int, 0, len(S))
    last := 0
    for i, num := range index {
        if num == 0 {
            ans = append(ans, i+1-last)
            last = i + 1
        }
    }
    return ans
}
