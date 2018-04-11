func PredictTheWinner(nums []int) bool {
    length := len(nums)
    if length == 1 {
        return true
    }
    dp := make([][]int, 2000)
    array := recursion(&dp, &nums, 0, length-1)
    return array[0] >= array[1]
}

func recursion(dp *[][]int, nums *[]int, start, end int) []int {
    if len((*dp)[start*100+end]) > 0 {
        return (*dp)[start*100+end]
    }
    if end == (start + 1) {
        if (*nums)[start] > (*nums)[end] {
            (*dp)[start*100+end] = []int{(*nums)[start], (*nums)[end]}
        } else {
            (*dp)[start*100+end] = []int{(*nums)[end], (*nums)[start]}
        }
        return (*dp)[start*100+end]
    }
    array1 := recursion(dp, nums, start+1, end)
    array1[1] += (*nums)[start]
    array2 := recursion(dp, nums, start, end-1)
    array2[1] += (*nums)[end]
    if array1[1] > array2[1] {
        (*dp)[start*100+end] = []int{array1[1], array1[0]}
    } else {
        (*dp)[start*100+end] = []int{array2[1], array2[0]}
    }
    return (*dp)[start*100+end]
}
