func findShortestSubArray(nums []int) int {
    numsDict := make(map[int]int, len(nums))
    indexDict := make(map[int][]int, len(nums))
    for index, num := range nums {
        numsDict[num]++
        if len(indexDict[num]) == 0 {
            indexDict[num] = append(indexDict[num], index)
            indexDict[num] = append(indexDict[num], index)
        } else {
            indexDict[num][1] = index
        }
    }
    maxcount := 0
    for num := range numsDict {
        if numsDict[num] > maxcount {
            maxcount = numsDict[num]
        }
    }
    minlength := 50001
    for num := range numsDict {
        if numsDict[num] == maxcount {
            length := indexDict[num][1] - indexDict[num][0] + 1
            if minlength > length {
                minlength = length
            }
        }
    }
    return minlength
}
