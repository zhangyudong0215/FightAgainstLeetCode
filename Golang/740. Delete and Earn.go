import "sort"

func deleteAndEarn(nums []int) int {
	numsDict := make(map[int]int, len(nums))
	for _, num := range nums {
		numsDict[num] += num
	}

	sort.Ints(nums)

	ignore := 0
	take := 0
	prev := -100

	for _, num := range nums {
		if num != prev {
			if num != prev+1 {
				ignore, take = max(ignore, take), numsDict[num]+max(ignore, take)
			} else {
				ignore, take = max(ignore, take), numsDict[num]+ignore
			}
			prev = num
		}
	}

	return max(ignore, take)
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
