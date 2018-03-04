import "strings"
func rotatedDigits(N int) int {
    count := 0
    for num := 1; num <= N; num++ {
        s := strconv.Itoa(num)
        if isrotatedDigits(s) {
            count++
        }
    }
    return count
}

func isrotatedDigits(s string) bool {
    if strings.Contains(s, "3") || strings.Contains(s, "4") || strings.Contains(s, "7") {
        return false
    } else if strings.Contains(s, "2") || strings.Contains(s, "5") || strings.Contains(s, "6") || strings.Contains(s, "9") {
        return true
    } else {
        return false
    }
}
