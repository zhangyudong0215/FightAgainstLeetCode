// func splitArraySameAverage(A []int) bool {
//     if len(A) == 1 {
//         return false
//     }
//     avg := float64(sum(A)) / float64(len(A))
//     for lenB := 1; lenB <= len(A)/2+1; lenB++ {
//         total := float64(lenB) * avg
//         if math.Ceil(total) == total {
//             if exist(int(total), lenB, 0, len(A)-1, &A) {
//                 return true
//             }
//         }
//     }
//     return false
// }

// func sum(arr []int) int {
//     total := 0
//     for _, num := range arr {
//         total += num
//     }
//     return total
// }

// func exist(tosum, lenB, first, last int, arr *[]int) bool {
//     if lenB == 0 {
//         if tosum != 0 {
//             return false
//         } else {
//             return true
//         }
//     }
    
//     if last-first+1 < lenB || first > last {
//         return false
//     }
    
//     if exist(tosum-(*arr)[first], lenB-1, first+1, last, arr) || exist(tosum, lenB, first+1, last, arr) {
//         return true
//     }
//     return false
// }

func splitArraySameAverage(A []int) bool {
    if len(A) == 1 {
        return false
    }
    avg := float64(sum(A)) / float64(len(A))
    for lenB := 1; lenB <= len(A)/2+1; lenB++ {
        total := float64(lenB) * avg
        if math.Ceil(total) == total {
            if exist(int(total), lenB, A) {
                return true
            }
        }
    }
    return false
}

func sum(arr []int) int {
    total := 0
    for _, num := range arr {
        total += num
    }
    return total
}

func exist(tosum, lenB int, arr []int) bool {
    if lenB == 0 {
        if tosum != 0 {
            return false
        } else {
            return true
        }
    }
    
    if lenB > len(arr) || len(arr) == 0 {
        return false
    }
    
    if exist(tosum-arr[0], lenB-1, arr[1:]) || exist(tosum, lenB, arr[1:]) {
        return true
    }
    return false
}