func isOneBitCharacter(bits []int) bool { // 4ms //这个的最坏情况还是O(n) 但是想想都知道效果会好很多
    index := len(bits) - 2
    if index == -1 || bits[index] == 0 {
        return true
    } else {
        count := 0
        for index >= 0 && bits[index] == 1 {
            count++
            index--
        }
        if count%2 == 1 {
            return false
        } else {
            return true
        }
    }
}
