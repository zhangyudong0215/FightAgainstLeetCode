// func nextGreatestLetter(letters []byte, target byte) byte { // 4ms
//     min := byte('z')
//     for _, letter := range letters {
//         if letter > target {
//             return letter
//         }
//         if letter < min {
//             min = letter
//         }
//     }
//     return min
// }

func nextGreatestLetter(letters []byte, target byte) byte { // 4ms
    min := rune('z')
    for _, letter := range letters {
        if rune(letter) > rune(target) {
            return letter
        }
        if rune(letter) < min {
            min = rune(letter)
        }
    }
    return byte(min)
}
