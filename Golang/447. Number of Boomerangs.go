func numberOfBoomerangs(points [][]int) int {
    total := 0
    for _, point1 := range points {
        distanceDict := make(map[int]int, 500)
        for _, point2 := range points {
            distanceDict[distance(point1, point2)]++
        }
        for d := range distanceDict {
            total += distanceDict[d] * (distanceDict[d] - 1)
            total -= distanceDict[0] * (distanceDict[0] - 1)
        }
    }
    return total
}

func distance(a, b []int) int {
    x := a[0] - b[0]
    y := a[1] - b[1]
    return x*x + y*y
}
