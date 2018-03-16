// func countBattleships(board [][]byte) int { // 0ms
//     r := len(board)
//     c := len(board[0])
//     ans := 0
//     for i := 0; i < r; i++ {
//         for j := 0; j < c; j++ {
//             if board[i][j] == 'X' {
//                 remove(i, j, &board)
//                 ans++
//             }
//         }
//     }
//     return ans
// }

// func remove(i, j int, board *[][]byte) {
//     (*board)[i][j] = '.'
//     if i > 0 && (*board)[i-1][j] == 'X' {
//         remove(i-1, j, board)
//     }
//     if i < len(*board) - 1 && (*board)[i+1][j] == 'X' {
//         remove(i+1, j, board)
//     }
//     if j > 0 && (*board)[i][j-1] == 'X' {
//         remove(i, j-1, board)
//     }
//     if j < len((*board)[0]) - 1 && (*board)[i][j+1] == 'X' {
//         remove(i, j+1, board)
//     }
// }

func countBattleships(board [][]byte) int {
    r := len(board)
    c := len(board[0])
    ans := 0
    for i := 0; i < r; i++ {
        for j := 0; j < c; j++ {
            // 只有左和上都不是'X'的时候才记录一次
            if board[i][j] == 'X' && (i == 0 || board[i-1][j] != 'X') && (j == 0 || board[i][j-1] != 'X') {
                ans++
            }
        }
    }
    return ans
}