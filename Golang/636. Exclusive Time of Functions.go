func exclusiveTime(n int, logs []string) []int {
    stack := make([][]int, 0, n)
    ans := make([]int, n)
    for _, log := range logs {
        item := strings.Split(log, ":")
        uid, _ := strconv.Atoi(item[0])
        time, _ := strconv.Atoi(item[2])
        
        if item[1] == "start" {
            stack = append(stack, []int{time, 0})
        } else {
            output := stack[len(stack)-1]
            stack = stack[: len(stack)-1]
            ans[uid] += time - output[0] + 1 - output[1]
            if len(stack) > 0 {
                stack[len(stack)-1][1] += time - output[0] + 1
            }
        }
    }
    return ans
}
