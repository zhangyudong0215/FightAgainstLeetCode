func selfDividingNumbers(left int, right int) []int {
    var result []int
    var i int
    for i = left; i <= right; i++ {
        var num int = i
        request := true
        res := 0
        for {
            res = num%10
            if res == 0 || i%res != 0 {
                request = false
                break
            }
            num = num/10
            if num == 0 {
                break
            }
        }
        if request {
            result = append(result, i)
        }
    }
    return result
}