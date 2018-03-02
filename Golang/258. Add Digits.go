func addDigits(num int) int { // 8ms
    // if num == 0 {
    //     return 0
    // } else {
    //     return (num-1)%9 + 1
    // }

    return (num-1)%9 + 1 // 4ms // 关键在于Go中 -1%9 = -1 而python3中 -1%9 = -8
}
