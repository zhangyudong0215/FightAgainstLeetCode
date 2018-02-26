func countPrimeSetBits(L int, R int) int {
    count := 0
    primes := []int{2, 3, 5, 7, 11, 13, 17, 19}
    for num := L; num <= R; num++ {
        if hasPrimeSetBits(num, primes) {
            count++
        }
    }
    return count
}

func hasPrimeSetBits(x int, primes []int) bool {
    xstr := strconv.FormatInt(int64(x), 2)
    count := strings.Count(xstr, "1")
    for _, prime := range primes {
        if count == prime {
            return true
        }
    }
    return false
}
