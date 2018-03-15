func complexNumberMultiply(a string, b string) string {
    aslice := strings.Split(a, "+")
    bslice := strings.Split(b, "+")
    aa, _ := strconv.Atoi(aslice[0])
    ab, _ := strconv.Atoi(aslice[1][: len(aslice[1])-1])
    ba, _ := strconv.Atoi(bslice[0])
    bb, _ := strconv.Atoi(bslice[1][: len(bslice[1])-1])
    fmt.Println(aa, ab, ba, bb)
    return strconv.Itoa(aa*ba - ab*bb) + "+" + strconv.Itoa(aa*bb + ba*ab) + "i"
}
