// func hasAlternatingBits(n int) bool {
//     nstr := []byte(strconv.FormatInt(int64(n), 2))
//     for i, _ := range nstr[1:] {
//         if nstr[i] == nstr[i+1] {
//             return false
//         }
//     }
//     return true
// }

func hasAlternatingBits(n int) bool {
    nstr := strconv.FormatInt(int64(n), 2)
    if strings.Contains(nstr, "00") || strings.Contains(nstr, "11") {
        return false
    } else {
        return true
    }
}
