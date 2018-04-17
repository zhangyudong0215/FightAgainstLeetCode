// func findMinArrowShots(points [][]int) int {
//     sort.Slice(points, func(i, j int) bool {
//         if points[i][1] == points[j][1] {
//             return points[i][0] > points[j][0]
//         }
//         return points[i][1] < points[j][1]
//     })

//     res := 0
//     end := -1 << 32
    
//     for _, point := range points {
//         if point[0] > end {
//             res++
//             end = point[1]
//         }
//     }
    
//     return res
// }

func findMinArrowShots(points [][]int) int {
    sort.Slice(points, func(i, j int) bool {
        // if points[i][0] == points[j][0] {
        //     return points[i][1] > points[j][1]
        // }
        return points[i][0] < points[j][0]
    })

    res := 0
    end := -1 << 32
    
    for _, point := range points {
        if point[0] > end {
            res++
            end = point[1]
        } else {
            if end > point[1] {
                end = point[1]
            }
        }
    }
    
    return res
}