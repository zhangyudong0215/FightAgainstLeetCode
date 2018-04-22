type pair struct {
    Num1 int
    Num2 int
}

func numFactoredBinaryTrees(A []int) int {
    dp := make(map[int]int)
    sort.Ints(A)
    numsDict := make(map[int][]pair)
    for i := 0; i < len(A); i++ {
        for j := i; j < len(A); j++ {
            product := A[i] * A[j]
            k := j + 1
            for k < len(A) && A[k] < product {
                k++
            }
            if k < len(A) && A[k] == product {
                numsDict[product] = append(numsDict[product], pair{Num1: A[i], Num2: A[j]})
            }
        }
    }
    
    ans := 0
    for _, num := range A {
        ans += recursion(&dp, &numsDict, num)
    }
    
    return ans % (1000000000 + 7)
}

func recursion(dp *map[int]int, numsDict *map[int][]pair, num int) int {
    if (*dp)[num] > 0 {
        return (*dp)[num]
    }
    if len((*numsDict)[num]) == 0 {
        (*dp)[num] = 1
    } else {
        count := 1
        for _, pair := range (*numsDict)[num] {
            if pair.Num1 == pair.Num2 {
                count += recursion(dp, numsDict, pair.Num1) * recursion(dp, numsDict, pair.Num2)
            } else {
                count += 2 * recursion(dp, numsDict, pair.Num1) * recursion(dp, numsDict, pair.Num2)
            }
        }
        (*dp)[num] = count
    }
    return (*dp)[num]
}
