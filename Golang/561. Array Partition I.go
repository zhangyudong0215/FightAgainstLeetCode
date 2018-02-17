func arrayPairSum(nums []int) int {
    var hashtable [20001]int8
    
    for _, num := range nums {
        hashtable[num+10000]++
    }
    
    var total int
    var getvalue bool = true
    
    for num, count := range hashtable {
        for count > 0 {
            if getvalue {
                total += num - 10000
            }
            getvalue = !getvalue
            count--
        }
    }
    return total
}
