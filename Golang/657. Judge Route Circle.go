func judgeCircle(moves string) bool {
    var total, total2 int
    for _, char := range moves {
        if char == 'L' {
            total -= 1
        } else if char == 'R' {
            total += 1
        } else if char == 'U' {
            total2 += 1
        } else {
            total2 -= 1
        }
    }
    return total == 0 && total2 == 0
}

// // GitHub参考答案
// package Problem0657

// import "strings"

// func judgeCircle(moves string) bool {
//     up := strings.Count(moves, "U")
//     down := strings.Count(moves, "D")
//     left := strings.Count(moves, "L")
//     right := strings.Count(moves, "R")

//     return up == down && left == right
// }