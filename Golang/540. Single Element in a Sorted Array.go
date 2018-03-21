func singleNonDuplicate(nums []int) int { // 4ms
    length := len(nums)
    head := 0
    last := length - 1
    mid := (head + last) / 2
    for check(&nums, mid, length) {
        if mid%2 == 0 {
            if nums[mid] == nums[mid-1] {
                last = mid - 1
            } else {
                head = mid + 1
            }
        } else {
            if nums[mid] == nums[mid+1] {
                last = mid - 1
            } else {
                head = mid + 1
            }
        }
        mid = (head + last) / 2
    }
    return nums[mid]
}

func check(nums *[]int, mid, length int) bool {
    if mid > 0 && mid < length-1 {
        return (*nums)[mid] == (*nums)[mid-1] || (*nums)[mid] == (*nums)[mid+1]
    } else if mid == 0 {
        return (*nums)[0] == (*nums)[1]
    } else {
        return (*nums)[length-1] == (*nums)[length-2]
    }
}