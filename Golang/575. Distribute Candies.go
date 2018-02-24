// func distributeCandies(candies []int) int {
//     hashtable := make(map[int]int, len(candies))
//     for _, candy := range candies {
//         hashtable[candy]++
//     }
//     if len(hashtable) > len(candies)/2 {
//         return len(candies)/2
//     } else {
//         return len(hashtable)
//     }
// }

func distributeCandies(candies []int) int {
    n := len(candies)
    hashtable := make(map[int]bool, n)
    
    for _, candy := range candies {
        hashtable[candy] = true
    }
    
    n2 := len(hashtable)
    
    if n2 > n/2 {
        return n/2
    } else {
        return n2
    }
}
