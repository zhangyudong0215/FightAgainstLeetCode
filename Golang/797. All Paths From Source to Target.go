// func allPathsSourceTarget(graph [][]int) [][]int { // 广度搜索, 运行不了
//     target := len(graph) - 1
//     currlevel := [][][]int{}
//     currlevel[0] = [][]int{}
//     currlevel[0][0] = []int{0}
//     currlevel[0][1] = []int{0}
//     ans := make([][]int, 0, len(graph))
    
//     for len(currlevel) > 0 {
//         nextlevel := [][][]int{}
//         for len(currlevel) > 0 {
//             curr := currlevel[len(currlevel)-1][0][0]
//             nodes := currlevel[len(currlevel)-1][1]
//             currlevel = currlevel[: len(currlevel)-1]
//             if curr == target {
//                 ans = append(ans, nodes)
//             }
//             for _, newnode := range graph[curr] {
//                 item := [][]int{}
//                 item[0][0] = newnode
//                 item[1] = append(nodes, newnode)
//                 nextlevel = append(nextlevel, item)
//             }
//         }
//         currlevel = nextlevel
//     }
//     return ans
// }

// func allPathsSourceTarget(graph [][]int) [][]int { // 递归, 依然报错很奇怪
//     ans := [][]int{}
//     target := len(graph) - 1
//     recursion(&graph, &ans, 0, target, []int{0})
//     return ans
// }

// func recursion(graph, ans *[][]int, i, target int, path []int) {
//     if i == target {
//         *ans = append(*ans, path)
//         return
//     }
//     for _, j := range (*graph)[i] {
//         recursion(graph, ans, j, target, append(path, j))
//     }
// }

func allPathsSourceTarget(graph [][]int) [][]int { // 深度搜索 还是没有结果
    target := len(graph) - 1
    currlevel := make([][][]int, 0, len(graph))
    currlevel[0] = make([][]int, 0, 2)
    currlevel[0][0] = []int{0}
    currlevel[0][1] = []int{0}
    ans := make([][]int, 0, len(graph))
    
    for len(currlevel) > 0 {

        curr := currlevel[len(currlevel)-1][0][0]
        nodes := currlevel[len(currlevel)-1][1]
        currlevel = currlevel[: len(currlevel)-1]
        if curr == target {
            ans = append(ans, nodes)
        }
        for _, newnode := range graph[curr] {
            item := [][]int{}
            item[0][0] = newnode
            item[1] = append(nodes, newnode)
            currlevel = append(currlevel, item)
        }

    }
    return ans
}
