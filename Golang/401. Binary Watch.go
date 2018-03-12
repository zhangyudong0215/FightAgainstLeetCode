import "strconv"
import "strings"
import "fmt"

func readBinaryWatch(num int) []string {
    ans := make([]string, 0, 20)
    for h := 0; h < 12; h++ {
        for m := 0; m < 60; m++ {
            s := strconv.FormatInt(int64(h), 2) + strconv.FormatInt(int64(m), 2)
            count := strings.Count(s, "1")
            if count == num {
                s = fmt.Sprintf("%d:%02d", h, m)
                ans = append(ans, s)
            }
        }
    }
    return ans
}
