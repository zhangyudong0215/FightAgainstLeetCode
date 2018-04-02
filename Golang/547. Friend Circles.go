func findCircleNum(M [][]int) int {
    length := len(M)
    visited := make([]bool, length)
    ans := 0
    for node := 0; node < length; node++ {
        if !visited[node] {
            ans++
            DFS(node, &M, &visited)
        }
    }
    return ans
}

func DFS(node int, M *[][]int, visited *[]bool) {
    (*visited)[node] = true
    for subnode, value := range (*M)[node] {
        if value == 1 && !(*visited)[subnode] {
            DFS(subnode, M, visited)
        }
    }
}
