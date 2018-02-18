// func findComplement(num int) int {
//     var count, total, op int
//     for num > 0 {
//         if num%2 > 0 {
//             op = 0
//         } else {
//             op = 1
//         }
//         total += pow2(count) * op
//         count++
//         num /= 2
//     }
//     return total
// }

// func pow2(count int) int {
//     if count == 0 {
//         return 1
//     } else {
//         return 2*pow2(count-1)
//     }
// }

func findComplement(num int) int {
    var mask int = ^0
    for mask&num > 0 {
        mask <<= 1
    }
    return ^mask & ^num
}
