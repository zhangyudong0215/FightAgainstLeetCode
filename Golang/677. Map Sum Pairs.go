type MapSum struct {
    dict map[string]int
}


/** Initialize your data structure here. */
func Constructor() MapSum {
    return MapSum{make(map[string]int)}
}


func (this *MapSum) Insert(key string, val int)  {
    this.dict[key] = val
}


func (this *MapSum) Sum(prefix string) int {
    ans := 0
    
    // length := len(prefix)
    // for key := range this.dict {
    //     if len(key) >= length && key[: length] == prefix {
    //         ans += this.dict[key]
    //     }
    // }
    
    for k, v := range this.dict {
        if strings.HasPrefix(k, prefix) {
            ans += v
        }
    }
    return ans
}


/**
 * Your MapSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(key,val);
 * param_2 := obj.Sum(prefix);
 */
