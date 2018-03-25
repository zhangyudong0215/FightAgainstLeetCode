func numberOfLines(widths []int, S string) []int {
    total := 0
    lines := 1
    for _, char := range S {
        if total + widths[int(char)-'a'] > 100 {
            lines += 1
            total = widths[int(char)-'a']
        } else {
            total += widths[int(char)-'a']
        }
    }
    return []int{lines, total}
}
