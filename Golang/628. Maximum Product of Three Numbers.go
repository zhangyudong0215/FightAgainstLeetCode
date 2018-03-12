func maximumProduct(nums []int) int {
    num3 := []int(nums[:3])
    sort.Ints(num3)
    min1, min2 := num3[1], num3[1]
    max1, max2, max3 := num3[0], num3[0], num3[0]
    
    for _, num := range nums {
        if num > max1 {
            max1, max2, max3 = num, max1, max2
        } else if num > max2 {
            max2, max3 = num, max2
        } else if num > max3 {
            max3 = num
        }
        
        if num < min1 {
            min1, min2 = num, min1
        } else if num < min2 {
            min2 = num
        }
    }
    
    return max(min1*min2*max1, max1*max2*max3)
}

func max(a, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}
