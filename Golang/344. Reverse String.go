func reverseString(s string) string {
    bytes := []byte(s)
    i, j := 0, len(bytes)-1
    for i < j {
        bytes[i], bytes[j] = bytes[j], bytes[i]
        i++
        j--
    }
    return string(bytes)
}
