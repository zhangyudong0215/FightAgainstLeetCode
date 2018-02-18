func reverseWords(s string) string {
    string_list := strings.Split(s, " ")
    for i, s := range string_list {
        string_list[i] = reverse(s)
    }
    return strings.Join(string_list, " ")
}

func reverse(s string) string { // 关键在于string不能使用索引，只能转化为[]byte数组才行
    new_s := []byte(s)
    i, j := 0, len(new_s)-1
    for i < j { // cpp中曾经用过类似的翻转方法
        new_s[i], new_s[j] = new_s[j], new_s[i]
        i++
        j--
    }
    return string(new_s)
}
