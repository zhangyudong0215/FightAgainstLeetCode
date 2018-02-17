func selfDividingNumbers(left int, right int) []int {
    var result []int
    var i int
    for i = left; i <= right; i++ {
        var num int = i
        request := true
        res := 0
        for {
            res = num%10
            if res == 0 || i%res != 0 {
                request = false
                break
            }
            num = num/10
            if num == 0 {
                break
            }
        }
        if request {
            result = append(result, i)
        }
    }
    return result
}

// func selfDividingNumbers(left int, right int) []int {
//     var numlist []int
//     for num := left; num <= right; num++ {
//         if isselfDividing(num) {
//             numlist = append(numlist, num)
//         }
//     }
//     return numlist
// }

// func isselfDividing(n int) bool {
//     var res int
//     var origin int = n
//     for n > 0 {
//         res = n%10
//         if res == 0 || origin%res != 0 {
//             return false
//         }
//         n /= 10
//     }
//     return true
// }
