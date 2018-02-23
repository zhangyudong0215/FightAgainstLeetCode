func fizzBuzz(n int) []string {
    ans := make([]string, n)
    for num := 1; num <= n; num++ {
        if num%15 == 0 {
            ans[num-1] = "FizzBuzz"
        } else if num%3 == 0 {
            ans[num-1] = "Fizz"
        } else if num%5 == 0 {
            ans[num-1] = "Buzz"
        } else {
            ans[num-1] = strconv.Itoa(num)
        }
    }
    return ans
}