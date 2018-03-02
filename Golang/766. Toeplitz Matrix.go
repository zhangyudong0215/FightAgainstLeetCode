// func isToeplitzMatrix(matrix [][]int) bool { // 28ms
//     r := len(matrix)
//     c := len(matrix[0])
    
//     isToeplitz := true
    
//     for i, _ := range matrix[:r-1] {
//         var s1, s2 string
//         bytes := make([]string, c-1)
        
//         for index, num := range matrix[i][:c-1] {
//             bytes[index] = strconv.Itoa(num)
//             s1 = strings.Join(bytes, "")
//         }
        
//         for index, num := range matrix[i+1][1:] {
//             bytes[index] = strconv.Itoa(num)
//             s2 = strings.Join(bytes, "")
//         }
        
//         if s1 != s2 {
//             isToeplitz = false
//         }
//     }
    
//     return isToeplitz
// }

// func isToeplitzMatrix(matrix [][]int) bool { // 20ms
//     r := len(matrix)
    
//     dict := make(map[int]int, r)
//     hasvalue := make(map[int]bool, r)
//     for i, row := range matrix {
//         for j, value := range row {
//             if !hasvalue[i-j] {
//                 dict[i-j] = value
//                 hasvalue[i-j] = true
//             } else if value != dict[i-j] {
//                 return false
//             }
//         }
//     }
//     return true
// }

func isToeplitzMatrix(matrix [][]int) bool { // 16ms
    r := len(matrix)
    c := len(matrix[0])
    
    for i := 0; i < r-1; i++ {
        if !isEqual(matrix[i][:c-1], matrix[i+1][1:]) {
            return false
        }
    }
    return true
}

func isEqual(a, b []int) bool {
    for i := range a {
        if a[i] != b[i] {
            return false
        }
    }
    return true
}