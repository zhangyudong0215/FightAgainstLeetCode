func findDuplicate(nums []int) int {
	turtle := nums[0]
	rabbit := nums[0]
	for {
		turtle = nums[turtle]
		rabbit = nums[nums[rabbit]]
		if turtle == rabbit {
			break
		}
	}

	ptr1 := nums[0]
	ptr2 := turtle
	for ptr1 != ptr2 {
		ptr1 = nums[ptr1]
		ptr2 = nums[ptr2]
	}

	return ptr1
}
