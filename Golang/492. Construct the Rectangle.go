func constructRectangle(area int) []int {
    W := int(math.Floor(math.Sqrt(float64(area))))
    for area % W != 0 {
        W--
    }
    return []int{area/W, W}
}
