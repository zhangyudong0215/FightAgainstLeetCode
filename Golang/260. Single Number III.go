func singleNumber(nums []int) []int {
    XOR := 0
    for _, num := range nums {
        XOR ^= num
    }
    diff := XOR & -XOR
    a := 0
    b := 0
    for _, num := range nums {
        if diff & num == 0 {
            a ^= num
        } else {
            b ^= num
        }
    }
    return []int{a, b}
}
