func calPoints(ops []string) int {
    scores := make([]int, 0, len(ops))
    for _, op := range ops {
        switch op {
        case "+":
            scores = append(scores, scores[len(scores)-1] + scores[len(scores)-2])
        case "D":
            scores = append(scores, 2*scores[len(scores)-1])
        case "C":
            scores = scores[:len(scores)-1]
        default:
            newint, _ := strconv.Atoi(op)
            scores = append(scores, newint)
        }
    }
    total := 0
    for _, num := range scores {
        total += num
    }
    return total
}