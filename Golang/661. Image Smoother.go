func imageSmoother(M [][]int) [][]int {
    r := len(M)
    c := len(M[0])
    N := make([][]int, r)
    
    for i := 0; i < r; i++ {
        for j := 0; j < c; j++ {
            N[i] = append(N[i], average(&M, i, j))
        }
    }
    return N
}

func average(M *[][]int, i, j int) int {
    row := make([]int, 0)
    col := make([]int, 0)
    row = append(row, 0)
    col = append(col, 0)
    if i > 0 {
        row = append(row, -1)
    }
    if i < len(*M)-1 {
        row = append(row, 1)
    }
    if j > 0 {
        col = append(col, -1)
    }
    if j < len((*M)[0])-1 {
        col = append(col, 1)
    }
    
    total := 0
    for _, r := range row {
        for _, c := range col {
            total += (*M)[i+r][j+c]
        }
    }
    return total / (len(row) * len(col))
}
