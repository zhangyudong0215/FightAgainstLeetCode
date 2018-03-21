func optimalDivision(nums []int) string {
    s := make([]string, 0, len(nums))
    for _, num := range nums {
        s = append(s, strconv.Itoa(num))
    }
    if len(s) == 1 {
        return s[0]
    }
    if len(s) == 2 {
        return s[0] + "/" + s[1]
    }
    return s[0] + "/(" + strings.Join(s[1:], "/") + ")"
}
