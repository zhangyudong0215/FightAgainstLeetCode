func fourSumCount(A []int, B []int, C []int, D []int) int {
    counter := make(map[int]int, len(A)*len(A))
    for _, a := range A {
        for _, b := range B {
            counter[a+b]++
        }
    }
    ans := 0
    for _, c := range C {
        for _, d := range D {
            ans += counter[-c-d]
        }
    }
    return ans
}
