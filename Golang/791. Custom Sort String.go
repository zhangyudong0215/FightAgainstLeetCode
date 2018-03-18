var charDict [26]int // 0ms Golang的自定义排序函数的实现

func customSortString(S string, T string) string {
    length := len(S)
    for index, char := range S {
        charDict[int(char) - 'a'] = index - length
    }
    runeT := []rune(T)
    sortCustomString(runeT)
    return string(runeT)
}

func sortCustomString(slice []rune) {
    sort.Sort(customString(slice))
}

type customString []rune

func (slice customString) Len() int {return len(slice)}

func (slice customString) Less(i, j int) bool {
    return charDict[slice[i]-'a'] < charDict[slice[j]-'a']
}

func (slice customString) Swap(i, j int) {
    slice[i], slice[j] = slice[j], slice[i]
}